#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:23:09 2019

Implemented using TensorFlow 1.0 and TFLearn 0.3.2
 
M. Zhao, S. Zhong, X. Fu, B. Tang, M. Pecht, Deep Residual Shrinkage Networks for Fault Diagnosis, 
IEEE Transactions on Industrial Informatics, 2019, DOI: 10.1109/TII.2019.2943898
 
@author: super_9527
"""
  
from __future__ import division, print_function, absolute_import
  
import tflearn
import numpy as np
import tensorflow as tf
from tflearn.layers.conv import conv_2d
  
# Data loading
from tflearn.datasets import cifar10
(X, Y), (testX, testY) = cifar10.load_data()
  
# Add noise
X = X + np.random.random((50000, 32, 32, 3))*0.1
testX = testX + np.random.random((10000, 32, 32, 3))*0.1
  
# Transform labels to one-hot format
Y = tflearn.data_utils.to_categorical(Y,10)
testY = tflearn.data_utils.to_categorical(testY,10)
  
def residual_shrinkage_block(incoming, nb_blocks, out_channels, downsample=False,
                   downsample_strides=2, activation='relu', batch_norm=True,
                   bias=True, weights_init='variance_scaling',
                   bias_init='zeros', regularizer='L2', weight_decay=0.0001,
                   trainable=True, restore=True, reuse=False, scope=None,
                   name="ResidualBlock"):
      
    # residual shrinkage blocks with channel-wise thresholds
  
    residual = incoming
    in_channels = incoming.get_shape().as_list()[-1]
  
    # Variable Scope fix for older TF
    try:
        vscope = tf.variable_scope(scope, default_name=name, values=[incoming],
                                   reuse=reuse)
    except Exception:
        vscope = tf.variable_op_scope([incoming], scope, name, reuse=reuse)
  
    with vscope as scope:
        name = scope.name #TODO
  
        for i in range(nb_blocks):
  
            identity = residual
  
            if not downsample:
                downsample_strides = 1
  
            if batch_norm:
                residual = tflearn.batch_normalization(residual)
            residual = tflearn.activation(residual, activation)
            residual = conv_2d(residual, out_channels, 3,
                             downsample_strides, 'same', 'linear',
                             bias, weights_init, bias_init,
                             regularizer, weight_decay, trainable,
                             restore)
  
            if batch_norm:
                residual = tflearn.batch_normalization(residual)
            residual = tflearn.activation(residual, activation)
            residual = conv_2d(residual, out_channels, 3, 1, 'same',
                             'linear', bias, weights_init,
                             bias_init, regularizer, weight_decay,
                             trainable, restore)
              
            # get thresholds and apply thresholding
            abs_mean = tf.reduce_mean(tf.reduce_mean(tf.abs(residual),axis=2,keep_dims=True),axis=1,keep_dims=True)
            scales = tflearn.fully_connected(abs_mean, out_channels//4, activation='linear',regularizer='L2',weight_decay=0.0001,weights_init='variance_scaling')
            scales = tflearn.batch_normalization(scales)
            scales = tflearn.activation(scales, 'relu')
            scales = tflearn.fully_connected(scales, out_channels, activation='linear',regularizer='L2',weight_decay=0.0001,weights_init='variance_scaling')
            scales = tf.expand_dims(tf.expand_dims(scales,axis=1),axis=1)
            thres = tf.multiply(abs_mean,tflearn.activations.sigmoid(scales))
            # soft thresholding
            residual = tf.multiply(tf.sign(residual), tf.maximum(tf.abs(residual)-thres,0))
              
  
            # Downsampling
            if downsample_strides > 1:
                identity = tflearn.avg_pool_2d(identity, 1,
                                               downsample_strides)
  
            # Projection to new dimension
            if in_channels != out_channels:
                if (out_channels - in_channels) % 2 == 0:
                    ch = (out_channels - in_channels)//2
                    identity = tf.pad(identity,
                                      [[0, 0], [0, 0], [0, 0], [ch, ch]])
                else:
                    ch = (out_channels - in_channels)//2
                    identity = tf.pad(identity,
                                      [[0, 0], [0, 0], [0, 0], [ch, ch+1]])
                in_channels = out_channels
  
            residual = residual + identity
  
    return residual
  
  
# Real-time data preprocessing
img_prep = tflearn.ImagePreprocessing()
img_prep.add_featurewise_zero_center(per_channel=True)
  
# Real-time data augmentation
img_aug = tflearn.ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_crop([32, 32], padding=4)
  
# Building Deep Residual Shrinkage Network
net = tflearn.input_data(shape=[None, 32, 32, 3],
                         data_preprocessing=img_prep,
                         data_augmentation=img_aug)
net = tflearn.conv_2d(net, 16, 3, regularizer='L2', weight_decay=0.0001)
net = residual_shrinkage_block(net, 1, 16)
net = residual_shrinkage_block(net, 1, 32, downsample=True)
net = residual_shrinkage_block(net, 1, 32, downsample=True)
net = tflearn.batch_normalization(net)
net = tflearn.activation(net, 'relu')
net = tflearn.global_avg_pool(net)
# Regression
net = tflearn.fully_connected(net, 10, activation='softmax')
mom = tflearn.Momentum(0.1, lr_decay=0.1, decay_step=20000, staircase=True)
net = tflearn.regression(net, optimizer=mom, loss='categorical_crossentropy')
# Training
model = tflearn.DNN(net, checkpoint_path='model_cifar10',
                    max_checkpoints=10, tensorboard_verbose=0,
                    clip_gradients=0.)
  
model.fit(X, Y, n_epoch=100, snapshot_epoch=False, snapshot_step=500,
          show_metric=True, batch_size=100, shuffle=True, run_id='model_cifar10')
  
training_acc = model.evaluate(X, Y)[0]
validation_acc = model.evaluate(testX, testY)[0]

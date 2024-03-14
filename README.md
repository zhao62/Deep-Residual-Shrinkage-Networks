# Deep-Residual-Shrinkage-Networks

The deep residual shrinkage network is a variant of deep residual networks (ResNets), and aims to improve the feature learning ability from highly noise signals or complex backgrounds. Although the method is originally developed for vibration-based fault diagnosis, it can be applied to image recognition and speech recognition as well. The major innovation is the integration of soft thresholding as nonlinear transformation layers into ResNets. Moreover, the thresholds are automatically determined by a specially designed sub-network, so that no professional expertise on threshold determination is required.

![The basic idea of deep residual shrinkage networks](https://github.com/zhao62/Deep-Residual-Shrinkage-Networks/blob/master/Basic-idea-of-DRSN.png)

The method is implemented using TensorFlow 1.0.1, TFLearn 0.3.2, and Keras 2.2.1, and applied for image classification. A small network with 3 residual shrinkage blocks is constructed in the code. More blocks and more training iterations can be used for a higher performance.

## Abstract:
This paper develops new deep learning methods, namely, deep residual shrinkage networks, to improve the feature learning ability from highly noised vibration signals and achieve a high fault diagnosing accuracy. Soft thresholding is inserted as nonlinear transformation layers into the deep architectures to eliminate unimportant features. Moreover, considering that it is generally challenging to set proper values for the thresholds, the developed deep residual shrinkage networks integrate a few specialized neural networks as trainable modules to automatically determine the thresholds, so that professional expertise on signal processing is not required. The efficacy of the developed methods is validated through experiments with various types of noise.

## Reference:

***Minghang Zhao, Shisheng Zhong, Xuyun Fu, Baoping Tang, Michael Pecht, Deep residual shrinkage networks for fault diagnosis, 
IEEE Transactions on Industrial Informatics, 2020, 16(7): 4681-4690.***

The paper has been cited over 700 times on Google Scholar.

https://scholar.google.com/citations?user=k82TzLwAAAAJ&hl=zh-CN

https://ieeexplore.ieee.org/document/8850096

http://homepage.hit.edu.cn/zhaominghang

## Results:

**(1) The performance on the manually noised Cifar10 dataset**

In the DRSN_TFLearn.py, we manually add noise to the Cifar10 dataset, and get the results of a deep residual shrinkage network. Then, we delete lines 79-88 in DRSN_TFLearn.py, make it be a deep residual network, and get its results.

Methods  | Deep residual shrinkage network  | Deep residual network
 ---- | ----- | ------  
Training accuracy  | 88.96% | 87.78%
Validation accuracy  | 84.33% | 83.99%

**(2) The performance on the un-noised Cifar10 dataset**

If we delete lines 25-27 in DRSN_TFLearn.py, the code will conduct a deep residual shrinkage network on the Cifar10 dataset without manually added noise. Then, if we delete lines 79-88 in DRSN_TFLearn.py, the code will conduct a deep residual network on the un-noised Cifar10 dataset.

Methods  | Deep residual shrinkage network  | Deep residual network
 ---- | ----- | ------  
Training accuracy  | 90.28% | 89.26%
Validation accuracy  | 85.87% | 85.57%

## Additional notes

There might be some problems in the Keras code. The TFLearn code is recommended for usage.

## Thanks for the applications

[1] Li Y, Chen H. Image recognition based on ***deep residual shrinkage Network***[C]//2021 International Conference on Artificial Intelligence and Electromechanical Automation (AIEA). IEEE, 2021: 334-337.

[2] Yu Y, Guo L, Gao H, et al. Pareto-optimal adaptive loss ***residual shrinkage network*** for imbalanced fault diagnostics of machines[J]. IEEE Transactions on Industrial Informatics, 2021, 18(4): 2233-2243.

[3] Hu H, Ma X, Shang Y. A novel method for transformer fault diagnosis based on refined ***deep residual shrinkage network***[J]. IET Electric Power Applications, 2022, 16(2): 206-223.

[4] Yao G, Chen Y, Liu Y, et al. Robust photon-efficient imaging using a pixel-wise ***residual shrinkage network***[J]. Optics Express, 2022, 30(11): 18856-18873.

[5] Cao X, Xu X, Duan Y, et al. Health status recognition of rotating machinery based on ***deep residual shrinkage network*** under time-varying conditions[J]. IEEE Sensors Journal, 2022, 22(19): 18332-18348.

[6] Yang P, Geng H, Wen C, et al. An intelligent quadrotor fault diagnosis method based on novel ***deep residual shrinkage network***[J]. Drones, 2021, 5(4): 133.

[7] Yang J, Gao T, Jiang S, et al. Fault diagnosis of rotating machinery based on one-dimensional ***deep residual shrinkage network*** with a wide convolution layer[J]. Shock and Vibration, 2020, 2020: 1-12.

[8] He Z, Yuan S, Zhao J, et al. A robust myocardial infarction localization system based on multi-branch ***residual shrinkage network*** and active learning with clustering[J]. Biomedical Signal Processing and Control, 2023, 80: 104238.

[9] Han T, Zhang Z, Ren M, et al. Speech Emotion Recognition Based on ***Deep Residual Shrinkage Network***[J]. Electronics, 2023, 12(11): 2512.

[10] Zhang Q, Zhai H, Ma Y, et al. Enhanced-***Deep-Residual-Shrinkage-Network***-Based Voiceprint Recognition in the Electric Industry[J]. Electronics, 2023, 12(14): 3017.

[11] Qin Y, Liu X, Zhang F, et al. Improved ***deep residual shrinkage network*** on near infrared spectroscopy for tobacco qualitative analysis[J]. Infrared Physics & Technology, 2023, 129: 104575.

[12] Tong Y, Wu P, He J, et al. Bearing fault diagnosis by combining a ***deep residual shrinkage network*** and bidirectional LSTM[J]. Measurement Science and Technology, 2021, 33(3): 034001.

[13] Sun F, Xu H, Zhao Y, et al. Data-driven fault diagnosis of control valve with missing data based on modeling and ***deep residual shrinkage network***[J]. Journal of Zhejiang University-SCIENCE A, 2022, 23(4): 303-313.

[14] Pei X, Dong S, Tang B, et al. Bearing running state recognition method based on feature-to-noise energy ratio and improved ***deep residual shrinkage network***[J]. IEEE/ASME Transactions on Mechatronics, 2021, 27(5): 3660-3671.

[15] Zhang S, Pan J, Han Z, et al. Recognition of noisy radar emitter signals using a one-dimensional ***deep residual shrinkage network***[J]. Sensors, 2021, 21(23): 7973.

[16] Liu X, He Y, Wang L. Adaptive transfer learning based on a two-stream densely connected ***residual shrinkage network*** for transformer fault diagnosis over vibration signals[J]. Electronics, 2021, 10(17): 2130.

[17] Zhang Z, Peng G, Tan Y, et al. THz wave detection of gap defects based on convolutional neural network improved by ***residual shrinkage network***[J]. CSEE Journal of Power and Energy Systems, 2020.

[18] Shi D, Wu Z, Zhang L, et al. Multi-Scale ***Deep Residual Shrinkage Network*** for Atrial Fibrillation Recognition[J]. International Journal of Computational Intelligence and Applications, 2022, 21(03): 2250015.

[19] Zuo G, Ren Z, Xiao X, et al. Magnetotelluric Noise Attenuation Using a ***Deep Residual Shrinkage Network***[J]. Minerals, 2022, 12(9): 1086.

[20] Sun R, Jiang Z, Su J. A ***deep residual shrinkage neural network***-based deep reinforcement learning strategy in financial portfolio management[C]//2021 IEEE 6th International Conference on Big Data Analytics (ICBDA). IEEE, 2021: 76-86.

[21] Wang J, Song Y, Mao Z, et al. EEG-Based Emotion Identification Using 1-D ***Deep Residual Shrinkage Network*** With Microstate Features[J]. IEEE Sensors Journal, 2023, 23(5): 5165-5174.

[22] Li B, Cui F. Inception module and ***deep residual shrinkage network***-based arc fault detection method for pantograph–catenary systems[J]. Journal of Power Electronics, 2022, 22(6): 991-1000.

[23] Wu X, Zhou Y, Wu D, et al. Improved ***Deep Residual Shrinkage Network*** for Intelligent Interference Recognition with Unknown Interference[J]. Sensors, 2023, 23(18): 7909.

[24] Xu Z, Ma Y, Pan Z, et al. Deep Spiking ***Residual Shrinkage Network*** for Bearing Fault Diagnosis[J]. IEEE Transactions on Cybernetics, 2022.

[25] Shi M, Huang Z, Xiao G, et al. Estimating the Depth of Anesthesia from EEG Signals Based on a ***Deep Residual Shrinkage Network***[J]. Sensors, 2023, 23(2): 1008.

[26] Liang X, Hu F, Li X, et al. Spatio-Temporal Wind Speed Prediction Based on Improved ***Residual Shrinkage Network***[J]. Sustainability, 2023, 15(7): 5871.

[27] Wang H, Wang J, Xu H, et al. DRSNFuse: ***Deep Residual Shrinkage Network*** for Infrared and Visible Image Fusion[J]. Sensors, 2022, 22(14): 5149.

[28] Yu X, Ren J, Cui Y, et al. DRSN4mCPred: accurately predicting sites of DNA N4-methylcytosine using ***deep residual shrinkage network*** for diagnosis and treatment of gastrointestinal cancer in the precision medicine era[J]. Frontiers in Medicine, 2023, 10: 1187430.

[29] Zheng G, Zhang Q, Li S. Failure diagnosis of linear arrays based on ***deep residual shrinkage network***[J]. Microwave and Optical Technology Letters, 2022, 64(9): 1627-1633.

[30] Zheng G, Zhang Q, Li S. Failure diagnosis of linear arrays based on ***deep residual shrinkage network***[J]. Microwave and Optical Technology Letters, 2022, 64(9): 1627-1633.

[31] Yue P, Xu P, Fang F, et al. Noise resistant steam generator water level reconstruction for nuclear power plant based on ***deep residual shrinkage network***[J]. Annals of Nuclear Energy, 2023, 193: 110038.

[32] Cheng L, He C. Fish Recognition Based on ***Deep Residual Shrinkage Network***[C]//2021 4th International Conference on Robotics, Control and Automation Engineering (RCAE). IEEE, 2021: 36-39.

[33] Zhang Z, Zhang C, Chen L, et al. LGMA-DRSN: a lightweight convex global multi-attention ***deep residual shrinkage network*** for fault diagnosis[J]. Measurement Science and Technology, 2023, 34(11): 115011.

[34] Lin N, Chen G, Zhou Q, et al. Dilated ***residual shrinkage network*** for SAR image despeckling[C]//2021 IEEE 6th International Conference on Signal and Image Processing (ICSIP). IEEE, 2021: 503-507.

[35] Ruan F, Dang L, Ge Q, et al. Dual-Path ***Residual “Shrinkage” Network*** for Side-Scan Sonar Image Classification[J]. Computational intelligence and neuroscience, 2022, 2022.

[36] Lu Y, Lin L, Zhang X, et al. New method for rice disease identification based on improved ***deep residual shrinkage network***[J]. Systems Science & Control Engineering, 2023, 11(1): 2177770.

[37] Xuejiao P, Shaojiang D, Xuewu P, et al. A method for rolling bearing life state recognition by combining health indicator and anti-noise ***deep residual shrinkage network***[J]. Journal of the Brazilian Society of Mechanical Sciences and Engineering, 2023, 45(1): 37.

[38] Guo W, Xu G, Wang Y. Brain visual image signal classification via hybrid dilation ***residual shrinkage network*** with spatio-temporal feature fusion[J]. Signal, Image and Video Processing, 2023, 17(3): 743-751.

[39] Yang Z, Wu B, Wang Z, et al. Image Recognition Based on an Improved ***Deep Residual Shrinkage Network***[J]. Available at SSRN 4013383, 2022.

[40] Li X. Bearing fault diagnosis method of wind turbine based on improved antinoise ***residual shrinkage network***[J]. Energy Eng, 2022, 119(2): 665-680.

[41] Wen X, Cao C, Sun Y, et al. RF Transmitter Identification and Classification Based on ***Deep Residual Shrinkage Network***[C]//2021 IEEE 23rd Int Conf on High Performance Computing & Communications; IEEE, 2021: 327-335.

[42] Li W, Lin K, Hou Y, et al. Multi-Omics Data Integration Patient Classification Method Based on Deep Dense ***Residual Shrinkage Network***[C]//2022 IEEE 34th International Conference on Tools with Artificial Intelligence (ICTAI). IEEE, 2022: 1098-1104.

[43] Wu X, Lu Y, Tang Z, et al. Communication Interference Recognition Based on Improved ***Deep Residual Shrinkage Network***[C]//2023 IEEE Symposium on Computers and Communications (ISCC). IEEE, 2023: 804-809.

[44] Zhao W, Hu S. End-to-End Auto-Encoder System for ***Deep Residual Shrinkage Network*** for AWGN Channels[J]. Journal of Computer and Communications, 2023, 11(5): 161-176.

[45] Liu G, Chen Y, Zhang X, et al. A ***deep residual shrinkage network*** based on multi-scale attention module for subsea Christmas tree valve leakage detection[J]. Measurement, 2022, 198: 110970.

[46] Ma Y, Bai Z, He B, et al. Enhanced ***Deep Residual Shrinkage Network*** Based Channel Estimation in RIS Communication System[C]//2023 25th International Conference on Advanced Communication Technology (ICACT). IEEE, 2023: 18-22.

[47] Shi B, Zhang Q, Li Y, et al. SAR image target recognition algorithm based on improved ***residual shrinkage network***[C]//2021 2nd International Seminar on Artificial Intelligence, Networking and Information Technology (AINIT). IEEE, 2021: 84-87.

[48] Cheng Q, Wu Z, Min J. Foggy Weather Monitoring Method Based on Improved ***Deep Residual Shrinkage Network*** and Radio Signal[C]//2022 3rd International Conference on Geology, Mapping and Remote Sensing (ICGMRS). IEEE, 2022: 495-499.

[49] Zhou Y, Yuan X, Cui X, et al. Fault diagnosis based on ***deep residual shrinkage network*** and maximum mean discrepancy[C]//2021 China Automation Congress (CAC). IEEE, 2021: 2340-2345.

[50] Liu J, Zhou Q, Zhang B. ***Deep Residual Shrinkage Network*** for Few-Shot Learning[C]//2021 3rd International Conference on Intelligent Control, Measurement and Signal Processing and Intelligent Oil Field (ICMSP). IEEE, 2021: 120-124.

[51] Li Y, Cao C, Zhang H, et al. Feature extraction and identification of specific radiation sources based on axial integral bispectrum and ***deep residual shrinkage network***[C]//2022 International Conference on Networking and Network Applications (NaNA). IEEE, 2022: 13-18.

[52] Ma G, Zhuo J, Gao W, et al. ***Deep Residual Shrinkage Network*** With Time-Frequency Features For Bearing Fault Diagnosis[C]//2022 IEEE International Conference on Signal Processing, Communications and Computing (ICSPCC). IEEE, 2022: 1-6.

[53] Zhao H, Guo B. EEG Signal Denoising Based on ***Deep Residual Shrinkage Network***[C]//Journal of Physics: Conference Series. IOP Publishing, 2022, 2395(1): 012076.

[54] Huang L, Gong Q. Hearing screening based on ***deep residual shrinkage network***[C]//Journal of Physics: Conference Series. IOP Publishing, 2022, 2347(1): 012006.

[55] Song Z, Cheng W, Li J, et al. A specific emitter identification method based on full bispectrum and ***deep residual shrinkage network***[C]//Thirteenth International Conference on Digital Image Processing (ICDIP 2021). SPIE, 2021, 11878: 620-629.

[56] Bai X, Ma Z, Meng G. Bearing Fault Diagnosis Based on Wavelet Transform and ***Residual Shrinkage Network***[C]//2022 International Conference on Computer Network, Electronic and Automation (ICCNEA). IEEE, 2022: 373-378.

[57] Lin J, Wen Z, Qiu Z. Multi-scale Feature Fusion ***Residual Shrinkage Network*** for COVID-19 Diagnosis[C]//2022 IEEE Smartworld, Ubiquitous Intelligence & Computing, Scalable Computing & Communications, Digital Twin, Privacy Computing, Metaverse, Autonomous & Trusted Vehicles. IEEE, 2022: 310-317.

[58] Tao H E, Jian C, Ying-you W E N. HEp-2 image recognition based on ***deep residual shrinkage network***[J]. Computer and Modernization, 2021 (01): 38.

[59] Wang Y, Luo S, Luo R, et al. Fault Diagnosis of Gearbox Based on ***Deep Residual Shrinkage Network*** in Noise Environment[C]//2022 Global Reliability and Prognostics and Health Management (PHM-Yantai). IEEE, 2022: 1-5.

[60] Lin Z. Vehicle logo recognition based on depth ***residual shrinkage network***[C]//Third International Conference on Artificial Intelligence and Computer Engineering (ICAICE 2022). SPIE, 2023, 12610: 749-753.

[61] Wei Q, Song Z, Zhao J. A network combining ***deep residual shrinkage block*** for infrared and visible image fusion[C]//Conference on Infrared, Millimeter, Terahertz Waves and Applications (IMT2022). SPIE, 2023, 12565: 776-785.

[62] Guo Y, Yan J. A CSI Based Localization and Identification Recognition Algorithm Using Multi-task Learning and ***Deep Residual Shrinkage Network***[C]//2022 IEEE 22nd International Conference on Communication Technology (ICCT). IEEE, 2022: 1770-1776.

[63] Xu L, Zhai J, Lin P, et al. Detection of malicious applications based on improved deep ***residual shrinkage network***[J]. Nanjing Xinxi Gongcheng Daxue Xuebao, 2022, 14(3): 368-378.

[64] Liang H, Xie H, Huang H, et al. Distributed Optical Fiber Sensing Signal Recognition Based on ***Deep Residual Shrinkage Network***[C]//2022 5th World Conference on Mechanical Engineering and Intelligent Manufacturing (WCMEIM). IEEE, 2022: 882-886.

[65] LI Y, HUANG T, XUN C D, et al. Single Image Super-Resolution Method Based on ***Residual Shrinkage Network*** in Real Complex Scenes[J]. Journal of Computer Applications, 2023: 0.

[66] YUAN Q, XUE S. Relation extraction algorithm based on ***residual shrinkage network***[J]. Journal of Computer Applications, 2022, 42(10): 3040.

[67] Wang J, Xue L, Gao X. Identification method of volcanic rock slices based on a ***deep residual shrinkage network***[C]//Fourth International Conference on Geoscience and Remote Sensing Mapping (GRSM 2022). SPIE, 2023, 12551: 389-394.

[68] Wang C, He T, Liu J, et al. A HEp-2 Cell Image Classification Model Based on ***Deep Residual Shrinkage Network*** Combined with Dilated Convolution[C]//International Conference on Intelligent Information Processing. Cham: Springer International Publishing, 2022: 409-418.

[69] Gu Z, Liu T, Song Y. Prediction of fracture index in tight reservoir based on depth ***residual shrinkage network***[R]. Copernicus Meetings, 2023.

[70] Zhang Z, Chen L, Zhang C, et al. GMA-DRSNs: a novel fault diagnosis method with global multi-attention ***deep residual shrinkage networks***[J]. Measurement, 2022, 196: 111203.

[71] Tong J, Tang S, Wu Y, et al. A fault diagnosis method of rolling bearing based on improved ***deep residual shrinkage networks***[J]. Measurement, 2023, 206: 112282.

[72] Cui F, Tu Y, Gao W. A Photovoltaic System Fault Identification Method Based on Improved ***Deep Residual Shrinkage Networks***[J]. Energies, 2022, 15(11): 3961.

[73] Tang P, Xu Y, Wei G, et al. Specific emitter identification for IoT devices based on ***deep residual shrinkage networks***[J]. China Communications, 2021, 18(12): 81-93.

[74] Zhang Z, Li H, Chen L, et al. Rolling bearing fault diagnosis using improved ***deep residual shrinkage networks***[J]. Shock and Vibration, 2021, 2021: 1-11.

[75] Chen W, Sun K, Li X, et al. Adaptive multi-channel ***residual shrinkage networks*** for the diagnosis of multi-fault gearbox[J]. Applied Sciences, 2023, 13(3): 1714.

[76] Zhu L, Qian K, Wang Z, et al. Heart sound classification based on ***residual shrinkage networks***[C]//2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE, 2022: 4469-4472.

[77] Yang X, Chi F, Shao S, et al. Bearing fault diagnosis under variable working conditions based on ***deep residual shrinkage networks*** and transfer learning[J]. Journal of Sensors, 2021, 2021: 1-13.

[78] Zhang Z, Li H, Chen L. ***Deep residual shrinkage networks*** with self-adaptive slope thresholding for fault diagnosis[C]//2021 7th International Conference on Condition Monitoring of Machinery in Non-Stationary Operations (CMMNO). IEEE, 2021: 236-239.

[79] Salimy A, Mitiche I, Boreham P, et al. Dynamic noise reduction with ***deep residual shrinkage networks*** for online fault classification[J]. Sensors, 2022, 22(2): 515.

[80] Xu J, Gao S, Dang X, et al. BO-MADRSN: Bayesian optimized multi-attention ***residual shrinkage networks*** for industrial soft sensor modeling[J]. Measurement, 2023: 113477.

[81] Yan C Q, Sun Y C, Zhang X, et al. A methodology to detect pilot perception of warning information by eye movement data and ***deep residual shrinkage networks***[J]. The Aeronautical Journal, 2023: 1-15.

[82] Zhang Z, Zhang C, Li H. Highly Imbalanced Fault Diagnosis of Rolling Bearings based on Variational Mode Gaussian Distortion and ***Deep Residual Shrinkage Networks***[J]. IEEE Transactions on Instrumentation and Measurement, 2023.

[83] Tiantian G, Xiaoyong Z, Lei W, et al. Research on Multi-dimensional Time Series Anomaly Detection Method Based on Temporal ***Deep Residual Shrinkage Networks***[C]//2021 IEEE 5th Information Technology, Networking, Electronic and Automation Control Conference (ITNEC). IEEE, 2021, 5: 1673-1677.

[84] Salimy A, Mitiche I, Boreham P, et al. Robust ***Deep Residual Shrinkage Networks*** for Online Fault Classification[C]//2021 29th European Signal Processing Conference (EUSIPCO). IEEE, 2021: 1691-1695.

[85] Sun K, Ren Q, Jin H, et al. Deep Spatio-Temporal ***Residual Shrinkage Networks*** for Traffic Prediction[C]//2022 IEEE 24th Int Conf on High Performance Computing & Communications. IEEE, 2022: 1036-1041.

[86] Cheng M, Gao Q, Bai Z, et al. Research on Hearing-Impaired EEG Emotion Recognition Based on ***Deep Residual Shrinkage Networks***[C]//2023 42nd Chinese Control Conference (CCC). IEEE, 2023: 8677-8682.

[87] Chunxing Y, Quan L, Kun C, et al. ***Deep Residual Shrinkage Networks*** for Adaptive Classification of EEG Error-Related Potentials[C]//2022 28th International Conference on Mechatronics and Machine Vision in Practice (M2VIP). IEEE, 2022: 1-6.

[88] Ma Y, Wang C, Jiang C, et al. ***Deep Residual Shrinkage Networks*** for EMG-based Gesture Identification[J]. arXiv preprint arXiv:2202.02984, 2022.

[89] CHI F, YANG X, SHAO S, et al. Bearing fault diagnosis under variable working conditions based on ***deep residual shrinkage networks***[J]. Computer Integrated Manufacturing System, 2023, 29(4): 1146.

[90] 刘徐洲, 李孝忠. 基于***深度残差收缩网络***和迁移学习的变工况轴承故障诊断[J]. 天津科技大学学报, 2023, 38(04): 76-80.

[91] 龚玉晓, 高淑萍. 基于改进***深度残差收缩网络***的心电信号分类算法[J]. 应用数学和力学, 2023, 44(08): 977-988.

[92] 卞文彬, 邓艾东, 刘东川, 赵敏, 刘洋, 李晶. 基于改进***深度残差收缩网络***的风电机组滚动轴承故障诊断方法[J]. 机械工程学报, 2023, 59(12): 202-214.

[93] 李颖, 黄超, 孙成栋, 徐勇. 真实复杂场景下基于***残差收缩网络***的单幅图像超分辨率方法[J]. 计算机应用, 2023, 43(12): 3903-3910.

[94] 麻建新, 袁春华, 李翔宇. 针对油井长时程基于***深度残差收缩网络***的模型故障诊断[J]. 科技资讯, 2023, 21(14): 116-119.

[95] 梁惠康, 谢浩燊, 黄红斌, 刘伟平. 基于改进***深度残差收缩网络***的DAS信号识别[J]. 激光与光电子学进展: 1-13.

[96] 林立媛. 基于***深度残差收缩网络***的水稻病害识别方法研究[D]. 黑龙江八一农垦大学, 2023.

[97] 高学金, 李虎, 韩华云, 齐咏生. 基于域自适应***残差收缩网络***的滚动轴承故障诊断[J]. 组合机床与自动化加工技术, 2023,(05): 164-168+173.

[98] 杨正理, 吴馥云, 陈海霞. ***深度残差收缩网络***的多特征锅炉炉管声波信号故障识别[J]. 智能系统学报: 1-10.

[99] 刘汉举. 一种基于机器视觉和***深度残差收缩网络***的智能制造缺陷检测方法[J]. 中国科技论文, 2023, 18(04): 462-468.

[100] 陈姮, 陈志翔, 申高宁, 王舒琪. 基于***深度残差收缩网络***的恶意代码分类[J]. 闽南师范大学学报(自然科学版), 2023, 36(01): 50-58.

[101] 曹珂璐. 基于***深度残差收缩网络***的风力发电机齿轮箱故障诊断方法研究[D]. 陕西科技大学, 2023.

[102] 庄全胜. 基于***深度残差收缩网络***的自然情境下的多模态情感识别研究[D]. 哈尔滨理工大学, 2023.

[103] 高云鹏, 孟雪晴, 张其旺, 王庆凯, 杨佳伟, 董一隆. 基于深度宽卷积***残差收缩网络***的球磨机负荷状态诊断[J]. 湖南大学学报(自然科学版), 2023, 50(02): 102-111.

[104] 曹珂璐, 任工昌, 桓源, 张路平. 基于***深度残差收缩网络***的风力发电机齿轮箱故障诊断[J]. 机械与电子, 2023, 41(02): 66-70+75.

[105] 魏煦航, 曹少中, 杨彦红, 项璇. 基于***深度残差收缩网络***的滚动轴承健康因子构建方法[J]. 印刷与数字媒体技术研究, 2023,(01): 71-79.

[106] 王玉, 张燕红, 周昱洲, 林鸿斌. 基于***深度残差收缩网络***的校园垃圾图像分类[J]. 吉林大学学报(信息科学版), 2023, 41(01): 186-192.

[107] 翁敏超, 王海瑞, 朱贵富. 小波变换和***深度残差收缩网络***在齿轮箱故障诊断中的应用[J]. 机械科学与技术: 1-7.

[108] 吴萌, 高怡宁, 王佳. 结合特征聚类和***深度残差收缩网络***的壁画风格迁移[J]. 激光与光电子学进展: 1-17.

[109] 樊庆玲, 杨宏波, 郭涛, 张伟, 王威廉. FrFT-Bark域特征提取与CNN***残差收缩网络***心音分类算法[J]. 云南大学学报(自然科学版), 2023, 45(03): 564-574.

[110] 杨正理, 吴馥云, 陈海霞. 基于改进***深度残差收缩网络***的旋转机械故障诊断[J]. 机电工程, 2023, 40(03): 344-352.

[111] 戴江涛, 申静. 基于双流***残差收缩网络***的人体动作识别方法[J]. 信息技术与信息化, 2022, (10): 106-110.

[112] 田钦文, 冯辅周, 李鸣, 陈晓明, 朱俊臻, 胡浩, 宋超. 基于一维***深度残差收缩网络***的汇流行星排齿轮裂纹故障诊断[J]. 振动与冲击, 2022, 41(19): 198-206.

[113] 彭涛, 伦功仁, 赵峰. 基于***深度残差收缩网络***的船用补水泵滚动轴承故障诊断[J]. 风机技术, 2022, 64(S1): 37-42.

[114] 胡从强, 曲娜, 张帅, 冮震. 连续小波变换和具有注意力机制的***深度残差收缩网络***在低压串联电弧故障检测中的应用[J]. 电网技术, 2023, 47(05): 1897-1905.

[115] 赵莹莹, 何怡刚, 邢致恺, 杜博伦. 基于信息融合与***深度残差收缩网络***的DAB变换器开路故障诊断方法[J]. 电力自动化设备, 2023, 43(02): 112-118.

[116] 王彦博, 吴俊勇, 季佳伸, 李栌苏, 李宝琴. 基于***深度残差收缩网络***的电力系统暂态频率安全集成评估[J]. 电网技术, 2023, 47(02): 482-494.

[117] 吴爱华, 彭金喜. 基于***深度残差收缩网络***的信号调制类型识别[J]. 电子信息对抗技术, 2022, 37(04): 24-30.

[118] 梁日强, 胡燕林, 蒋占四. 基于改进的***残差收缩网络***的带钢表面缺陷识别[J]. 组合机床与自动化加工技术, 2022, (06): 82-85.

[119] 殷磊. 基于***残差收缩网络***的旋转机械故障诊断方法研究[D]. 哈尔滨工业大学, 2022.

[120] 黄莹. 基于***深度残差收缩网络***的心律失常分类算法研究[D]. 广西大学, 2022.

[121] 张晓东. 基于***深度残差收缩网络***滚动轴承故障识别研究[D]. 沈阳工业大学, 2022.

[122] 张晓锋. 基于多尺度特征融合与***残差收缩网络***的齿轮箱故障诊断研究[D]. 石家庄铁道大学, 2022.

[123] 梁日强. 基于***残差收缩网络***的带钢表面缺陷识别方法研究[D]. 桂林电子科技大学, 2022.

[124] 谈诚, 卢德龙, 张丹青. 基于双层***深度残差收缩网络***的台区窃电用户识别方法[J]. 电力大数据, 2022, 25(05): 1-9.

[125] 李雪松, 李劲华, 吕智涵. 基于改进***深度残差收缩网络***的轴承故障诊断[J]. 青岛大学学报(自然科学版), 2022, 35(02): 38-43+50.

[126] 李瑞航, 吴红兰, 孙有朝, 吴华聪. 基于***深度残差收缩网络***多特征融合语音情感识别[J]. 数据采集与处理, 2022, 37(03): 542-554.

[127] 唐震, 乔晓强, 张涛, 苏健, 杨小蒙. 基于***深度残差收缩网络***的辐射源个体识别方法[J]. 电子测量技术, 2022, 45(09): 168-174.

[128] 张翔, 孙宪坤, 胡峻, 尹京苑, 熊玉洁. 结合数据扩增与***残差收缩网络***的地震短临预测[J]. 地震, 2022, 42(02): 74-88.

[129] 李晓峰, 向辉, 杨青桦. 噪声干扰下基于二维特征图和***深度残差收缩网络***的齿轮箱故障诊断[J]. 机床与液压, 2022, 50(07): 187-191.

[130] 刘晓锋, 高丽梅. 基于改进空间***残差收缩网络***模型的农作物病虫害识别[J]. 山东农业大学学报(自然科学版), 2022, 53(02): 259-264.

[131] 袁思邈. 基于宽广***残差收缩网络***的图像分类研究[D]. 山东理工大学, 2022.

[132] 孙丰, 徐贺, 赵宇晗, 张渝东. 数据驱动的基于数学模型插补和改进***深度残差收缩网络***的调节阀状态监控（英文）[J]. Journal of Zhejiang University-Science A(Applied Physics & Engineering), 2022, 23(04): 303-314.

[133] 王之卓, 吕健鸿, 王中鹏. 基于***深度残差收缩网络***的LDPC译码算法[J]. 浙江科技学院学报, 2022, 34(01): 35-41.

[134] 车思韬, 郭荣佐, 李卓阳, 杨军. 注意力机制结合***残差收缩网络***对遥感图像分类[J]. 计算机应用研究, 2022, 39(08): 2532-2537.

[135] 陈玲玲, 毕晓君. 基于***残差收缩网络***的睡眠脑电分期[J]. 仪器仪表学报, 2022, 43(02): 148-155.

[136] 马鑫, 尚毅梓, 胡昊, 徐杨. 基于数据特征增强和***残差收缩网络***的变压器故障识别方法[J]. 电力系统自动化, 2022, 46(03): 175-183.

[137] 孟庆旭, 沈功田, 俞跃, 胡斌, 王宝轩, 李志农. ***深度残差收缩网络***的含噪微泄漏超声识别方法[J]. 应用声学, 2022, 41(06): 964-972.

[138] 袁泉, 薛书鑫. 基于***残差收缩网络***的关系抽取算法[J]. 计算机应用, 2022, 42(10): 3040-3045.

[139] 许历隆, 翟江涛, 林鹏, 崔永富. 一种基于改进***深度残差收缩网络***的恶意应用检测方法[J]. 南京信息工程大学学报(自然科学版), 2022, 14(03): 368-378.

[140] 高晔, 郭松宜, 厍向阳. 基于***残差收缩网络***的遥感图像目标检测算法[J]. 计算机工程与应用, 2022, 58(17): 93-100.

[141] 柯翔, 包乾宗, 赵全波. 基于***深度残差收缩网络***的波阻抗反演建模[A]. 中国地球物理学会, 2021: 230-231.

[142] 张力, 常俊, 武浩, 黄彬, 刘欢. ***深度残差收缩网络***下的定位与行为联合识别[J]. 计算机工程与应用, 2022, 58(21): 205-212.

[143] 李昊璇, 闫新艳. 基于***深度残差收缩网络***的商品图像识别[J]. 测试技术学报, 2021, 35(04): 294-299+322.

[144] 卢锦玲, 郭鲁豫. 基于改进***深度残差收缩网络***的电力系统暂态稳定评估[J]. 电工技术学报, 2021, 36(11): 2233-2244.

[145] 宋子豪, 程伟, 彭岑昕, 李晓柏. 基于CWD和***残差收缩网络***的调制方式识别方法[J]. 系统工程与电子技术, 2021, 43(11): 3371-3379.

[146] 何涛, 陈剑, 闻英友. 基于***深度残差收缩网络***的HEp-2图像识别[J]. 计算机与现代化, 2021, (01): 38-42.

[147] 杨偲乐. 基于混合域注意力机制的卷积网络和***残差收缩网络***的轴承故障诊断[D]. 北京邮电大学, 2020.

[148] 李天慧, 谢云澄, 车荣花, 梁迪昌, 王健. 基于***DRSN***-BiLSTM的电力信息网络入侵检测模型[J]. 电力信息与通信技术, 2023, 21(09): 30-37.

[149] 刘高辉, 宋博武. ***DRSN***与集成融合的OFDM辐射源个体识别方法[J]. 信号处理: 1-14.

[150] 黄湛钧, 董鑫, 卢沐宇, 张瑞涛, 闫钊阳, 张安. 基于***DRSN***与电压幅值分析的航空HVDC系统中逆变器故障诊断[J]. 航空学报: 1-9.

[151] 王小聪, 郝正航, 陈卓. 基于***DRSN***-CW-LSTM网络的锂电池荷电状态预测[J]. 南方电网技术: 1-9.

[152] 赵光宏. 基于Conformer-***DRSN***的新冠肺炎CT图像检测系统的研究与实现[D].辽宁大学, 2023.

[153] 王磊, 孙志成, 王磊, 陈端兵, 蒋家玮. 基于***DRSN***-CW和LSTM的轴承故障诊断[J]. 电子科技大学学报, 2022, 51(06): 921-927.

[154] 文井辉, 伍荣森, 李帅永, 韩明秀. 基于***DRSN***和优化BiLSTM的轴承剩余寿命预测方法[J]. 计算机集成制造系统: 1-18.

[155] 吴卫堃, 宫士营, 郑耀华, 单超, 董传友. 基于***DRSN***的高噪声环境下XLPE电缆故障识别[J]. 电气传动, 2022, 52(16): 75-80.

[156] 毛浩英, 孙有朝, 李龙彪, 晏传奇. 基于改进***DRSN***的航空发动机故障风险预警模型[J]. 航空动力学报: 1-12.

[157] 胡昊, 马鑫, 徐杨, 任玉峰. 基于权重修正和***DRSN***-LSTM模型的向家坝下游水位多时间尺度预测[J]. 水利水电技术(中英文), 2022, 53(07): 46-57.

[158] 赵杰, 陈志刚, 赵志川, 张楠. 基于同步提取变换和***DRSN***的滚动轴承故障诊断研究[J]. 重庆理工大学学报(自然科学), 2021, 35(01): 138-144.

[159] 朱容波, 王晗铭, 李松泉. 基于纹理-颜色多尺度***残差收缩网络***的玉米病害识别方法[P]. 湖北省：CN116630960A, 2023-08-22.

[160] 赵振喜, 宋京哲, 倪凤祥等. 一种基于***残差收缩网络***和长短期记忆网络的变电站设备寿命预测方法[P]. 吉林省：CN116595853A, 2023-08-15.

[161] 孙逸潇, 赵治栋, 张显飞等. 一种基于改进***残差收缩网络***的身份识别方法[P]. 浙江省：CN116305048A, 2023-06-23.

[162] 顾军华, 邢佳豪, 张亚娟等. 基于多尺度***残差收缩网络***的多普勒雷达心跳检测方法[P]. 天津市：CN115969388A, 2023-04-18.

[163] 白智全, 马媛媛, 贺邦玮等. 基于改进***残差收缩网络***的RIS通信系统信道估计方法[P]. 山东省：CN115833974A, 2023-03-21.

[164] 陈阳, 杨燕琳, 王朝阳等. 一种基于改进***深度残差收缩网络***的二手车价格预测方法[P]. 青海省：CN115618727A, 2023-01-17.

[165] 苏依拉, 张旋, 仁庆道尔吉等. 一种基于***深度残差收缩网络***和seq2seq的蒙汉机器翻译方法[P]. 内蒙古自治区：CN115577720A, 2023-01-06.

[166] 杨涛, 徐琳. 基于多通道***深度残差收缩网络***的冰雹天气识别与分类方法[P]. 江苏省：CN114755745B, 2022-12-20.

[167] 徐慧, 吴一凡, 王皓晨等. 一种基于***深度残差收缩网络***的眼病诊断方法[P]. 江苏省：CN115456981A, 2022-12-09.

[168] 张玉梅, 库银涛, 吴晓军等. 基于***深层残差收缩网络***的隐函数文物三维模型重建方法[P]. 陕西省：CN115330944A, 2022-11-11.

[169] 蒋文波, 刘安顺, 李潘等. 基于***深度残差收缩网络***和生成对抗网络的去图像运动模糊方法[P]. 四川省：CN112734678B, 2022-11-08.

[170] 高世伟, 许金鹏, 党小超等. 一种基于贝叶斯优化的多注意力融合***深度残差收缩网络***软测量建模方法[P]. 甘肃省：CN115203954A, 2022-10-18.

[171] 王立辉, 张文鹏, 许宁徽. 基于改进***残差收缩网络***的FOCS故障诊断方法[P]. 江苏省：CN115130505A,2022-09-30.

[172] 李文耀, 林恺, 高建等. 一种基于***深度残差收缩网络***的多组学与表型关联预测方法[P]. 辽宁省：CN115132279A, 2022-09-30.

[173] 徐滌平, 宋伊晨, 周水清等. 基于***深度残差收缩网络***的集成灶风机故障诊断方法[P]. 浙江省：CN114897029A, 2022-08-12.

[174] 庄全胜, 吕鑫淼. 一种基于***深度残差收缩网络***的多模态情感识别方法[P]. 黑龙江省：CN114758676A, 2022-07-15.

[175] 严玉琮, 邵志刚. 一种基于***深度残差收缩网络***的犬鼻纹识别方法和模型[P]. 广东省：CN114511886A, 2022-05-17.

[176] 王正国, 王迪, 王新等. 一种多尺度元***深度残差收缩网络***的机械故障在线诊断方法[P]. 河南省：CN114492642A, 2022-05-13.

[177] 章坚武, 周晔. 一种基于***深度残差收缩网络***的语音欺骗检测方法[P]. 浙江省：CN114495950A, 2022-05-13.

[178] 邓艾东, 卞文彬, 刘洋等. 基于改进***深度残差收缩网络***的滚动轴承故障诊断方法[P]. 江苏省：CN114441173A, 2022-05-06.

[179] 任燕, 张瑞, 汤何胜等. 基于多模态***深度残差收缩网络***的液压防水阀故障诊断方法[P]. 浙江省：CN114358189A, 2022-04-15.

[180] 张涛, 唐震, 乔晓强等. 基于***深度残差收缩网络***的辐射源个体识别方法及装置[P]. 江苏省：CN114091545A, 2022-02-25.

[181] 覃程锦, 陶建峰, 刘成良等. 基于深度卷积***残差收缩网络***的刀具磨损预测方法和系统[P]. 上海市：CN114048958A, 2022-02-15.

[182] 胡斌, 沈功田, 孟庆旭等. 一种基于***深度残差收缩网络***含噪微泄漏识别方法[P]. 北京市：CN114036985A, 2022-02-11.

[183] 陈思哲, 杨欣, 曹云依等. 一种基于新型***深度残差收缩网络***的图像超分辨率重建方法[P]. 江苏省：CN113962857A, 2022-01-21.

[184] 蒋占四, 梁日强, 滕制等. 基于改进***残差收缩网络***的带钢缺陷检测方法[P]. 广西壮族自治区：CN113838208A, 2021-12-24.

[185] 刘凯, 柏建军, 张日东. 一种混合***深度残差收缩网络***与XGBoost算法的工业过程性能评估方法[P]. 浙江省：CN113705661A, 2021-11-26.

[186] 周冠华, 陈柳君, 苗昊雨等. 一种基于***深度残差收缩网络***的水深遥感反演方法[P]. 北京市：CN113639716A, 2021-11-12.

[187] 李智军, 光启宏, 李国欣. 一种基于***残差收缩网络***的设备诊断方法及系统[P]. 安徽省：CN113537382A, 2021-10-22.

[188] 吴彩萍, 申莲莲, 张蓉等. 基于***深度残差收缩网络***的车辆碰撞检测方法及装置[P]. 四川省：CN113177536B, 2021-09-10.

[189] 苏炯龙, 任晓天, 孙若宇等. 基于深度强化学习和***深度残差收缩网络***的投资方法及智能体[P]. 江苏省：CN112950374A, 2021-06-11.

[190] 王海凤, 王凯江, 白倩等. 基于注意力机制的***DRSN***和LSTM的网络入侵检测方法[P]. 内蒙古自治区：CN116684138A, 2023-09-01.

[191] 胡昊, 马鑫, 郑野等. 基于权重修正和***DRSN***-LSTM模型的水位预测方法[P]. 河南省：CN115099500B, 2023-04-18.

[192] 张淑慧, 兰田, 王连海等. 一种基于HOG和***DRSN***-LSTM的智能合约漏洞检测方法及系统[P]. 山东省：CN115937878A, 2023-04-07.

[193] 董亮, 胡思源, 张宇航等. 一种基于CEEMD-***DRSN***的离心泵空化状态识别方法[P]. 江苏省：CN115600126A, 2023-01-13.

[194] 卢德龙, 童充, 黄馨仪等. 一种基于***DRSN***的台区窃电用户识别方法、系统及装置[P]. 江苏省：CN115147135A, 2022-10-04.

[195] 李盛, 邱阳, 金亮等. 基于***DRSN***和person相关系数的道床故障预警方法[P]. 湖北省：CN113408441B, 2022-06-10.

[196] 缪小冬, 虞浒, 王华. 基于GAF-***DRSN***的滚动轴承故障诊断方法[P]. 江苏省：CN114595730A, 2022-06-07.

[197] 史宇杰. 一种基于***DRSN***的液基薄层细胞涂片数字病理图像检测方法[P]. 江苏省：CN114170198A, 2022-03-11.

[198] 文井辉, 李帅永, 韩明秀等. 基于***DRSN***和麻雀搜索优化BiLSTM的机械设备剩余寿命预测方法[P]. 重庆市：CN113723007A, 2021-11-30.

[199] 张夏林, 刘东涛, 翁正平等. 基于***残差收缩模块***与注意力机制的岩石薄片图像识别方法[P]. 湖北省：CN113486929B, 2023-02-24.

[200] 童轶之. 结合***残差收缩***和长短期记忆网络的轴承故障诊断[D]. 浙江理工大学, 2023.

[201] 朱文杰, 苗芳荣, 李云飞等.改进***DRSN***的抽油机轴承故障诊断系统[J]. 电工技术, 2023(16): 246-250.

[202] 杨晓岗. 基于改进***残差收缩网络***的不平衡时序数据故障诊断方法研究[D]. 北京化工大学, 2023.

[203] 唐世钰, 童靳于, 郑近德等. 改进的***深度残差收缩网络***轴承故障诊断方法[J]. 振动与冲击, 2023, 42(18): 217-224+285.

[204] 杜睿山, 程永昌, 孟令东. 基于***深度残差收缩网络***的油气柱高度预测[J]. 计算机技术与发展, 2023, 33(09): 175-181.

[205] 竹杭杰, 郭建新, 张雨帅等. 基于***DRSN***的通信信号调制方式识别方法[J/OL]. 无线电工程: 1-9 [2023-11-12].

[206] 张让勇, 郭文杰, 闫蕊等. 一种基于***DRSN***-CS和BiGRU+MLP模型的机械轴承剩余使用寿命预测方法[P]. 山东省：CN116842379A, 2023-10-03.

[207] 王康, 刘彩云, 熊杰等. 基于全卷积***残差收缩网络***的地震波阻抗反演[J/OL]. 物探与化探: 1-9 [2023-11-20].

[208] 陈琳伟, 应娉婷, 汤何胜等. 基于多传感器数据融合和***深度残差收缩网络***的轴向柱塞泵故障诊断[J]. 液压与气动, 2023, 47(11): 142-149.

[209] 尹建国, 盛文, 蒋伟. 基于***深度残差收缩网络***的雷达空中目标识别[J/OL]. 系统工程与电子技术: 1-8 [2023-11-29].

[210] 李天桢, 高世伟, 党小超等. 一种基于遮蔽卷积注意力***残差收缩网络***的软测量建模方法[P]. 甘肃省：CN116910483A, 2023-10-20.

[211] Song X, Zhang Q, Sun R, et al. A Hybrid Deep Learning Prediction Method of Remaining Useful Life for Rolling Bearings Using Multiscale Stacking ***Deep Residual Shrinkage Network***[J]. International Journal of Intelligent Systems, 2023, 6665534.

[212] Huang X, Song Z, Ji C, et al. Research on a Classification Method for Strip Steel Surface Defects Based on Knowledge Distillation and a Self-Adaptive ***Residual Shrinkage Network***[J]. Algorithms, 2023, 16(11): 516.

[213] Zhang Z, Zhang C, Zhang X, et al. ***Deep residual shrinkage networks*** with adaptively convex global parametric rectifier linear units for fault diagnosis[J]. Measurement Science and Technology, 2023, 35(2): 025023.

[214] Wu W, Peng H, Zhu H, et al. Mvc-Rsn: A Malware Variants Classification Method Based on ***Residual Shrinkage Networks***[J]. Available at SSRN 4612610.

[215] 赵睿, 刘硕佳, 陈建勇. 基于***深度残差收缩网络***的非授权频段无线信号识别方法[P]. 福建省：CN117312942A, 2023-12-29.

[216] 杨阿锋, 庄立旭, 杨卓霖等. 融合注意力机制与***深度残差收缩网络***的水声目标识别方法[P]. 浙江省：CN117310668A, 2023-12-29.

[217] 贾广飞, 李明. 一种基于改进***深度残差收缩网络***的旋转机械故障诊断方法[P]. 河北省：CN117313003A, 2023-12-29.

[218] 邓艾东, 卞文彬, 刘洋等. 基于改进***深度残差收缩网络***的滚动轴承故障诊断方法[P]. 江苏省：CN114441173B, 2023-11-24.

[219] 陈晓兵, 郭舒心, 张闯闯等. 一种基于改进***深度残差收缩网络***的轴承故障诊断方法[P]. 江苏省：CN117112991A, 2023-11-24.

[220] 尹柏强, 程怡, 王若宇等. 基于改进一维***深度残差收缩网络***的电能质量扰动识别方法[P]. 安徽省：CN117093519A, 2023-11-21.

[221] 张璐莹, 卞雨辰, 蒋鹏等. 一种基于改进***残差收缩网络***的管道漏磁图像识别方法[P]. 黑龙江省：CN117058443A, 2023-11-14.

[222] 赵建, 姜伟. 融合改进TCN与***DRSN***的IoT入侵检测模型[J/OL]. 小型微型计算机系统:1-10 [2024-01-29].

[223] Sun Y, Zhang J, Zhang Y. New Deep Learning Network (***Deep Residual Shrinkage Network***) Is Applied for Lithology Identification To Search for the Reservoir of CO2 Geological Storage[J]. Energy & Fuels, 2024.

[224] Ehteram M, Afshari Nia M, Panahi F, et al. Gaussian mutation–orca predation algorithm–***deep residual shrinkage network (DRSN)***–temporal convolutional network (TCN)–random forest model: an advanced machine learning model for predicting monthly rainfall and filtering irrelevant data[J]. Environmental Sciences Europe, 2024, 36(1): 13.

[225] Sun Y, Pang S, Zhang J, et al. DRSN-GAF: ***Deep Residual Shrinkage Network (DRSN)*** for Lithology Classification through Well Logging Data Transformed by Gram Angle Field[J]. IEEE Geoscience and Remote Sensing Letters, 2023.

[226] Zhang L, Bian Y, Jiang P, et al. Improving Pipeline Magnetic Flux Leakage (MFL) Detection Performance with Mixed Attention Mechanisms (AM) and ***Deep Residual Shrinkage Networks (DRSN)***[J]. IEEE Sensors Journal, 2024.

[227] Li Q, Lu T, Lai C, et al. Lithium-ion battery capacity estimation based on fragment charging data using ***deep residual shrinkage networks*** and uncertainty evaluation[J]. Energy, 2023: 130208.

[228] 陈仁祥, 张晓, 朱玉清等. 基于***深度残差收缩***迁移***网络***的复杂工况下滚动轴承故障诊断[J]. 振动与冲击, 2024, 43(03): 194-200.

[229] 郭松宜. 基于***残差收缩网络***与注意力机制的遥感图像目标检测算法[D]. 西安科技大学, 2022.

[230] 赵宇晗. 基于***残差收缩***的多状态下调节阀状态监控研究[D]. 哈尔滨工程大学, 2022.

[231] Wang L, Zou T, Cai K, et al. Rolling bearing fault diagnosis method based on improved ***residual shrinkage network***[J]. Journal of the Brazilian Society of Mechanical Sciences and Engineering, 2024, 46(3): 1-12.

[232] Li T, Wu X, Luo Z, et al. A Baring Fault Diagnosis Method under Small Sample Conditions Based on the Fractional Order Siamese ***Deep Residual Shrinkage Network***[J]. Fractal and Fractional, 2024, 8(3): 134.

[233] Li S, Qin L, Zhao D, et al. Indoor positioning system for single LED light based on ***deep residual shrinkage network***[J]. Optics Communications, 2024: 130366.

[234] 高振国, 曹雯琪. 结合***残差收缩模块***的多传感器数据轴承故障诊断方法[P]. 福建省: CN117333715A, 2024-01-02.

[235] 郭棉, 曾繁成, 柳秀山等. 一种基于***残差收缩网络***的人体活动识别方法[P]. 广东省: CN117523672A, 2024-02-06.

[236] Zhu, X, Zhang, J, Wang, X, et al. Improved ***deep residual shrinkage network*** for a multi-cylinder heavy-duty engine fault detection with single channel surface vibration[J]. Energy and AI, 2024, 100356.

[237] 全睿, 刘品, 张键等. 基于***RSN***-GRU融合网络的锂电池荷电状态估计[J/OL]. 华中科技大学学报(自然科学版): 1-7 [2024-03-14].

[238] 黄湛钧, 董鑫, 卢沐宇等. 基于***DRSN***与电压幅值分析的航空HVDC系统逆变器故障诊断[J]. 航空学报, 2024, 45(03): 216-227.

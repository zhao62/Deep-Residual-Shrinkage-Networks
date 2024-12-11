# Deep-Residual-Shrinkage-Networks

The deep residual shrinkage network is a variant of deep residual networks (ResNets), and aims to improve the feature learning ability from highly noise signals or complex backgrounds. Although the method is originally developed for vibration-based fault diagnosis, it can be applied to image recognition and speech recognition as well. The major innovation is the integration of soft thresholding as nonlinear transformation layers into ResNets. Moreover, the thresholds are automatically determined by a specially designed sub-network, so that no professional expertise on threshold determination is required.

![The basic idea of deep residual shrinkage networks](https://github.com/zhao62/Deep-Residual-Shrinkage-Networks/blob/master/Basic-idea-of-DRSN.png)

The method is implemented using TensorFlow 1.0.1, TFLearn 0.3.2, and Keras 2.2.1, and applied for image classification. A small network with 3 residual shrinkage blocks is constructed in the code. More blocks and more training iterations can be used for a higher performance.

## Abstract:
This paper develops new deep learning methods, namely, deep residual shrinkage networks, to improve the feature learning ability from highly noised vibration signals and achieve a high fault diagnosing accuracy. Soft thresholding is inserted as nonlinear transformation layers into the deep architectures to eliminate unimportant features. Moreover, considering that it is generally challenging to set proper values for the thresholds, the developed deep residual shrinkage networks integrate a few specialized neural networks as trainable modules to automatically determine the thresholds, so that professional expertise on signal processing is not required. The efficacy of the developed methods is validated through experiments with various types of noise.

## Reference:

***Minghang Zhao, Shisheng Zhong, Xuyun Fu, Baoping Tang, Michael Pecht, Deep residual shrinkage networks for fault diagnosis, 
IEEE Transactions on Industrial Informatics, 2020, 16(7): 4681-4690.***

***The paper has been cited over 1000 times on Google Scholar.***

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

[1] Li Y, Chen H. Image recognition based on **deep residual shrinkage Network**[C]//2021 International Conference on Artificial Intelligence and Electromechanical Automation (AIEA). IEEE, 2021: 334-337.

[2] Yu Y, Guo L, Gao H, et al. Pareto-optimal adaptive loss **residual shrinkage network** for imbalanced fault diagnostics of machines[J]. IEEE Transactions on Industrial Informatics, 2021, 18(4): 2233-2243.

[3] Hu H, Ma X, Shang Y. A novel method for transformer fault diagnosis based on refined **deep residual shrinkage network**[J]. IET Electric Power Applications, 2022, 16(2): 206-223.

[4] Yao G, Chen Y, Liu Y, et al. Robust photon-efficient imaging using a pixel-wise **residual shrinkage network**[J]. Optics Express, 2022, 30(11): 18856-18873.

[5] Cao X, Xu X, Duan Y, et al. Health status recognition of rotating machinery based on **deep residual shrinkage network** under time-varying conditions[J]. IEEE Sensors Journal, 2022, 22(19): 18332-18348.

[6] Yang P, Geng H, Wen C, et al. An intelligent quadrotor fault diagnosis method based on novel **deep residual shrinkage network**[J]. Drones, 2021, 5(4): 133.

[7] Yang J, Gao T, Jiang S, et al. Fault diagnosis of rotating machinery based on one-dimensional **deep residual shrinkage network** with a wide convolution layer[J]. Shock and Vibration, 2020, 2020: 1-12.

[8] He Z, Yuan S, Zhao J, et al. A robust myocardial infarction localization system based on multi-branch **residual shrinkage network** and active learning with clustering[J]. Biomedical Signal Processing and Control, 2023, 80: 104238.

[9] Han T, Zhang Z, Ren M, et al. Speech Emotion Recognition Based on **Deep Residual Shrinkage Network**[J]. Electronics, 2023, 12(11): 2512.

[10] Zhang Q, Zhai H, Ma Y, et al. Enhanced-**Deep-Residual-Shrinkage-Network**-Based Voiceprint Recognition in the Electric Industry[J]. Electronics, 2023, 12(14): 3017.

[11] Qin Y, Liu X, Zhang F, et al. Improved **deep residual shrinkage network** on near infrared spectroscopy for tobacco qualitative analysis[J]. Infrared Physics & Technology, 2023, 129: 104575.

[12] Tong Y, Wu P, He J, et al. Bearing fault diagnosis by combining a **deep residual shrinkage network** and bidirectional LSTM[J]. Measurement Science and Technology, 2021, 33(3): 034001.

[13] Sun F, Xu H, Zhao Y, et al. Data-driven fault diagnosis of control valve with missing data based on modeling and **deep residual shrinkage network**[J]. Journal of Zhejiang University-SCIENCE A, 2022, 23(4): 303-313.

[14] Pei X, Dong S, Tang B, et al. Bearing running state recognition method based on feature-to-noise energy ratio and improved **deep residual shrinkage network**[J]. IEEE/ASME Transactions on Mechatronics, 2021, 27(5): 3660-3671.

[15] Zhang S, Pan J, Han Z, et al. Recognition of noisy radar emitter signals using a one-dimensional **deep residual shrinkage network**[J]. Sensors, 2021, 21(23): 7973.

[16] Liu X, He Y, Wang L. Adaptive transfer learning based on a two-stream densely connected **residual shrinkage network** for transformer fault diagnosis over vibration signals[J]. Electronics, 2021, 10(17): 2130.

[17] Zhang Z, Peng G, Tan Y, et al. THz wave detection of gap defects based on convolutional neural network improved by **residual shrinkage network**[J]. CSEE Journal of Power and Energy Systems, 2020.

[18] Shi D, Wu Z, Zhang L, et al. Multi-Scale **Deep Residual Shrinkage Network** for Atrial Fibrillation Recognition[J]. International Journal of Computational Intelligence and Applications, 2022, 21(03): 2250015.

[19] Zuo G, Ren Z, Xiao X, et al. Magnetotelluric Noise Attenuation Using a **Deep Residual Shrinkage Network**[J]. Minerals, 2022, 12(9): 1086.

[20] Sun R, Jiang Z, Su J. A **deep residual shrinkage neural network**-based deep reinforcement learning strategy in financial portfolio management[C]//2021 IEEE 6th International Conference on Big Data Analytics (ICBDA). IEEE, 2021: 76-86.

[21] Wang J, Song Y, Mao Z, et al. EEG-Based Emotion Identification Using 1-D **Deep Residual Shrinkage Network** With Microstate Features[J]. IEEE Sensors Journal, 2023, 23(5): 5165-5174.

[22] Li B, Cui F. Inception module and **deep residual shrinkage network**-based arc fault detection method for pantograph–catenary systems[J]. Journal of Power Electronics, 2022, 22(6): 991-1000.

[23] Wu X, Zhou Y, Wu D, et al. Improved **Deep Residual Shrinkage Network** for Intelligent Interference Recognition with Unknown Interference[J]. Sensors, 2023, 23(18): 7909.

[24] Xu Z, Ma Y, Pan Z, et al. Deep Spiking **Residual Shrinkage Network** for Bearing Fault Diagnosis[J]. IEEE Transactions on Cybernetics, 2022.

[25] Shi M, Huang Z, Xiao G, et al. Estimating the Depth of Anesthesia from EEG Signals Based on a **Deep Residual Shrinkage Network**[J]. Sensors, 2023, 23(2): 1008.

[26] Liang X, Hu F, Li X, et al. Spatio-Temporal Wind Speed Prediction Based on Improved **Residual Shrinkage Network**[J]. Sustainability, 2023, 15(7): 5871.

[27] Wang H, Wang J, Xu H, et al. DRSNFuse: **Deep Residual Shrinkage Network** for Infrared and Visible Image Fusion[J]. Sensors, 2022, 22(14): 5149.

[28] Yu X, Ren J, Cui Y, et al. DRSN4mCPred: accurately predicting sites of DNA N4-methylcytosine using **deep residual shrinkage network** for diagnosis and treatment of gastrointestinal cancer in the precision medicine era[J]. Frontiers in Medicine, 2023, 10: 1187430.

[29] Zheng G, Zhang Q, Li S. Failure diagnosis of linear arrays based on **deep residual shrinkage network**[J]. Microwave and Optical Technology Letters, 2022, 64(9): 1627-1633.

[30] Zheng G, Zhang Q, Li S. Failure diagnosis of linear arrays based on **deep residual shrinkage network**[J]. Microwave and Optical Technology Letters, 2022, 64(9): 1627-1633.

[31] Yue P, Xu P, Fang F, et al. Noise resistant steam generator water level reconstruction for nuclear power plant based on **deep residual shrinkage network**[J]. Annals of Nuclear Energy, 2023, 193: 110038.

[32] Cheng L, He C. Fish Recognition Based on **Deep Residual Shrinkage Network**[C]//2021 4th International Conference on Robotics, Control and Automation Engineering (RCAE). IEEE, 2021: 36-39.

[33] Zhang Z, Zhang C, Chen L, et al. LGMA-DRSN: a lightweight convex global multi-attention **deep residual shrinkage network** for fault diagnosis[J]. Measurement Science and Technology, 2023, 34(11): 115011.

[34] Lin N, Chen G, Zhou Q, et al. Dilated **residual shrinkage network** for SAR image despeckling[C]//2021 IEEE 6th International Conference on Signal and Image Processing (ICSIP). IEEE, 2021: 503-507.

[35] Ruan F, Dang L, Ge Q, et al. Dual-Path **Residual “Shrinkage” Network** for Side-Scan Sonar Image Classification[J]. Computational intelligence and neuroscience, 2022, 2022.

[36] Lu Y, Lin L, Zhang X, et al. New method for rice disease identification based on improved **deep residual shrinkage network**[J]. Systems Science & Control Engineering, 2023, 11(1): 2177770.

[37] Xuejiao P, Shaojiang D, Xuewu P, et al. A method for rolling bearing life state recognition by combining health indicator and anti-noise **deep residual shrinkage network**[J]. Journal of the Brazilian Society of Mechanical Sciences and Engineering, 2023, 45(1): 37.

[38] Guo W, Xu G, Wang Y. Brain visual image signal classification via hybrid dilation **residual shrinkage network** with spatio-temporal feature fusion[J]. Signal, Image and Video Processing, 2023, 17(3): 743-751.

[39] Yang Z, Wu B, Wang Z, et al. Image Recognition Based on an Improved **Deep Residual Shrinkage Network**[J]. Available at SSRN 4013383, 2022.

[40] Li X. Bearing fault diagnosis method of wind turbine based on improved antinoise **residual shrinkage network**[J]. Energy Eng, 2022, 119(2): 665-680.

[41] Wen X, Cao C, Sun Y, et al. RF Transmitter Identification and Classification Based on **Deep Residual Shrinkage Network**[C]//2021 IEEE 23rd Int Conf on High Performance Computing & Communications; IEEE, 2021: 327-335.

[42] Li W, Lin K, Hou Y, et al. Multi-Omics Data Integration Patient Classification Method Based on Deep Dense **Residual Shrinkage Network**[C]//2022 IEEE 34th International Conference on Tools with Artificial Intelligence (ICTAI). IEEE, 2022: 1098-1104.

[43] Wu X, Lu Y, Tang Z, et al. Communication Interference Recognition Based on Improved **Deep Residual Shrinkage Network**[C]//2023 IEEE Symposium on Computers and Communications (ISCC). IEEE, 2023: 804-809.

[44] Zhao W, Hu S. End-to-End Auto-Encoder System for **Deep Residual Shrinkage Network** for AWGN Channels[J]. Journal of Computer and Communications, 2023, 11(5): 161-176.

[45] Liu G, Chen Y, Zhang X, et al. A **deep residual shrinkage network** based on multi-scale attention module for subsea Christmas tree valve leakage detection[J]. Measurement, 2022, 198: 110970.

[46] Ma Y, Bai Z, He B, et al. Enhanced **Deep Residual Shrinkage Network** Based Channel Estimation in RIS Communication System[C]//2023 25th International Conference on Advanced Communication Technology (ICACT). IEEE, 2023: 18-22.

[47] Shi B, Zhang Q, Li Y, et al. SAR image target recognition algorithm based on improved **residual shrinkage network**[C]//2021 2nd International Seminar on Artificial Intelligence, Networking and Information Technology (AINIT). IEEE, 2021: 84-87.

[48] Cheng Q, Wu Z, Min J. Foggy Weather Monitoring Method Based on Improved **Deep Residual Shrinkage Network** and Radio Signal[C]//2022 3rd International Conference on Geology, Mapping and Remote Sensing (ICGMRS). IEEE, 2022: 495-499.

[49] Zhou Y, Yuan X, Cui X, et al. Fault diagnosis based on **deep residual shrinkage network** and maximum mean discrepancy[C]//2021 China Automation Congress (CAC). IEEE, 2021: 2340-2345.

[50] Liu J, Zhou Q, Zhang B. **Deep Residual Shrinkage Network** for Few-Shot Learning[C]//2021 3rd International Conference on Intelligent Control, Measurement and Signal Processing and Intelligent Oil Field (ICMSP). IEEE, 2021: 120-124.

[51] Li Y, Cao C, Zhang H, et al. Feature extraction and identification of specific radiation sources based on axial integral bispectrum and **deep residual shrinkage network**[C]//2022 International Conference on Networking and Network Applications (NaNA). IEEE, 2022: 13-18.

[52] Ma G, Zhuo J, Gao W, et al. **Deep Residual Shrinkage Network** With Time-Frequency Features For Bearing Fault Diagnosis[C]//2022 IEEE International Conference on Signal Processing, Communications and Computing (ICSPCC). IEEE, 2022: 1-6.

[53] Zhao H, Guo B. EEG Signal Denoising Based on **Deep Residual Shrinkage Network**[C]//Journal of Physics: Conference Series. IOP Publishing, 2022, 2395(1): 012076.

[54] Huang L, Gong Q. Hearing screening based on **deep residual shrinkage network**[C]//Journal of Physics: Conference Series. IOP Publishing, 2022, 2347(1): 012006.

[55] Song Z, Cheng W, Li J, et al. A specific emitter identification method based on full bispectrum and **deep residual shrinkage network**[C]//Thirteenth International Conference on Digital Image Processing (ICDIP 2021). SPIE, 2021, 11878: 620-629.

[56] Bai X, Ma Z, Meng G. Bearing Fault Diagnosis Based on Wavelet Transform and **Residual Shrinkage Network**[C]//2022 International Conference on Computer Network, Electronic and Automation (ICCNEA). IEEE, 2022: 373-378.

[57] Lin J, Wen Z, Qiu Z. Multi-scale Feature Fusion **Residual Shrinkage Network** for COVID-19 Diagnosis[C]//2022 IEEE Smartworld, Ubiquitous Intelligence & Computing, Scalable Computing & Communications, Digital Twin, Privacy Computing, Metaverse, Autonomous & Trusted Vehicles. IEEE, 2022: 310-317.

[58] Tao H E, Jian C, Ying-you W E N. HEp-2 image recognition based on **deep residual shrinkage network**[J]. Computer and Modernization, 2021 (01): 38.

[59] Wang Y, Luo S, Luo R, et al. Fault Diagnosis of Gearbox Based on **Deep Residual Shrinkage Network** in Noise Environment[C]//2022 Global Reliability and Prognostics and Health Management (PHM-Yantai). IEEE, 2022: 1-5.

[60] Lin Z. Vehicle logo recognition based on depth **residual shrinkage network**[C]//Third International Conference on Artificial Intelligence and Computer Engineering (ICAICE 2022). SPIE, 2023, 12610: 749-753.

[61] Wei Q, Song Z, Zhao J. A network combining **deep residual shrinkage block** for infrared and visible image fusion[C]//Conference on Infrared, Millimeter, Terahertz Waves and Applications (IMT2022). SPIE, 2023, 12565: 776-785.

[62] Guo Y, Yan J. A CSI Based Localization and Identification Recognition Algorithm Using Multi-task Learning and **Deep Residual Shrinkage Network**[C]//2022 IEEE 22nd International Conference on Communication Technology (ICCT). IEEE, 2022: 1770-1776.

[63] Xu L, Zhai J, Lin P, et al. Detection of malicious applications based on improved deep **residual shrinkage network**[J]. Nanjing Xinxi Gongcheng Daxue Xuebao, 2022, 14(3): 368-378.

[64] Liang H, Xie H, Huang H, et al. Distributed Optical Fiber Sensing Signal Recognition Based on **Deep Residual Shrinkage Network**[C]//2022 5th World Conference on Mechanical Engineering and Intelligent Manufacturing (WCMEIM). IEEE, 2022: 882-886.

[65] LI Y, HUANG T, XUN C D, et al. Single Image Super-Resolution Method Based on **Residual Shrinkage Network** in Real Complex Scenes[J]. Journal of Computer Applications, 2023: 0.

[66] YUAN Q, XUE S. Relation extraction algorithm based on **residual shrinkage network**[J]. Journal of Computer Applications, 2022, 42(10): 3040.

[67] Wang J, Xue L, Gao X. Identification method of volcanic rock slices based on a **deep residual shrinkage network**[C]//Fourth International Conference on Geoscience and Remote Sensing Mapping (GRSM 2022). SPIE, 2023, 12551: 389-394.

[68] Wang C, He T, Liu J, et al. A HEp-2 Cell Image Classification Model Based on **Deep Residual Shrinkage Network** Combined with Dilated Convolution[C]//International Conference on Intelligent Information Processing. Cham: Springer International Publishing, 2022: 409-418.

[69] Gu Z, Liu T, Song Y. Prediction of fracture index in tight reservoir based on depth **residual shrinkage network**[R]. Copernicus Meetings, 2023.

[70] Zhang Z, Chen L, Zhang C, et al. GMA-DRSNs: a novel fault diagnosis method with global multi-attention **deep residual shrinkage networks**[J]. Measurement, 2022, 196: 111203.

[71] Tong J, Tang S, Wu Y, et al. A fault diagnosis method of rolling bearing based on improved **deep residual shrinkage networks**[J]. Measurement, 2023, 206: 112282.

[72] Cui F, Tu Y, Gao W. A Photovoltaic System Fault Identification Method Based on Improved **Deep Residual Shrinkage Networks**[J]. Energies, 2022, 15(11): 3961.

[73] Tang P, Xu Y, Wei G, et al. Specific emitter identification for IoT devices based on **deep residual shrinkage networks**[J]. China Communications, 2021, 18(12): 81-93.

[74] Zhang Z, Li H, Chen L, et al. Rolling bearing fault diagnosis using improved **deep residual shrinkage networks**[J]. Shock and Vibration, 2021, 2021: 1-11.

[75] Chen W, Sun K, Li X, et al. Adaptive multi-channel **residual shrinkage networks** for the diagnosis of multi-fault gearbox[J]. Applied Sciences, 2023, 13(3): 1714.

[76] Zhu L, Qian K, Wang Z, et al. Heart sound classification based on **residual shrinkage networks**[C]//2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE, 2022: 4469-4472.

[77] Yang X, Chi F, Shao S, et al. Bearing fault diagnosis under variable working conditions based on **deep residual shrinkage networks** and transfer learning[J]. Journal of Sensors, 2021, 2021: 1-13.

[78] Zhang Z, Li H, Chen L. **Deep residual shrinkage networks** with self-adaptive slope thresholding for fault diagnosis[C]//2021 7th International Conference on Condition Monitoring of Machinery in Non-Stationary Operations (CMMNO). IEEE, 2021: 236-239.

[79] Salimy A, Mitiche I, Boreham P, et al. Dynamic noise reduction with **deep residual shrinkage networks** for online fault classification[J]. Sensors, 2022, 22(2): 515.

[80] Xu J, Gao S, Dang X, et al. BO-MADRSN: Bayesian optimized multi-attention **residual shrinkage networks** for industrial soft sensor modeling[J]. Measurement, 2023: 113477.

[81] Yan C Q, Sun Y C, Zhang X, et al. A methodology to detect pilot perception of warning information by eye movement data and **deep residual shrinkage networks**[J]. The Aeronautical Journal, 2023: 1-15.

[82] Zhang Z, Zhang C, Li H. Highly Imbalanced Fault Diagnosis of Rolling Bearings based on Variational Mode Gaussian Distortion and **Deep Residual Shrinkage Networks**[J]. IEEE Transactions on Instrumentation and Measurement, 2023.

[83] Tiantian G, Xiaoyong Z, Lei W, et al. Research on Multi-dimensional Time Series Anomaly Detection Method Based on Temporal **Deep Residual Shrinkage Networks**[C]//2021 IEEE 5th Information Technology, Networking, Electronic and Automation Control Conference (ITNEC). IEEE, 2021, 5: 1673-1677.

[84] Salimy A, Mitiche I, Boreham P, et al. Robust **Deep Residual Shrinkage Networks** for Online Fault Classification[C]//2021 29th European Signal Processing Conference (EUSIPCO). IEEE, 2021: 1691-1695.

[85] Sun K, Ren Q, Jin H, et al. Deep Spatio-Temporal **Residual Shrinkage Networks** for Traffic Prediction[C]//2022 IEEE 24th Int Conf on High Performance Computing & Communications. IEEE, 2022: 1036-1041.

[86] Cheng M, Gao Q, Bai Z, et al. Research on Hearing-Impaired EEG Emotion Recognition Based on **Deep Residual Shrinkage Networks**[C]//2023 42nd Chinese Control Conference (CCC). IEEE, 2023: 8677-8682.

[87] Chunxing Y, Quan L, Kun C, et al. **Deep Residual Shrinkage Networks** for Adaptive Classification of EEG Error-Related Potentials[C]//2022 28th International Conference on Mechatronics and Machine Vision in Practice (M2VIP). IEEE, 2022: 1-6.

[88] Ma Y, Wang C, Jiang C, et al. **Deep Residual Shrinkage Networks** for EMG-based Gesture Identification[J]. arXiv preprint arXiv:2202.02984, 2022.

[89] CHI F, YANG X, SHAO S, et al. Bearing fault diagnosis under variable working conditions based on **deep residual shrinkage networks**[J]. Computer Integrated Manufacturing System, 2023, 29(4): 1146.

[90] 刘徐洲, 李孝忠. 基于**深度残差收缩网络**和迁移学习的变工况轴承故障诊断[J]. 天津科技大学学报, 2023, 38(04): 76-80.

[91] 龚玉晓, 高淑萍. 基于改进**深度残差收缩网络**的心电信号分类算法[J]. 应用数学和力学, 2023, 44(08): 977-988.

[92] 卞文彬, 邓艾东, 刘东川, 赵敏, 刘洋, 李晶. 基于改进**深度残差收缩网络**的风电机组滚动轴承故障诊断方法[J]. 机械工程学报, 2023, 59(12): 202-214.

[93] 李颖, 黄超, 孙成栋, 徐勇. 真实复杂场景下基于**残差收缩网络**的单幅图像超分辨率方法[J]. 计算机应用, 2023, 43(12): 3903-3910.

[94] 麻建新, 袁春华, 李翔宇. 针对油井长时程基于**深度残差收缩网络**的模型故障诊断[J]. 科技资讯, 2023, 21(14): 116-119.

[95] 梁惠康, 谢浩燊, 黄红斌, 刘伟平. 基于改进**深度残差收缩网络**的DAS信号识别[J]. 激光与光电子学进展: 1-13.

[96] 林立媛. 基于**深度残差收缩网络**的水稻病害识别方法研究[D]. 黑龙江八一农垦大学, 2023.

[97] 高学金, 李虎, 韩华云, 齐咏生. 基于域自适应**残差收缩网络**的滚动轴承故障诊断[J]. 组合机床与自动化加工技术, 2023,(05): 164-168+173.

[98] 杨正理, 吴馥云, 陈海霞. **深度残差收缩网络**的多特征锅炉炉管声波信号故障识别[J]. 智能系统学报: 1-10.

[99] 刘汉举. 一种基于机器视觉和**深度残差收缩网络**的智能制造缺陷检测方法[J]. 中国科技论文, 2023, 18(04): 462-468.

[100] 陈姮, 陈志翔, 申高宁, 王舒琪. 基于**深度残差收缩网络**的恶意代码分类[J]. 闽南师范大学学报(自然科学版), 2023, 36(01): 50-58.

[101] 曹珂璐. 基于**深度残差收缩网络**的风力发电机齿轮箱故障诊断方法研究[D]. 陕西科技大学, 2023.

[102] 庄全胜. 基于**深度残差收缩网络**的自然情境下的多模态情感识别研究[D]. 哈尔滨理工大学, 2023.

[103] 高云鹏, 孟雪晴, 张其旺, 王庆凯, 杨佳伟, 董一隆. 基于深度宽卷积**残差收缩网络**的球磨机负荷状态诊断[J]. 湖南大学学报(自然科学版), 2023, 50(02): 102-111.

[104] 曹珂璐, 任工昌, 桓源, 张路平. 基于**深度残差收缩网络**的风力发电机齿轮箱故障诊断[J]. 机械与电子, 2023, 41(02): 66-70+75.

[105] 魏煦航, 曹少中, 杨彦红, 项璇. 基于**深度残差收缩网络**的滚动轴承健康因子构建方法[J]. 印刷与数字媒体技术研究, 2023,(01): 71-79.

[106] 王玉, 张燕红, 周昱洲, 林鸿斌. 基于**深度残差收缩网络**的校园垃圾图像分类[J]. 吉林大学学报(信息科学版), 2023, 41(01): 186-192.

[107] 翁敏超, 王海瑞, 朱贵富. 小波变换和**深度残差收缩网络**在齿轮箱故障诊断中的应用[J]. 机械科学与技术: 1-7.

[108] 吴萌, 高怡宁, 王佳. 结合特征聚类和**深度残差收缩网络**的壁画风格迁移[J]. 激光与光电子学进展: 1-17.

[109] 樊庆玲, 杨宏波, 郭涛, 张伟, 王威廉. FrFT-Bark域特征提取与CNN**残差收缩网络**心音分类算法[J]. 云南大学学报(自然科学版), 2023, 45(03): 564-574.

[110] 杨正理, 吴馥云, 陈海霞. 基于改进**深度残差收缩网络**的旋转机械故障诊断[J]. 机电工程, 2023, 40(03): 344-352.

[111] 戴江涛, 申静. 基于双流**残差收缩网络**的人体动作识别方法[J]. 信息技术与信息化, 2022, (10): 106-110.

[112] 田钦文, 冯辅周, 李鸣, 陈晓明, 朱俊臻, 胡浩, 宋超. 基于一维**深度残差收缩网络**的汇流行星排齿轮裂纹故障诊断[J]. 振动与冲击, 2022, 41(19): 198-206.

[113] 彭涛, 伦功仁, 赵峰. 基于**深度残差收缩网络**的船用补水泵滚动轴承故障诊断[J]. 风机技术, 2022, 64(S1): 37-42.

[114] 胡从强, 曲娜, 张帅, 冮震. 连续小波变换和具有注意力机制的**深度残差收缩网络**在低压串联电弧故障检测中的应用[J]. 电网技术, 2023, 47(05): 1897-1905.

[115] 赵莹莹, 何怡刚, 邢致恺, 杜博伦. 基于信息融合与**深度残差收缩网络**的DAB变换器开路故障诊断方法[J]. 电力自动化设备, 2023, 43(02): 112-118.

[116] 王彦博, 吴俊勇, 季佳伸, 李栌苏, 李宝琴. 基于**深度残差收缩网络**的电力系统暂态频率安全集成评估[J]. 电网技术, 2023, 47(02): 482-494.

[117] 吴爱华, 彭金喜. 基于**深度残差收缩网络**的信号调制类型识别[J]. 电子信息对抗技术, 2022, 37(04): 24-30.

[118] 梁日强, 胡燕林, 蒋占四. 基于改进的**残差收缩网络**的带钢表面缺陷识别[J]. 组合机床与自动化加工技术, 2022, (06): 82-85.

[119] 殷磊. 基于**残差收缩网络**的旋转机械故障诊断方法研究[D]. 哈尔滨工业大学, 2022.

[120] 黄莹. 基于**深度残差收缩网络**的心律失常分类算法研究[D]. 广西大学, 2022.

[121] 张晓东. 基于**深度残差收缩网络**滚动轴承故障识别研究[D]. 沈阳工业大学, 2022.

[122] 张晓锋. 基于多尺度特征融合与**残差收缩网络**的齿轮箱故障诊断研究[D]. 石家庄铁道大学, 2022.

[123] 梁日强. 基于**残差收缩网络**的带钢表面缺陷识别方法研究[D]. 桂林电子科技大学, 2022.

[124] 谈诚, 卢德龙, 张丹青. 基于双层**深度残差收缩网络**的台区窃电用户识别方法[J]. 电力大数据, 2022, 25(05): 1-9.

[125] 李雪松, 李劲华, 吕智涵. 基于改进**深度残差收缩网络**的轴承故障诊断[J]. 青岛大学学报(自然科学版), 2022, 35(02): 38-43+50.

[126] 李瑞航, 吴红兰, 孙有朝, 吴华聪. 基于**深度残差收缩网络**多特征融合语音情感识别[J]. 数据采集与处理, 2022, 37(03): 542-554.

[127] 唐震, 乔晓强, 张涛, 苏健, 杨小蒙. 基于**深度残差收缩网络**的辐射源个体识别方法[J]. 电子测量技术, 2022, 45(09): 168-174.

[128] 张翔, 孙宪坤, 胡峻, 尹京苑, 熊玉洁. 结合数据扩增与**残差收缩网络**的地震短临预测[J]. 地震, 2022, 42(02): 74-88.

[129] 李晓峰, 向辉, 杨青桦. 噪声干扰下基于二维特征图和**深度残差收缩网络**的齿轮箱故障诊断[J]. 机床与液压, 2022, 50(07): 187-191.

[130] 刘晓锋, 高丽梅. 基于改进空间**残差收缩网络**模型的农作物病虫害识别[J]. 山东农业大学学报(自然科学版), 2022, 53(02): 259-264.

[131] 袁思邈. 基于宽广**残差收缩网络**的图像分类研究[D]. 山东理工大学, 2022.

[132] 孙丰, 徐贺, 赵宇晗, 张渝东. 数据驱动的基于数学模型插补和改进**深度残差收缩网络**的调节阀状态监控（英文）[J]. Journal of Zhejiang University-Science A(Applied Physics & Engineering), 2022, 23(04): 303-314.

[133] 王之卓, 吕健鸿, 王中鹏. 基于**深度残差收缩网络**的LDPC译码算法[J]. 浙江科技学院学报, 2022, 34(01): 35-41.

[134] 车思韬, 郭荣佐, 李卓阳, 杨军. 注意力机制结合**残差收缩网络**对遥感图像分类[J]. 计算机应用研究, 2022, 39(08): 2532-2537.

[135] 陈玲玲, 毕晓君. 基于**残差收缩网络**的睡眠脑电分期[J]. 仪器仪表学报, 2022, 43(02): 148-155.

[136] 马鑫, 尚毅梓, 胡昊, 徐杨. 基于数据特征增强和**残差收缩网络**的变压器故障识别方法[J]. 电力系统自动化, 2022, 46(03): 175-183.

[137] 孟庆旭, 沈功田, 俞跃, 胡斌, 王宝轩, 李志农. **深度残差收缩网络**的含噪微泄漏超声识别方法[J]. 应用声学, 2022, 41(06): 964-972.

[138] 袁泉, 薛书鑫. 基于**残差收缩网络**的关系抽取算法[J]. 计算机应用, 2022, 42(10): 3040-3045.

[139] 许历隆, 翟江涛, 林鹏, 崔永富. 一种基于改进**深度残差收缩网络**的恶意应用检测方法[J]. 南京信息工程大学学报(自然科学版), 2022, 14(03): 368-378.

[140] 高晔, 郭松宜, 厍向阳. 基于**残差收缩网络**的遥感图像目标检测算法[J]. 计算机工程与应用, 2022, 58(17): 93-100.

[141] 柯翔, 包乾宗, 赵全波. 基于**深度残差收缩网络**的波阻抗反演建模[A]. 中国地球物理学会, 2021: 230-231.

[142] 张力, 常俊, 武浩, 黄彬, 刘欢. **深度残差收缩网络**下的定位与行为联合识别[J]. 计算机工程与应用, 2022, 58(21): 205-212.

[143] 李昊璇, 闫新艳. 基于**深度残差收缩网络**的商品图像识别[J]. 测试技术学报, 2021, 35(04): 294-299+322.

[144] 卢锦玲, 郭鲁豫. 基于改进**深度残差收缩网络**的电力系统暂态稳定评估[J]. 电工技术学报, 2021, 36(11): 2233-2244.

[145] 宋子豪, 程伟, 彭岑昕, 李晓柏. 基于CWD和**残差收缩网络**的调制方式识别方法[J]. 系统工程与电子技术, 2021, 43(11): 3371-3379.

[146] 何涛, 陈剑, 闻英友. 基于**深度残差收缩网络**的HEp-2图像识别[J]. 计算机与现代化, 2021, (01): 38-42.

[147] 杨偲乐. 基于混合域注意力机制的卷积网络和**残差收缩网络**的轴承故障诊断[D]. 北京邮电大学, 2020.

[148] 李天慧, 谢云澄, 车荣花, 梁迪昌, 王健. 基于**DRSN**-BiLSTM的电力信息网络入侵检测模型[J]. 电力信息与通信技术, 2023, 21(09): 30-37.

[149] 刘高辉, 宋博武. **DRSN**与集成融合的OFDM辐射源个体识别方法[J]. 信号处理: 1-14.

[150] 黄湛钧, 董鑫, 卢沐宇, 张瑞涛, 闫钊阳, 张安. 基于**DRSN**与电压幅值分析的航空HVDC系统中逆变器故障诊断[J]. 航空学报: 1-9.

[151] 王小聪, 郝正航, 陈卓. 基于**DRSN**-CW-LSTM网络的锂电池荷电状态预测[J]. 南方电网技术: 1-9.

[152] 赵光宏. 基于Conformer-**DRSN**的新冠肺炎CT图像检测系统的研究与实现[D].辽宁大学, 2023.

[153] 王磊, 孙志成, 王磊, 陈端兵, 蒋家玮. 基于**DRSN**-CW和LSTM的轴承故障诊断[J]. 电子科技大学学报, 2022, 51(06): 921-927.

[154] 文井辉, 伍荣森, 李帅永, 韩明秀. 基于**DRSN**和优化BiLSTM的轴承剩余寿命预测方法[J]. 计算机集成制造系统: 1-18.

[155] 吴卫堃, 宫士营, 郑耀华, 单超, 董传友. 基于**DRSN**的高噪声环境下XLPE电缆故障识别[J]. 电气传动, 2022, 52(16): 75-80.

[156] 毛浩英, 孙有朝, 李龙彪, 晏传奇. 基于改进**DRSN**的航空发动机故障风险预警模型[J]. 航空动力学报: 1-12.

[157] 胡昊, 马鑫, 徐杨, 任玉峰. 基于权重修正和**DRSN**-LSTM模型的向家坝下游水位多时间尺度预测[J]. 水利水电技术(中英文), 2022, 53(07): 46-57.

[158] 赵杰, 陈志刚, 赵志川, 张楠. 基于同步提取变换和**DRSN**的滚动轴承故障诊断研究[J]. 重庆理工大学学报(自然科学), 2021, 35(01): 138-144.

[159] 朱容波, 王晗铭, 李松泉. 基于纹理-颜色多尺度**残差收缩网络**的玉米病害识别方法[P]. 湖北省：CN116630960A, 2023-08-22.

[160] 赵振喜, 宋京哲, 倪凤祥等. 一种基于**残差收缩网络**和长短期记忆网络的变电站设备寿命预测方法[P]. 吉林省：CN116595853A, 2023-08-15.

[161] 孙逸潇, 赵治栋, 张显飞等. 一种基于改进**残差收缩网络**的身份识别方法[P]. 浙江省：CN116305048A, 2023-06-23.

[162] 顾军华, 邢佳豪, 张亚娟等. 基于多尺度**残差收缩网络**的多普勒雷达心跳检测方法[P]. 天津市：CN115969388A, 2023-04-18.

[163] 白智全, 马媛媛, 贺邦玮等. 基于改进**残差收缩网络**的RIS通信系统信道估计方法[P]. 山东省：CN115833974A, 2023-03-21.

[164] 陈阳, 杨燕琳, 王朝阳等. 一种基于改进**深度残差收缩网络**的二手车价格预测方法[P]. 青海省：CN115618727A, 2023-01-17.

[165] 苏依拉, 张旋, 仁庆道尔吉等. 一种基于**深度残差收缩网络**和seq2seq的蒙汉机器翻译方法[P]. 内蒙古自治区：CN115577720A, 2023-01-06.

[166] 杨涛, 徐琳. 基于多通道**深度残差收缩网络**的冰雹天气识别与分类方法[P]. 江苏省：CN114755745B, 2022-12-20.

[167] 徐慧, 吴一凡, 王皓晨等. 一种基于**深度残差收缩网络**的眼病诊断方法[P]. 江苏省：CN115456981A, 2022-12-09.

[168] 张玉梅, 库银涛, 吴晓军等. 基于**深层残差收缩网络**的隐函数文物三维模型重建方法[P]. 陕西省：CN115330944A, 2022-11-11.

[169] 蒋文波, 刘安顺, 李潘等. 基于**深度残差收缩网络**和生成对抗网络的去图像运动模糊方法[P]. 四川省：CN112734678B, 2022-11-08.

[170] 高世伟, 许金鹏, 党小超等. 一种基于贝叶斯优化的多注意力融合**深度残差收缩网络**软测量建模方法[P]. 甘肃省：CN115203954A, 2022-10-18.

[171] 王立辉, 张文鹏, 许宁徽. 基于改进**残差收缩网络**的FOCS故障诊断方法[P]. 江苏省：CN115130505A,2022-09-30.

[172] 李文耀, 林恺, 高建等. 一种基于**深度残差收缩网络**的多组学与表型关联预测方法[P]. 辽宁省：CN115132279A, 2022-09-30.

[173] 徐滌平, 宋伊晨, 周水清等. 基于**深度残差收缩网络**的集成灶风机故障诊断方法[P]. 浙江省：CN114897029A, 2022-08-12.

[174] 庄全胜, 吕鑫淼. 一种基于**深度残差收缩网络**的多模态情感识别方法[P]. 黑龙江省：CN114758676A, 2022-07-15.

[175] 严玉琮, 邵志刚. 一种基于**深度残差收缩网络**的犬鼻纹识别方法和模型[P]. 广东省：CN114511886A, 2022-05-17.

[176] 王正国, 王迪, 王新等. 一种多尺度元**深度残差收缩网络**的机械故障在线诊断方法[P]. 河南省：CN114492642A, 2022-05-13.

[177] 章坚武, 周晔. 一种基于**深度残差收缩网络**的语音欺骗检测方法[P]. 浙江省：CN114495950A, 2022-05-13.

[178] 邓艾东, 卞文彬, 刘洋等. 基于改进**深度残差收缩网络**的滚动轴承故障诊断方法[P]. 江苏省：CN114441173A, 2022-05-06.

[179] 任燕, 张瑞, 汤何胜等. 基于多模态**深度残差收缩网络**的液压防水阀故障诊断方法[P]. 浙江省：CN114358189A, 2022-04-15.

[180] 张涛, 唐震, 乔晓强等. 基于**深度残差收缩网络**的辐射源个体识别方法及装置[P]. 江苏省：CN114091545A, 2022-02-25.

[181] 覃程锦, 陶建峰, 刘成良等. 基于深度卷积**残差收缩网络**的刀具磨损预测方法和系统[P]. 上海市：CN114048958A, 2022-02-15.

[182] 胡斌, 沈功田, 孟庆旭等. 一种基于**深度残差收缩网络**含噪微泄漏识别方法[P]. 北京市：CN114036985A, 2022-02-11.

[183] 陈思哲, 杨欣, 曹云依等. 一种基于新型**深度残差收缩网络**的图像超分辨率重建方法[P]. 江苏省：CN113962857A, 2022-01-21.

[184] 蒋占四, 梁日强, 滕制等. 基于改进**残差收缩网络**的带钢缺陷检测方法[P]. 广西壮族自治区：CN113838208A, 2021-12-24.

[185] 刘凯, 柏建军, 张日东. 一种混合**深度残差收缩网络**与XGBoost算法的工业过程性能评估方法[P]. 浙江省：CN113705661A, 2021-11-26.

[186] 周冠华, 陈柳君, 苗昊雨等. 一种基于**深度残差收缩网络**的水深遥感反演方法[P]. 北京市：CN113639716A, 2021-11-12.

[187] 李智军, 光启宏, 李国欣. 一种基于**残差收缩网络**的设备诊断方法及系统[P]. 安徽省：CN113537382A, 2021-10-22.

[188] 吴彩萍, 申莲莲, 张蓉等. 基于**深度残差收缩网络**的车辆碰撞检测方法及装置[P]. 四川省：CN113177536B, 2021-09-10.

[189] 苏炯龙, 任晓天, 孙若宇等. 基于深度强化学习和**深度残差收缩网络**的投资方法及智能体[P]. 江苏省：CN112950374A, 2021-06-11.

[190] 王海凤, 王凯江, 白倩等. 基于注意力机制的**DRSN**和LSTM的网络入侵检测方法[P]. 内蒙古自治区：CN116684138A, 2023-09-01.

[191] 胡昊, 马鑫, 郑野等. 基于权重修正和**DRSN**-LSTM模型的水位预测方法[P]. 河南省：CN115099500B, 2023-04-18.

[192] 张淑慧, 兰田, 王连海等. 一种基于HOG和**DRSN**-LSTM的智能合约漏洞检测方法及系统[P]. 山东省：CN115937878A, 2023-04-07.

[193] 董亮, 胡思源, 张宇航等. 一种基于CEEMD-**DRSN**的离心泵空化状态识别方法[P]. 江苏省：CN115600126A, 2023-01-13.

[194] 卢德龙, 童充, 黄馨仪等. 一种基于**DRSN**的台区窃电用户识别方法、系统及装置[P]. 江苏省：CN115147135A, 2022-10-04.

[195] 李盛, 邱阳, 金亮等. 基于**DRSN**和person相关系数的道床故障预警方法[P]. 湖北省：CN113408441B, 2022-06-10.

[196] 缪小冬, 虞浒, 王华. 基于GAF-**DRSN**的滚动轴承故障诊断方法[P]. 江苏省：CN114595730A, 2022-06-07.

[197] 史宇杰. 一种基于**DRSN**的液基薄层细胞涂片数字病理图像检测方法[P]. 江苏省：CN114170198A, 2022-03-11.

[198] 文井辉, 李帅永, 韩明秀等. 基于**DRSN**和麻雀搜索优化BiLSTM的机械设备剩余寿命预测方法[P]. 重庆市：CN113723007A, 2021-11-30.

[199] 张夏林, 刘东涛, 翁正平等. 基于**残差收缩模块**与注意力机制的岩石薄片图像识别方法[P]. 湖北省：CN113486929B, 2023-02-24.

[200] 童轶之. 结合**残差收缩**和长短期记忆网络的轴承故障诊断[D]. 浙江理工大学, 2023.

[201] 朱文杰, 苗芳荣, 李云飞等.改进**DRSN**的抽油机轴承故障诊断系统[J]. 电工技术, 2023(16): 246-250.

[202] 杨晓岗. 基于改进**残差收缩网络**的不平衡时序数据故障诊断方法研究[D]. 北京化工大学, 2023.

[203] 唐世钰, 童靳于, 郑近德等. 改进的**深度残差收缩网络**轴承故障诊断方法[J]. 振动与冲击, 2023, 42(18): 217-224+285.

[204] 杜睿山, 程永昌, 孟令东. 基于**深度残差收缩网络**的油气柱高度预测[J]. 计算机技术与发展, 2023, 33(09): 175-181.

[205] 竹杭杰, 郭建新, 张雨帅等. 基于**DRSN**的通信信号调制方式识别方法[J/OL]. 无线电工程: 1-9 [2023-11-12].

[206] 张让勇, 郭文杰, 闫蕊等. 一种基于**DRSN**-CS和BiGRU+MLP模型的机械轴承剩余使用寿命预测方法[P]. 山东省：CN116842379A, 2023-10-03.

[207] 王康, 刘彩云, 熊杰等. 基于全卷积**残差收缩网络**的地震波阻抗反演[J/OL]. 物探与化探: 1-9 [2023-11-20].

[208] 陈琳伟, 应娉婷, 汤何胜等. 基于多传感器数据融合和**深度残差收缩网络**的轴向柱塞泵故障诊断[J]. 液压与气动, 2023, 47(11): 142-149.

[209] 尹建国, 盛文, 蒋伟. 基于**深度残差收缩网络**的雷达空中目标识别[J/OL]. 系统工程与电子技术: 1-8 [2023-11-29].

[210] 李天桢, 高世伟, 党小超等. 一种基于遮蔽卷积注意力**残差收缩网络**的软测量建模方法[P]. 甘肃省：CN116910483A, 2023-10-20.

[211] Song X, Zhang Q, Sun R, et al. A Hybrid Deep Learning Prediction Method of Remaining Useful Life for Rolling Bearings Using Multiscale Stacking **Deep Residual Shrinkage Network**[J]. International Journal of Intelligent Systems, 2023, 6665534.

[212] Huang X, Song Z, Ji C, et al. Research on a Classification Method for Strip Steel Surface Defects Based on Knowledge Distillation and a Self-Adaptive **Residual Shrinkage Network**[J]. Algorithms, 2023, 16(11): 516.

[213] Zhang Z, Zhang C, Zhang X, et al. **Deep residual shrinkage networks** with adaptively convex global parametric rectifier linear units for fault diagnosis[J]. Measurement Science and Technology, 2023, 35(2): 025023.

[214] Wu W, Peng H, Zhu H, et al. Mvc-Rsn: A Malware Variants Classification Method Based on **Residual Shrinkage Networks**[J]. Available at SSRN 4612610.

[215] 赵睿, 刘硕佳, 陈建勇. 基于**深度残差收缩网络**的非授权频段无线信号识别方法[P]. 福建省：CN117312942A, 2023-12-29.

[216] 杨阿锋, 庄立旭, 杨卓霖等. 融合注意力机制与**深度残差收缩网络**的水声目标识别方法[P]. 浙江省：CN117310668A, 2023-12-29.

[217] 贾广飞, 李明. 一种基于改进**深度残差收缩网络**的旋转机械故障诊断方法[P]. 河北省：CN117313003A, 2023-12-29.

[218] 邓艾东, 卞文彬, 刘洋等. 基于改进**深度残差收缩网络**的滚动轴承故障诊断方法[P]. 江苏省：CN114441173B, 2023-11-24.

[219] 陈晓兵, 郭舒心, 张闯闯等. 一种基于改进**深度残差收缩网络**的轴承故障诊断方法[P]. 江苏省：CN117112991A, 2023-11-24.

[220] 尹柏强, 程怡, 王若宇等. 基于改进一维**深度残差收缩网络**的电能质量扰动识别方法[P]. 安徽省：CN117093519A, 2023-11-21.

[221] 张璐莹, 卞雨辰, 蒋鹏等. 一种基于改进**残差收缩网络**的管道漏磁图像识别方法[P]. 黑龙江省：CN117058443A, 2023-11-14.

[222] 赵建, 姜伟. 融合改进TCN与**DRSN**的IoT入侵检测模型[J/OL]. 小型微型计算机系统:1-10 [2024-01-29].

[223] Sun Y, Zhang J, Zhang Y. New Deep Learning Network (**Deep Residual Shrinkage Network**) Is Applied for Lithology Identification To Search for the Reservoir of CO2 Geological Storage[J]. Energy & Fuels, 2024.

[224] Ehteram M, Afshari Nia M, Panahi F, et al. Gaussian mutation–orca predation algorithm–**deep residual shrinkage network (DRSN)**–temporal convolutional network (TCN)–random forest model: an advanced machine learning model for predicting monthly rainfall and filtering irrelevant data[J]. Environmental Sciences Europe, 2024, 36(1): 13.

[225] Sun Y, Pang S, Zhang J, et al. DRSN-GAF: **Deep Residual Shrinkage Network (DRSN)** for Lithology Classification through Well Logging Data Transformed by Gram Angle Field[J]. IEEE Geoscience and Remote Sensing Letters, 2023.

[226] Zhang L, Bian Y, Jiang P, et al. Improving Pipeline Magnetic Flux Leakage (MFL) Detection Performance with Mixed Attention Mechanisms (AM) and **Deep Residual Shrinkage Networks (DRSN)**[J]. IEEE Sensors Journal, 2024.

[227] Li Q, Lu T, Lai C, et al. Lithium-ion battery capacity estimation based on fragment charging data using **deep residual shrinkage networks** and uncertainty evaluation[J]. Energy, 2023: 130208.

[228] 陈仁祥, 张晓, 朱玉清等. 基于**深度残差收缩**迁移**网络**的复杂工况下滚动轴承故障诊断[J]. 振动与冲击, 2024, 43(03): 194-200.

[229] 郭松宜. 基于**残差收缩网络**与注意力机制的遥感图像目标检测算法[D]. 西安科技大学, 2022.

[230] 赵宇晗. 基于**残差收缩**的多状态下调节阀状态监控研究[D]. 哈尔滨工程大学, 2022.

[231] Wang L, Zou T, Cai K, et al. Rolling bearing fault diagnosis method based on improved **residual shrinkage network**[J]. Journal of the Brazilian Society of Mechanical Sciences and Engineering, 2024, 46(3): 1-12.

[232] Li T, Wu X, Luo Z, et al. A Baring Fault Diagnosis Method under Small Sample Conditions Based on the Fractional Order Siamese **Deep Residual Shrinkage Network**[J]. Fractal and Fractional, 2024, 8(3): 134.

[233] Li S, Qin L, Zhao D, et al. Indoor positioning system for single LED light based on **deep residual shrinkage network**[J]. Optics Communications, 2024: 130366.

[234] 高振国, 曹雯琪. 结合**残差收缩模块**的多传感器数据轴承故障诊断方法[P]. 福建省: CN117333715A, 2024-01-02.

[235] 郭棉, 曾繁成, 柳秀山等. 一种基于**残差收缩网络**的人体活动识别方法[P]. 广东省: CN117523672A, 2024-02-06.

[236] Zhu X, Zhang J, Wang X, et al. Improved **deep residual shrinkage network** for a multi-cylinder heavy-duty engine fault detection with single channel surface vibration[J]. Energy and AI, 2024, 100356.

[237] 全睿, 刘品, 张键等. 基于**RSN**-GRU融合网络的锂电池荷电状态估计[J/OL]. 华中科技大学学报(自然科学版): 1-7 [2024-03-14].

[238] 黄湛钧, 董鑫, 卢沐宇等. 基于**DRSN**与电压幅值分析的航空HVDC系统逆变器故障诊断[J]. 航空学报, 2024, 45(03): 216-227.

[239] Yang L, Chen Z, Xu Z, et al. Remaining Useful Life Prediction of Lithium-Ion Battery Based on Improved **Deep Residual Shrinkage Network**. Available at SSRN 4753969.

[240] 姜屹远. 基于**DRSN**-TCN的短期光伏功率预测及其不确定性分析[D]. 广西大学, 2023.

[241] 龚铭扬, 程瑞寅, 杨楚原, 等. 基于MRMR-**DRSN**的电力系统暂态稳定评估[J]. 电力学报, 2024, 39(01): 21-28.

[242] 邵小强, 原泽文, 杨永德, 等. 基于GRU-**DRSN**的双通道人体活动识别[J]. 科学技术与工程, 2024, 24(02): 676-683.

[243] 杨惠, 陈雷, 徐建军, 等. 基于一维**残差收缩网络**的电能质量复合扰动识别[J]. 自动化技术与应用, 2024, 43(04): 51-55.

[244] 邱少明, 刘良玉, 王岩, 等. 一种基于改进**深度残差收缩网络**的机械设备故障诊断方法[P]. 辽宁省: CN202311750834.X, 2024-03-19.

[245] 刘成勇, 吴玉意, 张丁丁, 等. 基于**深度残差收缩网络**的DAS管道监测信号识别方法[P]. 陕西省: CN202311624883.9, 2024-03-22.

[246] Yang J, Kong L, Ye H. Surface hardness determination of laser cladding using laser-induced breakdown spectroscopy and machine learning (PLSR, CNN, ResNet, and **DRSN**). Applied Optics, 2024, 63(10), 2509-2517.

[247] Yin J, Wen S, Zhang C, et al. Radar sequence HRRP target recognition based on **DRSN**-LSTM. In Proceedings of the 2024 8th International Conference on Control Engineering and Artificial Intelligence, 2024, pp. 66-72.

[248] 郝本建, 荣飞, 周子然, 等. 基于**DRSN**网络抗塔康干扰的IFF信号识别方法、系统、设备及存储介质[P]. 陕西省:CN202311817031.1, 2024-03-29.

[249] 朱劲锟, 郑侃, 梁振华, 等. 基于VAE-**DRSN**的微纳卫星推力器故障诊断方法[J]. 航天器工程, 2024, 33(02): 76-83.

[250] 梁惠康, 谢浩燊, 黄红斌, 等. 基于改进**深度残差收缩网络**的分布式光纤声传感信号识别[J]. 激光与光电子学进展, 2024, 61(05): 162-168.

[251] Liu Y, Wang Z, Zhang D, et al. Product Quality Anomaly Recognition and Diagnosis Based on **DRSN**-SVM-SHAP. Symmetry, 2024, 16(5), 532.

[252] 高树辉, 张浩. 融合HSI的**深度残差收缩网络**鉴别变造文件字迹油墨研究[J]. 中国人民公安大学学报(自然科学版), 2024, 30(01): 1-7.

[253] 潘雪娇, 董绍江, 周存芳, 等. 基于深度卷积自编码器和多尺度**残差收缩网络**的滚动轴承寿命状态识别[J]. 重庆交通大学学报(自然科学版), 2024, 43(05): 124-132.

[254] 金博, 章嘉湾. 基于离散小波和**残差收缩网络**的睡眠分期方法[J/OL]. 数据分析与知识发现, 1-14[2024-05-24].

[255] 王震, 牛晓伟. 双注意力密集**残差收缩网络**的图像去雨算法[J/OL]. 电光与控制, 1-9[2024-05-24].

[256] 冯骥, 杨国华, 史磊, 等. 基于并行融合**深度残差收缩网络**的有源配电网故障诊断[J/OL]. 综合智慧能源, 1-8[2024-05-24].

[257] 郜东瑞, 李小鱼, 沈艳, 等. 基于多尺度时间**残差收缩网络**的睡眠分期模型构建方法[P]. 四川省:CN202410101569.0, 2024-05-10.

[258] 宋月, 安治国, 黄晓红, 等. 一种基于改进**深度残差收缩网络**的图像纹理预测方法[P]. 河北省:CN202410157446.9, 2024-05-10.

[259] 田波, 张广生, 马泽宁, 等. 基于EMD-**DRSN**和ILSO-SVM的水电机组故障诊断[J/OL]. 中国农村水利水电, 1-13[2024-05-24].

[260] X Li, J Chen, J Wang, et al. Research on Fault Diagnosis Method of Bearings in the Spindle System for CNC Machine Tools Based on **DRSN**-Transformer[J].IEEE Access, Accepted.

[261] Zhang, X, Wang, Y, Wei, S, et al. Multi-scale **deep residual shrinkage networks** with a hybrid attention mechanism for rolling bearing fault diagnosis[J]. Journal of Instrumentation, 2024, 19(05), P05015.

[262] Wang, Q, Nie, Z, Liu, H. Assessment of Power System Stability During Transients Using **Deep Residual Shrinkage Network** and CBAM Integration[J]. Journal of Circuits, Systems and Computers, 2024.

[263] 刘高辉, 宋博武. 低信噪比下**DRSN**和集成融合的OFDM通信辐射源个体识别的方法[P]. 陕西: CN202410125095.3, 2024-05-24.

[264] Zuo, F, Zhang, D, Li, L, et al. GSOOA-1DDRSN: Network Traffic Anomaly Detection Based on **Deep Residual Shrinkage Networks**[J]. Heliyon, 2024.

[265] Zhang, P, Xue, Y, Song, R, et al. Photovoltaic DC arc fault detection method based on **deep residual shrinkage network**. Journal of Power Electronics, 2024, 1-13.

[266] 王晓琪, 吴轲, 赵观辉, 等. 基于全局注意力**残差收缩网络**的柱塞泵故障诊断方法[J/OL]. 中国舰船研究, 1-8 [2024-06-15].

[267] Jiang W, Wu J, Zhu H, et al.Multi-Model Fusion Health Assessment for MultiState Industrial Robot via Fuzzy **Deep Residual Shrinkage Network** and Versatile Cluster[J]. IEEE Transactions on Fuzzy Systems. 2024.

[268] 李振东. 基于**残差收缩网络**和卷积网络的机器人地面分类研究[D]. 哈尔滨工程大学, 2023.

[269] 曾高俊, 芦天亮, 任英杰, 等. 改进**深度残差收缩网络**的端到端合成语音检测[J/OL]. 计算机科学与探索, 1-15 [2024-06-21].

[270] 刘京华,魏祥麟,范建华,等.基于时序**深度残差收缩网络**的混叠信号调制识别方法[J/OL].电信科学,1-20[2024-08-02].

[271] Sun T, Gao J, Meng L, et al. A bearing fault diagnosis method based on adaptive **residual shrinkage network**[J]. Measurement, 2024: 115416.

[272] Cao J, Zhang J, Jiao X, et al. Gearbox Fault Diagnosis Method in Noisy Environments Based on **Deep Residual Shrinkage Networks**[J]. Sensors, 2024, 24(14): 4633.

[273] Gao S, Li T, Dong X. Soft sensor modeling based on masked convolutional transformer block **deep residual shrinkage network**[J]. Journal of the Taiwan Institute of Chemical Engineers, 2024, 163: 105666.

[274] Peng H, Li J, Cheng W, et al. Automatic diagnosis of pediatric high myopia via Attention-based Patch **Residual Shrinkage network**[J]. Expert Systems with Applications, 2024: 124704.

[275] 谢振华, 侯林明, 黄惠根, 等. 一种基于**深度残差收缩网络**的光伏串联直流电弧故障检测方法、存储介质及电子设备[P]. 浙江省: CN202410170401.5, 2024-06-25.

[276] 高慧慧, 马晟魁, 韩红桂, 等. 一种基于注意力增强记忆**残差收缩网络**的滚动轴承早期故障监测方法[P]. 北京市:CN202410280268.9, 2024-06-21.

[277] 陈松, 陈文华, 张文广. 基于**DRSN**融合Transformer编码器的轴承故障诊断方法研究[J]. 自动化与仪表, 2024, 39(05): 103-108.

[278] Luo L, Liu Y. Fault Diagnosis of Planetary Gear Train Crack Based on DC-**DRSN**[J]. Applied Sciences, 2024, 14(16), 6873.

[279] F. Wang; D. Chen; X. Zhang. Mental Fatigue Detection of Construction Equipment Operators Based on EEG Collected by A Novel Valve-type Semi-dry Electrode Using **Deep Residual Shrinkage Networks** under Real Construction Environment, IEEE Transactions on Instrumentation and Measurement, 2024.

[280] 杜雨蒙, 庄炜, 张旭, 等. 基于**DRSN**的MG-Y激光器快速准连续波长调谐方法[J]. 光子学报, 2024, 53(08): 167-176.

[281] T. Sun, J. Gao. New Fault Diagnosis Method for Rolling Bearings Based on Improved **Residual Shrinkage Network** Combined with Transfer Learning[J]. Sensors, 24(2024): 5700.

[282] Zhang Li, et al. **Residual Shrinkage** ViT with Discriminative Rebalancing Strategy for Small and Imbalanced Fault Diagnosis[J]. Sensors, 24(2024): 890.

[283] Chen H, et al. Automatic Modulation Recognition Method Based on Phase Transformation and **Deep Residual Shrinkage Network**[J]. Electronics, 13(2024): 2141.

[284] Liu Z., et al. **Deep residual shrinkage network** with multichannel VMD inputs for noise reduction of micro-thrust measurement[J]. AIP Advances, 14.6 (2024).

[285] Li S., H. Peng, Z. Mao. **Deep Residual Shrinkage Network** Based Fault Diagnosis for Quadrotor UAV Formation System[J]. IEEE 13th Data Driven Control and Learning Systems Conference, 2024.

[286] Liu, Xiangyu, and Zipeng Hou. Improved **Deep Residual Shrinkage Network** for Noisy Image Recognition. 5th International Seminar on Artificial Intelligence, Networking and Information Technology, 2024.

[287] Lin Z., et al. GNSS blanket jamming classification algorithm based on spatial attention mechanism and **residual shrinkage neural network**[J]. Measurement Science and Technology, 35(2024): 045120.

[288] 沈庆阳. 《第三章 基于混合注意力**残差收缩网络**的R2D2模型》基于深度学习的指针式仪表自动识别与示数读取方法研究[D]. 天津理工大学, 2023.

[289] 程倩.《基于改进**深度残差收缩网络**的无线电大雾天气监测方法》基于深度学习的无线电大雾天气监测方法[D].兰州交通大学,2023.

[290] 马国轩.《第三章 基于**深度残差收缩网络**的故障诊断方法》基于深度学习的机械故障诊断系统研究与实现[D].江苏大学,2023.

[291] 戴江涛.《第4章 基于双流**残差收缩网络**的人体动作识别》基于深度学习的人体动作识别方法研究[D].沈阳工业大学,2022.

[292] 李伟龙.《第4章 基于CBAM改进的**残差收缩网络**滚动轴承故障诊断方法》基于深度学习的滚动轴承故障诊断的方法研究[D].哈尔滨理工大学,2022.

[293] 张文鹏.《第四章 基于改进**深度残差收缩网络**的故障诊断算法》基于深度学习的光纤电流互感器故障诊断方法研究[D].东南大学,2022.

[294] 张雅雯.《基于**残差收缩网络**的时间序列分类算法》基于残差网络的时间序列分类算法研究[D].北京交通大学,2020.

[295] 刘安顺.《基于**深度残差收缩网络**的生成对抗网络去运动模糊》基于生成对抗网络的图像去运动模糊算法研究[D].西华大学,2022.

[296] 侯梦军.《基于**残差收缩**注意力网络的单样本部分遮挡人脸识别》基于深度学习的单样本部分遮挡人脸识别研究[D].重庆邮电大学,2022.

[297] 曾宏伟.《第五章 基于**深度残差收缩网络**的刀具磨损评估》钻削加工颤振监测、抑制及刀具磨损评估方法研究[D].上海交通大学,2021.

[298] 詹灿坚.《第四章 基于SRP-**残差收缩网络**的混合气体定量分析》基于仿生嗅觉的混合气体定量分析[D].广东工业大学,2021.

[299] 陈玲玲.《第3章 基于**残差收缩网络**的睡眠单通道脑电分期研究》基于深度神经网络的睡眠分期研究[D].哈尔滨工程大学,2022.

[300] 崔坤鹏.《基于**残差收缩网络**的脑图像配准方法》脑部核磁共振图像非刚性配准关键技术研究[D].郑州大学,2021.

[301] 陈辉.《基于**残差收缩网络**的姿态变化不敏感的纹理特征提取》姿态变化不敏感的足底识别算法研究[D].大连海事大学,2023.

[302] 陈文壮.《基于改进**深度残差收缩网络**的电机轴承故障诊断模型》基于深度迁移学习的电机轴承故障诊断方法研究[D].辽宁工程技术大学,2023.

[303] 徐威.《第3章 基于多尺度**深度残差收缩**的AUV推进器故障诊断》基于深度学习的AUV推进器多信源融合故障诊断方法研究[D].江苏科技大学,2023.

[304] 贺才郡.《基于**深度残差收缩网络**的PQDS识别》基于深度学习的电能质量扰动识别及模型轻量化研究[D].华中科技大学,2023.

[305] 孙诗胜.《第四章 基于改进**深度残差收缩网络**的轴承故障诊断研究》基于卷积神经网络的轴承故障诊断及寿命预测研究[D].石家庄铁道大学,2023.

[306] 刘伟洁.《第三章 基于2D-**DRSN**的心律失常分类研究》&《第四章 基于DRSN-Bi GRU的心律失常分类研究》基于深度学习的ECG心律失常分类研究[D].青海师范大学,2022.

[307] 杨一炫.《4.1 基于**深度残差收缩网络**的射频指纹识别》基于深度学习的通信个体辐射源识别研究[D].兰州交通大学,2023.

[308] 曾祥军.《基于混合卷积**深度残差收缩网络**的齿轮箱故障诊断》数据驱动的风电机组齿轮箱异常检测与故障诊断研究[D].山东大学,2022.

[309] 陆伟.《第5章 **深度残差收缩网络**与肌肉贡献度融合的肌力预测方法》基于肌电信号的人体上肢肌力预测方法研究[D].中国科学技术大学,2023.

[310] 李大鹏.《基于Mobile Net V3和**残差收缩网络**的鸟声识别算法》自然场景下鸟鸣声识别算法研究[D].南京信息工程大学,2022.

[311] 张文琪.《第四章 基于多尺度特征和**残差收缩网络**的多谱段图像匹配》基于CNN的多谱段图像匹配[D].贵州大学,2022.

[312] 王飞龙.《第4章 融合**深度残差收缩网络**与胶囊网络的带噪声小样本图像分类模型》基于胶囊网络的复杂小样本图像分类研究[D].太原理工大学,2021.

[313] 李慧.《第四章 基于多尺度**残差收缩网络**的遥感图像分类算法》结合面向对象与深度学习的高分辨率遥感图像分类研究[D].广东工业大学,2020.

[314] 陈润榕.《第四章 基于**深度残差收缩网络**的轴承故障诊断方法》&《第五章 基于混合域注意力的深度残差收缩网络的轴承故障诊断方法》基于深度学习的复杂工况下滚动轴承故障诊断方法研究[D].华南理工大学,2022.

[315] 李响.《第四章 基于深度迁移**残差收缩网络**的故障诊断方法》基于深度迁移学习的轴承故障诊断方法研究[D].佛山科学技术学院,2022.

[316] 龚玉晓.《第四章 基于改进**深度残差收缩网络**的心电信号分类算法》基于深度学习的心电信号自动分类算法研究[D].西安电子科技大学,2023.

[317] 张胜利.《第四章 基于自适应**深度残差收缩网络**的雷达辐射源脉内调制样式识别》基于深度学习的雷达辐射源识别研究[D].国防科技大学,2022.

[318] 陈成雪.《第3章 基于**DRSN**的行人检测算法》基于YOLOv4的交叉道路场景下的行人检测算法研究[D].沈阳师范大学,2023.

[319] 王云庆.《基于**DRSN**-BiLSTM刀具剩余使用寿命预测》基于信息融合的刀具磨损状态监测和剩余使用寿命预测[D].华东交通大学,2023.

[320] 唐震.《第二章 基于**深度残差收缩网络**的辐射源个体识别方法》基于深度学习的辐射源个体识别技术研究与实现[D].南京信息工程大学,2023.

[321] 刘师良.《第4章 基于IEMD和自适应**残差收缩网络**的轴承故障诊断》基于数据驱动和深度学习的滚动轴承故障诊断方法研究[D].青岛理工大学,2022.

[322] 胡博文.《第3章 基于**深度残差收缩网络**的电力系统暂态稳定预测方法》基于深度学习的电力系统暂态稳定预测研究[D].贵州大学,2023.

[323] 冯骥.《第五章 基于F**DRSN**-IBES-SVM的含DG配电网故障识别方法》基于多模型融合的含分布式电源配电网故障诊断研究[D].宁夏大学,2022.

[324] 续宗棠.《第三章 基于注意力机制改进的脉冲**残差收缩网络**模型》&《第四章 基于混合注意力机制的深度脉冲残差收缩网络模型》基于脉冲卷积神经网络的故障信号诊断[D].青岛大学,2023.

[325] 张睿琳.《基于**深度残差收缩网络**的帕金森脑电研究》&《5.1 可调Q因子小波变换与**深度残差收缩网络**结合的帕金森脑电研究》&《5.2 小波包变换与深度残差收缩网络结合的帕金森脑电研究》基于时频分析与深度学习的帕金森脑电分析[D].西北大学,2022.

[326] 史杨梅.《基于双通道阈值共享**深度残差收缩网络**的轴承故障诊断》基于声学信号的轴承故障诊断算法[D].中国矿业大学,2022.

[327] 刘芯志.《第四章 基于改进**深度残差收缩网络**的轻量级故障诊断方法》基于深度学习的滚动轴承故障诊断研究[D].湖南工业大学,2022.

[328] 杨惠.《第四章 基于一维**残差收缩网络**的电能质量复合扰动识别方法》基于深度学习的电能质量扰动识别方法研究[D].东北石油大学,2022.

[329] 马浩然.《第四章 基于Wide&Deep**残差收缩网络**的小样本学习》基于深度学习的刀具磨损自适应监测研究[D].华东师范大学,2023.

[330] 魏煦航.《基于**DRSN**的轴承健康状态评估建模》基于深度学习的印刷装备智能诊断系统研究与实现[D].北京印刷学院,2022.

[331] 郑琪.《第4章 基于**深度残差收缩网络**的电梯轴承分段剩余寿命预测》基于数据特征挖掘与机器学习的电梯故障诊断与预警[D].浙江大学,2022.

[332] 李雪松.《第三章 基于CWT-M**DRSN**的轴承故障诊断》基于深度学习的轴承故障诊断[D].青岛大学,2022.

[333] 文井辉.《第2章 基于**DRSN**的轴承健康指标构建方法研究》基于改进BiLSTM的轴承剩余寿命预测方法研究[D].重庆邮电大学,2022.

[334] 方鹏.《第三章 基于**深度残差收缩网络**的刀具磨损状态识别》基于多传感器信息融合的刀具磨损量监测系统研究[D].重庆交通大学,2021.

[335] 刘畅.《第四章 基于**DRSN**-ViT网络的图像情感分类识别模型》基于视觉深度自注意力变换网络的图像情感分类[D].西南大学,2022.

[336] 许历隆.《第三章 基于改进**残差收缩网络**的恶意应用细粒度分类方法》安卓恶意应用网络侧检测算法研究[D].南京信息工程大学,2022.

[337] 田科位.《第四章 噪声环境下基于改进**深度残差收缩网络**的刀具磨损状态识别方法研究》基于深度学习的刀具磨损状态监测方法研究[D].重庆交通大学,2022.

[338] 闫新艳.《第三章 基于**深度残差收缩网络**的商品图像识别》基于深度学习的商品识别技术研究[D].山西大学,2021.

[339] 熊志刚.《第3章 基于**深度残差收缩网络**和注意力机制的非侵入式负荷分解》基于深度学习的家用电器非侵入式负荷分解方法研究[D].湘潭大学,2022.

[340] 王之卓.《3.4 基于**深度残差收缩网络**的LDPC译码方案》车载信道下基于深度学习的LDPC译码算法研究[D].浙江科技学院,2021.

[341] 陈甜甜.《第3章 基于改进**深度残差收缩网络**的泄漏识别》基于深度学习的输油管道泄漏检测方法研究[D].中国石油大学(北京),2023.

[342] 何芋钢.《5.3 基于加权融合改进**深度残差收缩网络**》&《5.4 基于MDC和加权**DRSN**的成型鼓故障诊断试验》基于数据增强和改进残差网络的轮胎成型鼓故障诊断研究[D].华南理工大学,2022.

[343] 王彦博.《基于**深度残差收缩网络**的电力系统频率安全集成评估》基于深度学习的电力系统扰动后频率安全评估[D].北京交通大学,2023.

[344] 刘相武.《第4章 改进**DRSN**的往复式压缩机轴瓦故障诊断方法》基于改进残差网络的往复式压缩机轴瓦故障诊断方法研究[D].中国石油大学(北京),2023.

[345] 胡从强.《5.2 基于注意力机制和**深度残差收缩网络**的电弧故障检测》基于多模态特征分析的低压串联电弧故障检测研究[D].沈阳航空航天大学,2023.

[346] 曲胤熹.《第3章 一维**深度残差收缩网络**轴承故障诊断》基于深度学习的轴承预测性维护决策研究[D].沈阳大学,2023.

[347] 贾锐.《第三章 基于**深度残差收缩网络**的回放攻击检测》基于Sinc滤波器的语音回放攻击检测研究[D].安徽大学,2023.

[348] 罗煜坤.《基于CWT-**DRSN**-SVM的轴承故障诊断》基于深度学习的滚动轴承故障诊断方法研究[D].盐城工学院,2024.

[349] 郭延昭.《第三章 基于硬参数共享机制和**深度残差收缩网络**的无线感知算法》多任务学习框架下基于共享机制的无线感知技术研究[D].南京邮电大学,2023.

[350] 姚娜.《第3章 基于自适应抗噪的**DRSN**的滚动轴承故障诊断》基于机器学习的风力机滚动轴承故障诊断[D].东北电力大学,2023.

[351] 康哲恺.《第3章 基于**深度残差收缩网络**的恶意流量分类模型》基于深度学习的网络流量分类模型研究[D].中北大学,2023.

[352] 赵杰.《4.4 基于SET和**DRSN**的轴承智能故障诊断方法》基于时频特征提取的滚动轴承故障诊断方法研究[D].北京建筑大学,2022.

[353] 周晔.《第3章 基于**深度残差收缩网络**的多特征联合检测模型》基于深度学习的语音欺骗检测[D].杭州电子科技大学,2023.

[354] 王梦琪.《第4章 基于改进**深度残差收缩网络**的地震信号分类》基于改进深度残差网络的地震信号分类研究[D].广西师范大学,2022.

[355] 申平.《第四章 基于MOMEDA和**DRSN**的滚动轴承故障模式分类》基于解卷积的滚动轴承故障特征提取与智能诊断算法研究[D].华东交通大学,2023.

[356] 麻建新.《5.3 基于**深度残差收缩网络**的故障诊断及其相关算法》基于电参时序分析的油井故障诊断方法[D].沈阳理工大学,2023.

[357] 于顼顼.《第3章 基于**深度残差收缩网络**的城市环境声音识别算法》&《第4章 基于改进的Peephole网络和深度残差收缩网络的城市环境声音识别算法》基于深度学习的城市环境声音识别算法研究及系统实现[D].桂林理工大学,2022.

[358] 裴雪武.《第四章 基于改进**深度残差收缩网络**的滚动轴承寿命状态识别方法研究》滚动轴承早期失效判别及退化趋势预测方法研究[D].重庆交通大学,2022.

[359] 文培田.《第三章 双通道输入的WGAN和**DRSN**的滚动轴承智能诊断》基于生成对抗网络的滚动轴承故障特征提取及智能识别[D].华东交通大学,2022.

[360] 陈飞.《第四章 基于空洞残差**收缩卷积网络**的非侵入式负荷分解》面向住宅用户的非侵入式负荷监测方法研究[D].贵州大学,2022.

[361] 郭鲁豫.《第4章 基于改进**深度残差收缩网络**的电力系统暂态稳定评估》基于机器学习的电力系统暂态稳定评估[D].华北电力大学,2021.

[362] 谢松林.《4.2.3 基于**DRSN**与LSTM的特征频段识别模型》基于多源信号的开关冗余电源健康评估研究[D].电子科技大学,2022.

[363] 郑国亮.《第3章 基于**深度残差收缩网络**的线阵诊断方法》基于深度学习的阵列天线诊断方法研究[D].三峡大学,2022.

[364] 薛书鑫.《第3章 基于**残差收缩网络**的关系抽取模型》基于深度学习的关系抽取研究[D].重庆邮电大学,2022.

[365] 童轶之.《第3章 基于**DRSN**-LSTM模型的故障诊断》&《第4章 基于**DRSN**-BILSTM模型的故障诊断》结合残差收缩和长短期记忆网络的轴承故障诊断[D].浙江理工大学,2022.

[366] 张谦.《4.3 基于**深度残差收缩网络**的分类算法》癌变胃黏膜的拉曼光谱分析及分类研究[D].兰州大学,2022.

[367] 陈世鹏.《第5章 基于**DRSN**的改进TCN剩余寿命预测方法研究》船舶机械轴承故障识别与剩余寿命预测方法研究[D].江苏科技大学,2021.

[368] 阮智利.《2.2.2 基于**DRSN**自适应阈值冗余去除的双关节角度估计模型》肘腕关节连续运动估计及上肢外骨骼柔顺控制研究[D].武汉理工大学,2022.

[369] 高云飞.《4.1 融合**残差收缩块**的自注意力生成对抗网络进行人体姿态估计》基于自注意力生成对抗网络的人体姿态估计[D].中国矿业大学,2021.

[370] 宋雨萱.《第二章 基于**深度残差收缩网络**的鲁棒通信辐射源个体识别》演化深度学习研究与通信信号识别应用[D].西安电子科技大学,2020.

[371] 马鑫.《基于改进**深度残差收缩网络**的变压器故障特征识别》基于特征增强的变压器故障识别方法[D].华北水利水电大学,2021.

[372] 王然.《第4章 基于深度密集**残差收缩网络**的图像超分辨率》基于改进卷积神经网络的图像超分辨率重建算法研究[D].湖北工业大学,2021.

[373] 倪天琦.《4.5 基于3D**残差收缩网络**的集合预报区域性订正模型》集合预报洋面阵风订正研究[D].天津大学,2020.

[374] 孟庆旭.《5.2 **深度残差收缩网络**的泄漏识别模型》带压气体管道泄漏超声波检测方法研究[D].南昌航空大学,2022.

[375] 李新玉.《第3章 基于**DRSN**_CAM的动态主用户频谱感知算法》基于深度学习的频谱感知算法研究[D].杭州电子科技大学,2024.

[376] 宋育杰.《4.5 软判决下基于**DRSN**的LDPC码识别》基于深度学习的LDPC码闭集识别技术研究[D].西安电子科技大学,2023.

[377] 高怡宁.《特征聚类结合**深度残差收缩**的壁画风格迁移模型》墓室壁画风格迁移技术研究与应用[D].西安建筑科技大学,2023.

[378] 王彬宇.《基于**深度残差收缩网络**的电缆双故障监测》通信电缆故障智能监测技术研究[D].重庆大学,2022.

[379] 朱敬傲.《基于**深度残差收缩网络**的故障检测》基于机器学习的卫星姿态故障检测[D].中国科学院大学(中国科学院微小卫星创新研究院）,2022.

[380] 来庭煜.《基于优化S变换和改进**深度残差收缩网络**的识别方法》换流阀饱和电抗器铁心松动的振动及声纹识别研究[D].华北电力大学,2023.

[381] 邵梦园.《基于**深度残差收缩网络**的安卓恶意软件分类》基于深度主动学习的安卓恶意软件分类方法研究[D].西安电子科技大学,2022.

[382] 郑豪豪.《基于ResNet与**DRSN**的地磁数据去噪方法研究》基于参考道数据约束与深度学习的地磁数据去噪方法研究[D].东华理工大学,2023.

[383] 张毅恒.《第三章 基于VMD和**DRSN**的IFF辐射源细微特征识别》智能计算在IFF中的关键技术研究及应用[D].江南大学,2023.

[384] 施娜.《第五章 基于I**DRSN**的锂离子电池RUL预测》基于深度学习的锂离子电池健康状态评估和寿命预测研究[D].南京航空航天大学,2022.

[385] 李子睿.《基于自适应**残差收缩网络**的机械设备故障诊断方法》数据驱动的典型机械设备故障诊断技术研究[D].华中科技大学,2023.

[386] 来展航.《第4章 基于领域自适应**深度残差收缩网络**的变工况机床轴承故障诊断》可重构数控机床状态监测与故障诊断研究[D].天津职业技术师范大学,2024.

[387] 闫学成.《4.1 基于一维**深度残差收缩网络**的温度传感器偏差故障诊断方法》中央空调冷源系统温度传感器偏差故障诊断方法研究[D].华南理工大学,2023.

[388] 张诚志.《第三章 基于I**DRSN**-LSTM的变工况下的轴承故障诊断》基于深度学习的变工况下轴承故障诊断[D].安徽大学,2023.

[389] Yin B, Zeng Y, Wang R, et al. Small-Sample GIS Partial Discharge Type Identification Method Based on Fusion of One-Dimensional AT-**DRSN** and IDRN Models[J]. IEEE Transactions on Dielectrics and Electrical Insulation, 2024.

[390] Y. Shang, L. Geng, C. Li, et al. A Multi-Fault Testing Method for TSVs Based on GAF-**DRSN** and Mirror Constant Current Source Structure[J]. IEEE Transactions on Components, Packaging and Manufacturing Technology, 2024.

[391] Gao H, Zhang X, Gao X, et al. Multi-timescale Attention **Residual Shrinkage Network** with Adaptive Global-Local Denoising for Rolling-Bearing Fault Diagnosis[J]. Knowledge-Based Systems, 2024: 112478.

[392] 宋博武. 《**DRSN**与集成融合的OFDM辐射源个体识别方法研究》改进残差网络的OFDM辐射源个体识别方法研究[D]. 西安理工大学, 2024.

[393] 安有为.《第四章 基于时频增强和**深度残差收缩网络**的LFM信号源分类识别》抗信道影响的LFM信号源识别[D].东南大学,2023.

[394] 彭辉, 黄婧柠, 郑宇锋, 等. 基于改进**深度残差收缩网络**的光伏发电阵列故障诊断方法[J/OL]. 海军工程大学学报, 2024, 1-9.

[395] 洪乐. 基于多尺度**残差收缩网络**的滚动轴承故障诊断方法和系统[P]. 上海市:CN202410660807.1,2024-09-06.

[396] 刘振宇,钟鹏程,刘惠,等. 基于并行**残差收缩网络**的复杂装备关键零件故障诊断方法[P]. 浙江省:CN202410481948.7,2024-09-03.

[397] 伍兴,李志伟,宁文乐,等. 基于LWKConv-**DRSN**-FPN的旋转机械故障诊断[J]. 噪声与振动控制,2024,44(05):133-139.

[398] 李帅帅. 基于**DRSN**神经网络的NPC多电平逆变器开路故障诊断[D]. 南昌大学,2024.

[399] 王童童, 杜嘉仪, 谈贇, 等. 一种基于**深度残差收缩网络**的磁干扰补偿方法[P]. 陕西省:CN202410816885.6, 2024-10-29.

[400] 李嘉豪, 张兵, 朱建阳. 基于**深度残差收缩网络**的刀具故障自感知系统研究[J]. 农业装备与车辆工程, 2024, 62(10): 104-110.

[401] 唐丹, 吴浩, 蔡源, 等. 基于改进**深度残差收缩网络**的电缆早期故障识别[J]. 科学技术与工程, 2024,24(28): 12159-12168.

[402] 卢宁. 基于**残差收缩网络**的地铁浮置板隔振器失效检测方法研究[D]. 西南交通大学, 2023.

[403] 刘国柱. 数据增强条件下基于改进**深度残差收缩网络**的变压器故障诊断方法[D]. 安徽理工大学, 2024.

[404] 朱良玉. 基于**深度残差收缩网络**和迁移学习的轴承故障定量诊断方法研究[D]. 桂林电子科技大学, 2023.

[405] 李逸凡. 基于**深度残差收缩网络**的射频指纹特征提取与识别研究[D]. 海南大学, 2023.

[406] 张正旭. 基于注意力和多尺度**残差收缩**U-Net的胎儿心电提取[D]. 哈尔滨理工大学, 2023.

[407] 王瑞峰, 王智. 基于**DRSN**-BiLSTM的S700K转辙机故障诊断[J/OL]. 电子测量与仪器学报, 1-10[2024-11-24].

[408] 韩东洋,陈宏,陈新财,等.短时傅里叶变换结合**DRSN**的滚动轴承故障诊断研究[J].中国测试,2024,50(10):136-141.

[409] Lv X, Wang J, Qin R, et al. Self-learning guided **residual shrinkage network** for intelligent fault diagnosis of planetary gearbox[J]. Engineering Applications of Artificial Intelligence, 2025, 139: 109603.

[410] Qiu S, Liu L, Wang Y, Mechanical equipment fault diagnosis method based on improved **deep residual shrinkage network**[J]. PloS one, 2024, 19(10): e0307672.

[411] Xu C, Wu J, Xuan Q, et al. A Robust Specific Emitter Identification Method for CPS Devices Based on **Deep Residual Shrinkage Network**[J]. IEEE Transactions on Reliability, 2024.

[412] Wang L, Xie K. Multi‐function radar work mode recognition based on **residual shrinkage** reconstruction recurrent neural network[J]. IET Radar, Sonar & Navigation, 2024.

[413] Hong L, Wen C.Rolling bearing fault diagnosis based on multiscale **residual shrinkage network**[C]. In Sixth International Conference on Information Science, Electrical, and Automation Engineering (ISEAE 2024) (Vol. 13275, pp. 559-564).

[414] Wang L, Zhu T, Xu X, et al. Detection and Identification of Maize Disease and Insect Pests Based on the Spatial **Residual Shrinkage Network** Model[C]. In 8TH International Conference on Computing, Control and Industrial (Vol. 2, p. 86). Springer Nature, 2024.

[415] Yin S, Chen Z. Research on Compound Fault Diagnosis of Bearings Using an Improved **DRSN**-GRU Dual-Channel Model[J]. IEEE Sensors Journal, 2024.

[416] 赵睿诚.《4.2 基于**深度残差收缩网络**的磁干扰补偿方法》基于机器学习的地磁测量干扰补偿方法研究[D].西安理工大学,2024.

[417] 李俊屿.《3.1 基于**深度残差收缩**的语音流网络》基于双流网络的语音-人脸跨模态匹配方法[D].中国人民公安大学,2024.

[418] 曾昭优.《第四章 基于迁移**深度残差收缩网络**的鸟鸣声识别研究》基于深度学习的鸟鸣声识别方法研究[D].南京信息工程大学,2024.

[419] 曹善杰.《第四章 基于**深度残差收缩网络**的温度廓线反演模型》基于卷积网络的FY-4A/GIIRS温度廓线反演方法研究[D].南京信息工程大学,2024.

[420] 邹丰帆.《3.1 基于**DRSN**和Transformer编码器的心电信号分类网络》基于深度学习的心电信号分类及分割研究[D].南昌大学,2024.

[421] 赵炳辉.《5.1 多尺度融合全局**残差收缩网络**的网络构建》深度学习框架下多震源地震波场高精度重建方法研究[D].吉林大学,2024.

[422] 张浩.《5.3 基于**深度残差收缩网络**的构建及结构改进》基于高光谱技术的汽车车身油漆物证智能识别方法研究[D].中国人民公安大学,2024.

[423] 李晗峰.《第四章 基于改进**残差收缩**单元的枪声分类与定位模型》基于深度学习的枪声分类与定位方法研究与系统实现[D].电子科技大学,2024.

[424] 胡俊伟.《第3章 基于先验知识的**残差收缩**原型网络小样本故障诊断》面向小样本跨域复杂场景的旋转机械设备智能诊断算法研究[D].武汉科技大学,2024.

[425] 封强.《3.1.1 **深度残差收缩网络**》深度学习框架下微地震信号识别与震源定位方法研究[D].吉林大学,2023.

[426] 张尹.《5.2.1 **深度残差收缩神经网络**》基于脑电信号特征处理和深度学习的癫痫发作预测研究[D].南京邮电大学,2023.

[427] 陈顺.《4.2 基于**残差收缩块**与多尺度注意力机制的DLBCL分割网络》跨模态弥漫性大B细胞淋巴瘤自动分割及预后研究[D].南京邮电大学,2023.

[428] 孔志伟.《4.3 基于D-**DRSN**的负荷分解模型》《4.3.2 **深度残差收缩网络**》面向家庭用户的非侵入式负荷监测方法研究[D].山东建筑大学,2023.

[429] 邱野.《3.3.1 **深度残差收缩网络**》基于深度学习的地铁行人目标检测方法研究[D].南京信息工程大学,2023.

[430] 张亚洲.《3.2.1 **残差收缩模块**》《3.3.1 多尺度**残差收缩块**》基于卷积神经网络的滚动轴承故障诊断与剩余寿命预测研究[D].兰州理工大学,2023.

[431] 杨锋.《4.3 基于**DRSN网络**的无意调制识别方法》《4.2.2 **深度残差收缩网络(DRSN)**》基于轻量化神经网络的雷达辐射源识别研究[D].南昌大学,2023.

[432] 刘志刚.《6.2 **深度残差收缩网络(DRSN)**》《6.2.1 **深度残差收缩网络**的基本层》《6.2.2 **深度残差收缩网络**的残差收缩模块》铁路轴箱轴承故障微弱特征信息提取及性能退化评估研究[D].华东交通大学,2023.

[433] 范晓旭.《3.3 建立**深度残差收缩网络**模型》基于角点检测的煤矸石识别方法研究[D].辽宁工程技术大学,2023.

[434] 朱富海.《5.1 **深度残差收缩模块**研究》《5.1.4 **深度残差收缩网络**》基于可调谐激光器和深度学习的甲烷气体检测[D].东北石油大学,2023.

[435] 黄雄伟.《4 基于**残差收缩**的室内定位与手势识别联合网络》基于WiFi的手势识别和位置分类联合深度学习方法研究[D].广东技术师范大学,2023.

[436] 郭梓良.《第四章 VMD算法和改进**残差收缩网络**的故障诊断研究》基于信号处理和改进残差网络的齿轮箱故障诊断研究[D].石家庄铁道大学,2023.

[437] 苗芳荣.《3.6 改进**深度残差收缩神经网络**》《3.6.1 **深度残差收缩神经网络**模型》《3.6.2 改进**深度残差收缩神经网络**模型》游梁式抽油机状态监测与故障识别系统研究[D].青岛理工大学,2023.

[438] 吴永珍.《3.2 基于**深度残差收缩网络**的人脸表情图像情绪识《3.2.1 **深度残差收缩网络**基本结构》《3.2.2 **深度残差收缩网络**模型的设计》基于人脸表情图像和脑电信号的多模态情绪识别[D].青岛大学,2023.

[439] 赵儒.《3.2.2 **深度残差收缩模块**》基于UWB和IMU的人员定位与步态识别研究[D].山东大学,2023.

[440] 范方朝.《4.2.2 **深度残差收缩网络**》基于深度学习的脑电信号识别与分类算法研究[D].北京交通大学,2023.

[441] 孙珂.《第4章 基于交叉单元的**深度残差收缩网络**》基于卷积网络的交通流量分析技术研究[D].黑龙江大学,2023.

[442] 罗嗣鑫.《3.2.2 **残差收缩模块**》基于多尺度显著特征的PSG自动睡眠分期研究[D].重庆理工大学,2023.

[443] 陶孟元.《3 结合**残差收缩**和时空上下文的行为检测方法》《4 基于**残差收缩**和时空对称多尺度的行为检测方法》基于时空协同的自然场景人体行为检测方法研究[D].安庆师范大学,2023.

[444] 安宇.《第四章 基于**残差收缩**和可变形空洞卷积的板材表面缺陷识别模型》《4.3 可变形**残差收缩模块**和空洞残差收缩模块》基于深度学习的板材表面缺陷识别研究及应用[D].太原科技大学,2023.

[445] 廖宏程.《2.1.2 **深度残差收缩网络**》基于多尺度回声状态网络的变速器试验运行故障识别研究[D]. 重庆科技学院, 2023.

[446] 孟储航. 《第3章 基于**深度残差收缩网络**的复合故障诊断》数据驱动的船舶柴油机复杂故障诊断方法研究[D]. 哈尔滨工业大学, 2023.

[447] 张均益. 《第4章 基于**残差收缩**图注意力网络的故障预测》基于图神经网络的船舶柴油机故障预测方法研究[D]. 哈尔滨工业大学, 2023.

[448] 龙辉. 《第4章 基于**深度残差收缩网络**的车轮扁疤故障诊断》基于车载振动响应的地铁车轮扁疤辨识方法研究[D]. 西南交通大学, 2023.

[449] 王凯. 《第四章 基于动态卷积**深度残差收缩网络**的电能质量扰动识别》基于深度卷积神经网络的电能质量扰动识别方法研究[D]. 东北石油大学, 2023.

[450] 何云川. 《4.2.2 **残差收缩模块**》基于深度学习的行人重识别方法研究[D]. 西安工业大学, 2023.

[451] 董宁. 《4.3 基于**残差收缩网络**的雷达信号识别》基于时频域特征和深度学习的雷达信号脉内调制识别方法[D]. 吉林大学, 2023.

[452] 吴小飞. 《4.3.2 **残差收缩网络**》基于深度学习的SAR图像目标识别方法研究[D]. 西南科技大学, 2023.

[453] 许宝然. 《2.4.2 **深度残差收缩网络**》基于拉曼光谱结合深度学习的蜂蜜品质鉴别技术研究[D]. 燕山大学, 2023.

[454] 杨朋辉. 《5.4.3 **深度残差收缩模型**》基于卷积循环神经网络的脑电信号情绪识别方法研究[D]. 燕山大学, 2023.

[455] 马嘉辉. 《4.1 **深度残差收缩网络**》基于深度森林与BiGRU的网络安全态势感知方法[D]. 哈尔滨师范大学, 2023.

[456] 彭军英. 《4.1.2 **深度残差收缩模块**》基于散斑自相关感知学习的散射成像技术研究[D]. 哈尔滨工程大学, 2023.

[457] 伍昊昕. 《4.3.3 基于多通道的**残差收缩网络**的改进》基于小波变换的混凝土缺陷超声检测方法研究[D]. 湖南大学, 2023.

[458] 刘鑫鹏. 《5 基于改进**深度残差收缩网络**的烟叶光谱定性建模方法》基于近红外光谱的卷烟原料质量评价研究[D]. 青岛科技大学, 2023.

[459] 史大印. 《第四章 基于多尺度**残差收缩网络**的房颤识别技术研究》基于深度学习的心房颤动识别技术研究[D]. 山东理工大学, 2023.

[460] 夏蒸富. 《4.2.1 **深度残差收缩网络**模块》基于深度学习的复杂环境声音识别研究[D]. 重庆交通大学, 2023.

[461] 王瑞东. 《4.2 **深度残差收缩网络**》基于多级多输出深度学习模型的滚动轴承故障诊断方法研究[D]. 长安大学, 2023.

[462] 卢安琪. 《4.3.2 时域注意力机制**残差收缩网络**》《4.3.3 通道域注意力机制**残差收缩网络**》基于集成学习与注意力机制的泵机设备异常声音检测方法研究[D]. 合肥学院, 2023.

[463] 刘艳. 《2.4 **深度残差收缩网络**》基于深度学习的圆锥角膜辅助诊断[D]. 天津理工大学, 2023.

[464] 王钧珲. 《3.2.3 一维**残差收缩网络**》基于脑电微状态与功能脑网络的听障者情感识别研究[D]. 天津理工大学, 2023.

[465] 李颖. 《第5章 基于**残差收缩网络**的单幅图像超分辨率方法》基于深度学习的单幅图像超分辨率方法研究[D]. 哈尔滨工业大学, 2023.

[466] 赵文翔, 普运伟.《1.2 **深度残差收缩网络**和组归一化》一种改进生成对抗网络的遥感图像去云方法[J]. 遥感信息, 2024, 39(05): 78-85.

[467] 刘云峰, 杨晋彪, 韩晋锋, 等.《2.1 **残差收缩网络**》基于边缘增强生成对抗网络的电力设备热成像超分辨率重建[J]. 电力建设, 2021, 42(07): 83-89.

[468] 史宝岱, 张秦, 李宇环, 等.《2 **残差收缩网络**》基于混合注意力机制的SAR图像目标识别算法[J]. 电光与控制, 2023, 30(04): 45-49.

[469] 马贵林, 李世超, 高宏力, 等.《2.1 **深度残差收缩网络**》考虑噪声抑制的高超声速风洞气动力识别方法[J]. 航空动力学报, 2023, 38(02): 420-430.

[470] 雷宇, 刘少儒, 徐寅林.《1.1 **DRSN**分类诊断模型的设计》具有自动抗噪功能的心电信号分类算法[J]. 电子测量技术, 2021, 44(21): 49-55.

[471] 徐成霞, 阎庆, 李腾, 等.《2.1 **深度残差收缩网络**》基于联合注意力机制的单幅图像去雨算法[J]. 计算机应用, 2022, 42(08): 2578-2585.

[472] 赵迪, 王呈.《1.1 面向特征提取的**DRSN**模块》基于改进胶囊网络的运维知识库故障分类方法[J]. 电子测量与仪器学报, 2022, 36(05): 104-112.

[473] 张秀再, 邱野, 张晨.《2.2.1 **深度残差收缩网络**》改进YOLOv5s算法的地铁场景行人目标检测[J]. 激光与光电子学进展, 2023, 60(06): 144-153.

[474] 贺才郡, 李开成, 董宇飞, 等.《2.3 **DRSN**》基于知识蒸馏与RP-MobileNetV3的电能质量复合扰动识别[J]. 电力系统保护与控制, 2023, 51(14): 75-84.

[475] 张浩, 高树辉.《1.6.2 改进的1D-**DRSN**高光谱数据分类模型》基于高光谱技术的现场车漆物证识别模型研究[J]. 分析测试学报, 2023, 42(07): 817-824.

[476] 陈作懿, 邓超, 吴军, 等.《2.1 **残差收缩网络**》基于收缩自注意关系网络的机械装备故障智能检测与定位方法[J]. 中国科学:技术科学, 2023, 53(07): 1214-1228.

[477] 杨晓岗, 夏涛.《2) **残差收缩块**》基于多尺度融合模型的化工故障诊断[J]. 电子测量技术, 2023, 46(13): 8-16.

[478] 宋绍剑, 姜屹远, 刘斌.《1 基于SSA优化的**DRSN**-TCN短期光伏功率点预测模型》一种TCN的改进模型及其在短期光伏功率区间预测的应用[J]. 计算机应用研究, 2023, 40(10): 3064-3069.

[479] 闫文恒, 程永强, 郝润芳.《1.4 **深度残差收缩网络**》双重融合的轻量级卷积神经网络轴承故障诊断[J]. 组合机床与自动化加工技术, 2023, (05): 174-177+183.

[480] 李大鹏, 周晓彦, 王基豪, 等.《1.2 **DRSN**》基于Mel频谱值和深度学习网络的鸟声识别算法[J]. 应用声学, 2023, 42(04): 825-832.

[481] 阮慧, 黄细霞, 李登峰, 等.《1.2 **深度残差收缩网络**》滚动轴承细粒度故障诊断研究[J]. 计算机工程与应用, 2024, 60(06): 312-322.

[482] 刘云鹏, 来庭煜, 刘嘉硕, 等.《4.1 改进**深度残差收缩网络**》特高压直流换流阀饱和电抗器振动声纹特性与松动程度声纹检测方法[J]. 电工技术学报, 2023, 38(05): 1375-1389.

[483] 李帅永, 张超, 梅琳, 等.《1.1 **深度残差收缩网络**》基于改进Holt双指数模型的轴承剩余寿命预测方法[J]. 自动化与仪器仪表, 2023, (02): 87-93.

[484] 陈佳, 章坚武, 张浙亮.《1.1 **深度残差收缩网络**》基于上下文信息与注意力特征的欺骗语音检测[J]. 电信科学, 2023, 39(02): 92-102.

[485] 余佳润, 王亚峰.《2.3 基于**DRSN**的LOS径DoA估计方法》一种低信噪比下基于深度学习的DoA估计方法[J]. 北京邮电大学学报, 2022, 45(06): 115-121.

[486] 黄志静, 邵慕义, 张庭瑞, 等.《2.5 **深度残差收缩网络**》基于深度学习的野生动物识别[J]. 电子测试, 2022, 36(22): 69-71+10.

[487] 林涛, 吉萌萌, 付崇阁, 等.《2. 2 **深度残差收缩网络**》《3.2 改进的堆叠**残差收缩网络**块》基于改进时间卷积网络的空气质量预测研究[J]. 计算机仿真, 2022, 39(10): 451-456+501.

[488] 周晔, 章坚武, 程继承.《2.1 **残差收缩**构建单元RSBU》面向复杂声学环境的伪装语音检测[J]. 传感技术学报, 2022, 35(10): 1355-1362.

[489] 刘芯志, 彭成, 满君丰, 等.《1.4 改进的**深度残差收缩模块**》改进残差结构的轻量级故障诊断方法[J]. 计算机工程与设计, 2022, 43(08): 2303-2310.

[490] 李新玉, 赵知劲.《1.2.1 **深度残差收缩模块DRSN**》基于深度学习的动态主用户频谱感知算法[J]. 电子技术应用, 2024, 50(01): 60-65.

[491] 杨靛青, 毛艳萍.《2.3 **深度残差收缩网络DRSN**-CW》基于改进深度学习的航拍滑坡检测方法[J]. 计算机工程与设计, 2024, 45(01): 268-274.

[492] 刘媛媛, 程双全, 朱路, 等.《1.1 **残差收缩网络**》多尺度关键信息融合的轻量级图像超分辨重建[J]. 光电子·激光, 2024, 35(11): 1145-1154.

[493] 黄宇, 张宗拾, 刘家兴, 等.《1.1 **深度残差收缩网络**》基于改进时间卷积网络与藤Copula的短期风速预测[J]. 电力科学与工程, 2024, 40(07): 60-69.

[494] 马剑波, 左翔, 丛小飞, 等.《3.1 **深度残差收缩网络**》基于深度学习的水利工控网络流量异常检测方法[J/OL]. 水利水电技术(中英文), 1-14[2024-11-27].

[495] 苌文涵, 张云翔, 顾彬, 等.《2.1 改进**DRSN**》结合改进DRSE-GCNN的电力调度语声识别模型[J/OL]. 应用声学, 1-10[2024-11-27]

[496] 李振坤, 张天翼, 邓莉荣, 等.《3 基于**DRSN**-TCN的韧性在线评估模型》基于模型-数据混合驱动的区域能源互联网韧性在线评估[J]. 电网技术, 2024, 48(10): 4060-4076.

[497] 查燕平, 王红军, 沈哲贤.《1.1 **深度残差收缩网络**》特征融合式轻量化调制识别方法设计与研究[J/OL]. 小型微型计算机系统, 1-10[2024-11-27].

[498] 黎芮彤. 《2.2.5 **深度残差收缩网络DRSN**》面向程序语言和自然语言的查询匹配模型研究[D]. 武汉大学, 2021.

[499] 江伟雄, 王吉, 吴军, 等. 基于模糊**残差收缩网络**与人机协同的机械装备健康评估方法[J/OL]. 仪器仪表学报, 1-13 [2024-12-06].

[500] 何牧耕.《5 基于改进**残差收缩**D3QN的噪声环境故障诊断》非完备弱数据环境下基于深度强化学习的旋转机械故障诊断研究[D]. 重庆大学, 2023.

[501] 文秀华.《3 基于**深度残差收缩网络**的无线设备识别方法》信号指纹特征提取与识别方法研究[D]. 海南大学, 2022.

[502] 邢佳豪. 基于改进**残差收缩网络**和雷达时频信息的心跳检测研究[D]. 河北工业大学, 2023.

[503] 董贵平, 鞠含, 杜琛鑫, 等. 基于**深度残差收缩**记忆网络的猫粮投喂量预测方法[P]. 江苏省:CN202411009159.X, 2024-11-22.

[504] 王誉霏. 基于**DRSN**-BiGRU的滚动轴承剩余使用寿命预测方法研究[D]. 沈阳工业大学, 2024.

[505] 龙云峰. 《4 基于**残差收缩网络**和联邦学习的局部放电模式识别方法》变压器局部放电监测柔性天线与分布式深度学习模式识别研究[D]. 重庆大学, 2023.

[506] 周云龙. 《3.3 **深度残差收缩模块**(DRSH)》基于全卷积神经网络脑组织和胶质瘤分割算法研究[D]. 东北大学, 2021.

[507] 周晗. 《4.3.2 **残差收缩网络DRSN**-RFFE模型设计》信号图像特征扩维射频指纹库构建及其应用[D]. 电子科技大学, 2024.

[508] 王晗铭. 基于纹理-颜色二分支多尺度**残差收缩网络**的玉米病害识别[D]. 华中农业大学, 2024.

>针对现有的玉米病害识别方法难以克服复杂背景干扰、多尺寸病斑识别准确度低的问题，提出了一种基于深度学习的纹理-颜色二分支多尺度**残差收缩网络**模型（TC-MRSN）。模型的主要内容如下：（1）提出了纹理特征提取模块和纹理-颜色二分支模块，用于从病斑中提取纹理特征并将纹理特征与颜色特征融合，达到采样过程中保留小尺寸病斑特征信息的目的；（2）提出了多尺度**残差收缩模块**，用于提取不同的感受野特征并用软阈值函数对冗余噪声进行处理，从而减少冗余背景噪声对病斑融合特征的干扰；（3）构建TC-MRSN模型，同时兼顾“复杂背景”与“多尺寸病斑识别”两要素，实现了不同尺寸的玉米叶片病斑特征的有效提取。

>本章结合论文中提出的基于纹理颜色二分支**残差收缩网络**的玉米叶片病害识别模型，设计并实现一个移动端离线玉米病害识别系统，用户通过相册上传待测图像或直接通过系统在田间拍摄玉米病害图像，接下来系统对用户输入的图像进行预处理将其转换为标准格式，然后输入模型进行病害识别。

[509] 邢佳豪. 基于改进**残差收缩网络**和雷达时频信息的心跳检测研究[D]. 河北工业大学, 2023.

>为了解决心跳检测容易被呼吸谐波、身体晃动等因素干扰的问题，提出了一种基于改进**深度残差收缩网络**重构雷达信号的心跳检测算法，针对心跳信号低信噪比的特点，构建了改进**残差收缩网络**，在重构信号的过程中加入去噪功能，以获得更加准确的心跳检测效果。

>考虑到雷达信号在时域和频域上的信息互补性，提出了基于时频信息重构雷达信号的心跳检测方法，使用改进的**残差收缩网络**捕获时域上的信息，另外设计了一个自适应希尔伯特-黄变换模块，用于捕获频域上的信息，并将其嵌入到神经网络中，通过对改进**残差收缩网络**提取的时域特征与自适应希尔伯特-黄变换模块提取的时频特征进行融合，有效地结合了时域和频域信息，从而以更加全面的信息对雷达信号进行重构，进一步提高心跳检测准确率，并在采集的数据集上验证了该模型的有效性。

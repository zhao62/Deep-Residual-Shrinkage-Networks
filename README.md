# Deep-Residual-Shrinkage-Networks 深度残差收缩网络

The deep residual shrinkage network is a variant of deep residual networks (ResNets), and aims to improve the feature learning ability from highly noise signals or complex backgrounds. Although the method is originally developed for vibration-based fault diagnosis, it can be applied to image recognition and speech recognition as well. The major innovation is the integration of soft thresholding as nonlinear transformation layers into ResNets. Moreover, the thresholds are automatically determined by a specially designed sub-network, so that no professional expertise on threshold determination is required.

![The basic idea of deep residual shrinkage networks](https://github.com/zhao62/Deep-Residual-Shrinkage-Networks/blob/master/Basic-idea-of-DRSN.png)

The method is implemented using TensorFlow 1.0.1, TFLearn 0.3.2, and Keras 2.2.1, and applied for image classification. A small network with 3 residual shrinkage blocks is constructed in the code. More blocks and more training iterations can be used for a higher performance.

## Abstract (摘要)
This paper develops new deep learning methods, namely, deep residual shrinkage networks, to improve the feature learning ability from highly noised vibration signals and achieve a high fault diagnosing accuracy. Soft thresholding is inserted as nonlinear transformation layers into the deep architectures to eliminate unimportant features. Moreover, considering that it is generally challenging to set proper values for the thresholds, the developed deep residual shrinkage networks integrate a few specialized neural networks as trainable modules to automatically determine the thresholds, so that professional expertise on signal processing is not required. The efficacy of the developed methods is validated through experiments with various types of noise.

## Original Paper (原始文献)

***Minghang Zhao, Shisheng Zhong, Xuyun Fu, Baoping Tang, Michael Pecht, Deep residual shrinkage networks for fault diagnosis, 
IEEE Transactions on Industrial Informatics, 2020, 16(7): 4681-4690.***

**The paper has been cited over 1000 times on Google Scholar. (本论文的谷歌学术引用量已经超过1000次)**

https://scholar.google.com/citations?user=k82TzLwAAAAJ&hl=zh-CN

https://ieeexplore.ieee.org/document/8850096

http://homepage.hit.edu.cn/zhaominghang

## Additional Notes (备注)

There might be some problems in the Keras code. The TFLearn code is recommended for usage.

## Thanks for the Applications (感谢以下文献及作者)

**According to incomplete statistics, deep residual shrinkage networks have been directly applied or improved by many scholars to many fields such as machinery, electricity, vision, medical, speech, text, radar, remote sensing.(根据不完全统计，深度残差收缩网络已经被国内外学者直接应用或改进后应用于机械、电力、视觉、医疗、语音、文本、雷达、遥感等众多领域)**

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

[510] 梁欣涛, 王玉静, 乔春阳, 等. 一种改进关系网络的滚动轴承故障识别方法[P]. 黑龙江省:CN202110975013.0, 2024-11-29.

>根据元学习训练策略划分数据集，并将**残差收缩模块**和SELU激活函数引入关系网络的嵌入模块中，**残差收缩模块**利用注意力机制自动确定阈值，将信号中的冗余信息剔除。

[511] 黎国强, 段超群, 吴德烽, 等. 一种滚动轴承零故障样本诊断方法[P]. 福建省:CN202411162922.2, 2024-11-22.

>建立多个基于**深度残差收缩网络**的特征编码器，设计一种全新的对比损失函数，利用灰度图像训练集，优化特征编码器。

[512] 涂锦波, 施文铮, 刘晓敏, 等. 一种基于大数据的伤情理赔智能预测方法及系统[P]. 福建省:CN202411371405.6, 2024-11-01.

>采用结合**残差收缩单元**的深度神经网络，进行伤情理赔预测，并通过构建组合层，收缩过滤阈值函数来改进原本**残差收缩**单元的软阈值过滤策略，缓解了信息的过度过滤和重要信息丢失的问题，提高了预测的整体准确性，并提升了伤情理赔智能预测的整体可用性。

[513] 耿国华, 赵虹乔, 刘阳洋, 等. 一种基于卷积神经网络的陶瓷碎片分类方法[P]. 陕西省:CN202210793879.4, 2024-10-29.

>构建**深度残差收缩网络**，**深度残差收缩网络**由八个**残差收缩**块堆叠而成，**残差收缩**块包括残差单元、阈值学习单元和软阈值化处理单元；在ResNet18网络的每一个残差单元后加入阈值学习单元，将阈值学习单元输出的阈值再输入到软阈值化处理单元中，将得到的处理结果与输入特征图实现残差连接，得到最终的输出特征图，构建**残差收缩**块，**残差收缩**块堆叠成**深度残差收缩网络**。

[514] 彭倩, 曲家璇, 韩锋钢. 基于数字孪生的电动矿卡动力电池SOC预测方法、装置[P]. 福建省:CN202411065041.9, 2024-10-25.

>引入深度学习的方法，融入**深度残差收缩网络**，对仿真数据进行学习训练。该方法可以根据实时获取的数据和外部条件动态调整训练优化模型，从而提高SOC预测的鲁棒性。

[515] 黄晋英, 白雄, 王宇轩, 等. 一种基于数据驱动的特种车辆座椅振动舒适性评价方法[P]. 山西省:CN202410736586.1, 2024-10-18.

>然后将提取融合后的特征信息通过改进**残差收缩模块**生成新的网络模型进行座椅振动舒适度评估。

[516] 邱意想, 高泉龙. 一种微电机异音检测方法及装置[P]. 广东省:CN202410944209.7, 2024-10-11.

>根据SGE模块、Dropout层与**深度残差收缩网络**模型生成改进**深度残差收缩网络**模型，将训练数据集合与验证数据集合输入至改进**深度残差收缩网络**模型分别进行训练与调参操作，得到最终的异音检测模型，并进行声音信号的识别分类，得到最终的异音识别分类结果。

[517] 但果, 姜乃夫, 马锦婷, 等. 一种高密度表面肌电信号实时分解方法、系统及终端[P]. 广东省:CN202410648504.8, 2024-09-17.

>构建多标签**深度残差收缩网络**，根据所述离线数据集中的高密度表面肌电信号和对应的所述运动单元发放序列，对所述多标签**深度残差收缩网络**进行模型训练，得到分解模型。

[518] 汪小东, 杨紫佳, 方凯, 等. 多源数据融合的无人机林业遥感安全目标识别方法及系统[P]. 浙江省:CN202410584574.1, 2024-08-16.

>构建SC-RTDETR模型，用改进的**深度残差收缩网络DRSN**替换RTDETR网络中特征提取部分的Bottleneck模块。

[519] 尹柏强, 曾亚洪, 王若宇, 等. 基于深度迁移网络和模型融合的局部放电模式识别方法[P]. 安徽省:CN202410507300.2, 2024-08-13.

>S1：通过UHF传感器获取不同缺陷类型下局部放电的时域波形数据S(t)；S2：提取相应的数值化时序特征参数矢量；S3：搭建深度迁移学习**残差收缩网络**模型；S4：搭建一维改进深度残差网络的网络模型；S5：将局部放电的时序信号原始数据与特征参数矢量分别作为深度迁移学习**残差收缩网络**模型与一维改进深度残差网络模型的输入，使用Adam算法作为PD分类模型的优化算法，训练获得PD分类模型的最佳参数，使用Softmax函数输出局部放电类型判断结果。

[520] 吴永旭, 丁正建, 司乔瑞, 等. 一体化污水处理设备的鼓风搅拌淤泥智能控制系统[P]. 江苏省:CN202410687300.5, 2024-08-09.

>采用了基于**残差收缩模块**的DRN网络算法,采用多普勒双频超声波测量法所采集的淤泥各项参数,预测一体化污水处理设备好氧池中所需要的曝气搅拌频率和方向,从而控制鼓风机的工作功率和喷嘴的方向进行精确曝气这一过程。

[521] 高云鹏, 张其旺, 孟雪晴, 等. 一种球磨机负荷状态检测方法[P]. 湖南省:CN202210716493.3, 2024-06-28.

>预设的球磨机负荷状态检测模型包括依次连接的宽卷积神经网络、卷积层、N个**残差收缩网络**模块、池化层、全连接层和softmax分类器；且**残差收缩网络**模块的输入和输出融合之后作为其后一个模块或网络层的输入；所述宽卷积神经网络，包括依次连接的卷积层、批量归一化层、激活函数层和池化层；每个**残差收缩网络**模块包括依次连接的一个或多个卷积块；**残差收缩网络**模块中除最后一个卷积块外的其他卷积块，每个卷积块包括依次连接的卷积层、批量归一化层、激活函数层和池化层；**残差收缩网络**模块中最后一个卷积块包括一个卷积层CONV、一个注意力机制模块和一个软阈值模块...

[522] 李建强, 彭浩然. 眼底图像处理方法、装置、电子设备及存储介质[P]. 北京市:CN202111327342.0, 2024-06-21.

>所述两个特征向量分别输入至两个**残差收缩模块**，得到两个池化向量以及两个激活向量；其中，所述**残差收缩模块**包括全局平均池化层和第一激活层...

[523] 刘惠聪, 张华赢, 张宏钊, 等. 一种新能源配电台区的可开放容量需求预测方法及装置[P]. 广东省:CN202410283377.6, 2024-06-21.

>通过构建影响因素库、时间序列分解、LSTM模型预测与**深度残差收缩网络**处理等技术手段,实现对不同时间尺度下新能源配电台区可开放容量的准确预测。

[524] 魏广芬, 徐媛, 张薇, 等. 一种气体传感器漂移补偿方法[P]. 山东省:CN202410172049.9, 2024-06-14.

>构建图像融合的**残差收缩网络**分类模型，并进行模型训练，利用训练好的图像融合的**残差收缩网络**分类模型，进行气体传感器漂移数据的分类。

[525] 赵金亮, 李耀杰, 刘洋洲, 等. 一种基于图像识别的绿化方法[P]. 山西省:CN202410436135.6, 2024-06-11.

>获取目标绿化区域的遥感数据并输入**深度残差收缩网络**，得到实际生长指标。

[526] 吴军, 陈作懿, 李子睿, 等. 无故障样本下的工业机器人故障检测与定位方法、系统[P]. 湖北省:CN202211559797.X, 2024-06-04.

>采用**残差收缩网络**来消除隐藏在小波时频特征中的噪声特征，并提取有代表性的特征；构建特征样本对来揭示健康状态的独一属性和共有属性...

[527] 武瑛, 卢彭真. 基于深度学习和多无人机的桥梁结构动力特性识别方法[P]. 浙江省:CN202410068893.7, 2024-06-04.

>该数据集作为训练样例训练**深度残差收缩网络DRSN**；然后将原始视频帧输入训练好的**深度残差收缩网络DRSN**,以获得所有原始视频帧中桥梁的结构组件的语义分类掩码的预测值...

[528] 吕喆, 梁燕萍, 余立. DoA估计方法、装置、设备及介质[P]. 北京市:CN202211502534.5, 2024-05-28.

>将所述目标协方差矩阵进行第一数据预处理后，输入至**深度残差收缩网络**，获得直射LOS径波达方向DoA估计结果；将所述目标协方差矩阵进行第二数据预处理后，输入至卷积神经网络，获得非直射NLOS径DoA估计结果。

[529] 舒禹程,贺朝刚,乔丽红,等.一种振动系统的轻量化振动控制方法[P]. 重庆市:CN202410204171.X,2024-05-24.

>采用了**深度残差收缩网络**，以实现自适应去噪和轻量化的神经网络；同时，引入了多奖励机制，以协助轻量化网络找到接近最优的控制策略，并采用了优先级经验回放机制，以加速神经网络的收敛速度，提高数据利用效率。

[530] 李奇,王海龙,李响,等.一种质子交换膜燃料电池电化学阻抗谱在线测量方法[P]. 四川省:CN202410088043.3,2024-05-10.

>基于所得特征值，采用基于**残差收缩**的卷积神经网络进行水管理故障分类。

[531] 吕虎,陈蔚,郑毅隽.一种基于机器学习的全身麻醉药效预测方法及系统[P]. 上海市:CN202410122067.6,2024-04-26.

>本方案采用最优**深度残差收缩网络**进行特征提取，更有效地处理受噪声干扰的脑电信号，自动从中提取潜在特征，提高了后续的预测精度，有助于增强预测模型的鲁棒性。

[532] 梁培,张玉禄,贺云,等.一种基于CNN-CBAM收缩二分类网络的雷达信号处理方法[P]. 福建省:CN202410063831.7,2024-04-12.

>同时使用Shrink-Attention残差块构建**深度残差收缩网络**，既提高了网络的泛化能力，也保证了雷达信号数据处理的效率和准确度。

[533] 张辉,侯辰飞,徐向阳,等.一种面向多轴车辆轮毂电机的故障诊断方法[P]. 北京市:CN202311692345.3,2024-04-12.

>筛选出有利于故障诊断的特征参数，并采用**深度残差收缩块**对筛选后的振动信号进行降噪处理。最后将降噪后的训练集振动信号输入到**深度残差收缩**局部编码器网络DRSPAN中进行训练，并将训练好的DRSPAN模型用于未知的电机故障的诊断。

[534] 覃振权,张璇,卢炳先,等.一种基于多源迁移融合收缩框架的旋转机械故障诊断方法[P]. 辽宁省:CN202111363881.X,2024-04-09.

>用源域带标签样本对模型进行预训练，通过**深度残差收缩网络**结构处理高噪声数据，提取出高维特征并训练好模型的分类模块。

[535] 王海,彭一明,蔡英凤,等.一种面向高校校园的智能垃圾分类小车及分类方法[P]. 江苏省:CN202311561220.7,2024-04-09.

>算法上基于图像识别和**深度残差收缩网络**的垃圾分类，极大程度上提高垃圾种类识别的准确性

[536] 陈姬,王松聿,孙浩法,等.一种基于深度学习的多层单道焊焊缝尺寸预测方法及系统[P]. 山东省:CN202410233809.2,2024-04-05.

>以残差模块作为图像特征提取模块，以**残差收缩模块**作为电信号特征提取模块，对预测模型进行优化、训练以及验证。

[537] 张黄河,宋锐,武传艳.基于步态动态变化和足底压力的糖尿病智能诊断系统[P]. 山东省:CN202410193358.4,2024-04-02.

>将多维步态特征向量输入至**深度残差收缩网络**模型中，输出患者的糖尿病患病概率。

[538] 张文广,李浩瀚,曾卫东,等.一种基于工况判别的智能发电机组控制模型在线更新方法[P]. 北京市:CN202111593325.1,2024-03-19.

>构建包含50个隐藏层的**深度残差收缩网络**模型,随机初始化网络参数,设置最大迭代次数、批量训练样本个数等超参数；将归一化后的训练集输入**深度残差收缩网络**,前向传播计算输出值与实际值之间的误差

[539] 葛海彬,朱昱瑛,岳广臣,等.基于混合神经网络的电力变压器故障检测方法[P].黑龙江省:CN202311574893.6,2024-02-27.

>电力变压器故障检测网络采用LCNN模型实现，其残差模块包括一个输入层、一个卷积层、一定数量的**深度残差收缩模块**、一个批标准化、一个ReLU激活函数、一个全局均值池化和一个全连接输出层

[540] 王江涛,马浩然,张清,等.一种基于数据升维自适应区分加工模式的刀具监测方法及系统[P].上海市:CN202310534485.1,2024-01-30.

>将不同加工模式下的电流数据用**深度残差收缩网络**进行分类，用于判断刀具是否发生损坏；根据判断获得的整刀的磨损程度，给出刀具发生损坏的概率，并进行结果展示。

[541] 凌捷,林茂源,罗玉,等.一种基于注意力机制的恶意流量检测方法和系统[P].广东省:CN202111661242.1,2024-01-09.

>将预处理数据集输入到预先训练好的基于注意力机制的**深度残差收缩网络**，通过所述基于注意力机制的**深度残差收缩网络**对预处理数据集进行分类，获得待检测的流量数据集的恶意流量检测结果；步骤S3所述基于注意力机制的**深度残差收缩网络**通过结合**深度残差收缩网络**和长短期记忆网络进行构建得到；步骤S3所述基于注意力机制的**深度残差收缩网络**包括：**深度残差收缩网络**、长短期记忆网络、多层感知器、激活函数；基于注意力机制的**深度残差收缩网络**的输入数据分别经过**深度残差收缩网络**、长短期记忆网络得到各自的处理结果，然后对**深度残差收缩网络**的处理结果和长短期记忆网络的处理结果进行连接操作，对连接操作结果依次输入多层感知器和激活函数，得到是否为恶意流量的分类结果。

[542] 王慧慧,张新聚.基于CNN和Transformer联合的行星齿轮箱故障诊断方法[P].河北省:CN202311548546.6,2024-01-05.

>对采集到的一维行星齿轮箱振动信号进行数据预处理，构建**残差收缩**降噪模块，将预处理后的数据输入到**残差收缩网络**进行降噪，保存降噪后的特征数据...

[543] 郭方洪,陈晟琦,丁云,等.一种基于联邦迁移学习的供热管网失水诊断方法[P].浙江省:CN202311241448.8,2023-12-29.

>利用各参与方的相关性表达图样本集在**深度残差收缩网络**训练得到各参与方的本地模型。

[544] 张文广,周世豪,孟宪辉,等.基于多元统计分析的燃气轮机进口导叶系统故障诊断方法[P].北京市:CN202111112610.7,2023-12-26.

>通过**深度残差收缩网络**快速、精确的完成故障诊断。

[545] 王福运,刘哲,张贵元,等.一种LNG接收站低温潜液泵故障监测方法、系统及设备[P].北京市:CN202311164821.4,2023-12-12.

>所述故障识别模型是利用LNG接收站低温潜液泵标注后的历史振动信号，对**深度残差收缩网络**进行训练得到的；所述**深度残差收缩网络**是通过向卷积网络中每两个卷积层的输入和输出之间添加一条跳跃连接后得到的。

[546] 李凯,贾贤石,李洲,等.基于动态域对抗图卷积网络的机床刀具磨损状态预测方法[P].湖南省:CN202311431935.0,2023-12-12.

>设置多尺度深度残差收缩网络，将主轴振动子样本集信号输入多尺度**深度残差收缩网络**中提取与刀具磨损相关的敏感特征信号，构建刀具磨损图数据样本集。

[547] 俞嘉地,陈运忠,孔浩,等.基于RFID的语音感知方法[P].上海市:CN202311173181.3,2023-12-08.

>将预处理后的RF信号分别通过循环神经网络(RNN)、卷积循环神经网络(CRNN)和**深度残差收缩网络**(DRSN)提取得到面部运动、骨骼振动和空气振动特征...

[548] 伍栋文,樊友杰,俞林刚,等.窃电用户的识别方法及装置、存储介质、终端[P].江西省:CN202210461189.9,2023-11-10.

>所述窃电识别模型为基于完成扩充的用户样本数据集对**深度残差收缩网络**进行模型训练得到的。

[549] 闫戈,韩放,李钊阳,等.一种模拟电路故障诊断方法、系统及电子设备[P].北京市:CN202310887449.3,2023-11-10.

>最后采用基于**残差收缩网络**的故障诊断模型来识别模拟电路的工作状态，从而保障电子设备的可靠性和安全性。

[550] 于广增,张巧灵.基于多尺度小波阈值化网络的轴承故障诊断方法及系统[P].浙江省:CN202310738821.4,2023-11-03.

>利用**深度残差收缩网络**中软阈值化的结构与多尺度卷积小波分解模块结合可以实现多尺度小波分解和自适应滤波，有利于提升故障诊断的精度。

[551]李红涛,华缘,李皋,等.一种钻井液含油量和含气量在线智能监测方法及系统[P].四川省:CN202310925700.0,2023-10-24.

>通过**深度残差收缩网络**拟合出这些特征与钻井液含气量、含油量之间的关系，从而能实时地评估出水基钻井液中含气量与含油量分别所占的体积分数并通过监测系统用户交互模块进行在线查询与监测。

[552]王雷,赵晋平,于博,等.基于高空间分辨率遥感影像的畜牧业牲畜监测提取方法[P].北京市:CN202310739339.2,2023-09-19.

>将所述第一特征集以及所述第二特征集输入所述**残差收缩网络**模块，所述第一特征集以及所述第二特征集均包含多个特征数据，所述**残差收缩网络**模块用于去除所述特征数据中的无关参数信息。

[553] 方利梅,王柳婧,柴武君,等.用于卷烟设备的多信号融合故障检测方法、装置和介质[P].浙江省:CN202310606660.3,2023-09-15.

>将预转子振动数据输入至训转子预测**深度残差收缩网络**模型C1中，得到第一故障概率分布集合；将基座振动数据输入至基座预测**深度残差收缩网络**模型C2中，得到第二故障概率分布集合；将外壳振动数据输入至外壳预测**深度残差收缩网络**模型C3中，得到第三故障概率分布集合。

[554] 赵莹莹,何鎏璐.卷积神经网络和SVM的DAB变换器故障诊断方法及系统[P].浙江省:CN202310615957.6,2023-09-15.

>构建变换器故障诊断模型，通过**残差收缩模块**构建多个一维卷积神经网络，分别学习对应诊断信号的故障状态，并将故障状态学习结果输入至SVM中进行综合决策；将样本输入到故障诊断模型中进行训练和测试，利用训练好的模型对功率开关管开路故障进行诊断。结合**残差收缩模块**，构建基于卷积神经网络和SVM决策DAB变换器故障诊断模型，能够有效减少信号噪声对故障诊断准确度的影响。

[555] 王华勇,陈婧威,田贺,等.一种列车轴承状态诊断系统及方法[P].山东省:CN202310660400.4,2023-09-05.

>所述诊断模型是在**深度残差收缩网络**模型的基础上改进得到的，包括输入层、卷积层1、卷积层2、**残差收缩模块**1、残差项计算模块、软阈值化模块、池化层、**残差收缩模块**2、Dense层、输出层；所述**残差收缩模块**1包括GAP函数、FC函数、BN函数、Leaky ReLU激活函数和tanh函数；

[556] 宋爽,罗勇,张俊.基于半监督的CT影像合成方法、装置、设备及存储介质[P].湖北省:CN202310535204.4,2023-08-25.

>所述半监督生成对抗网络模型包括共用图像生成器和**残差收缩**判别器的有监督分支网络和无监督分支网络，所述**残差收缩**判别器包括多个通道级**残差收缩模块**和一卷积层；基于所述训练数据集对所述半监督生成对抗网络模型进行训练，以更新优化图像生成器和**残差收缩**判别器，生成图像合成模型；

[557] 牟宗磊,曹青浩,李丽,等.一种水面无人艇执行器故障诊断方法及系统[P].山东省:CN202310593508.6,2023-08-18.

>通过训练好的改进**深度残差收缩网络**对数据进行分析，判断水面无人艇执行器是否发生故障。

[558] 朱冬,方向明,宋雯,等.一种旋转机械剩余使用寿命预测方法、装置及终端设备[P].重庆市:CN202310418740.6,2023-08-18.

>方法包括基于**深度残差收缩网络**重构目标旋转机械的状态监测原始数据，获得HI数据；

[559] 卢安琪,陈圣兵,刘雨欣,等.一种基于注意力与集成学习机制的泵机设备故障检测方法[P].安徽省:CN202210828857.7,2023-08-04.

>对时域特征集利用时域注意力机制**残差收缩网络**训练，得到N个时域基学习器(TA1，TA2...TAn)；对频域特征集，利用通道域注意力机制**残差收缩网络**训练，得到M个通道域基学习器(CA1，CA2...CAn)；

>将基于时间域、通道域注意力机制的**残差收缩网络**作为基学习器并进行加权融合，有效解决了泵机设备故障检测问题，是人工智能与设备检测技术的巨大贡献。

[560] 傅质馨,周子浩,朱俊澎,等.一种噪声背景下基于振动信号的海上风电机组齿轮箱故障诊断方法[P].江苏省:CN202310312634.X,2023-06-27.

>将故障样本扩充原数据集送入构建好的**深度残差收缩网络**模型，通过**深度残差收缩网络**模型实现对振动信号的降噪以及分类，获取到故障诊断结果。

[561] 郑雨婷,吕文涛,余凯,等.一种织物瑕疵检测模型及训练方法、织物瑕疵检测方法[P].浙江省:CN202310276820.2,2023-06-23.

>第二卷积瓶颈层分别和冲突过滤**残差收缩模块**、第二融合瓶颈层相连，第三卷积瓶颈层分别和冲突过滤**残差收缩模块**、第一融合瓶颈层连接，空间金字塔快速池化模块和第一卷积块相连，第一卷积块经上采样后和第一融合卷积层相连；冲突过滤**残差收缩模块**分别和第三融合瓶颈层、第四融合瓶颈层相连

[562] 丁铿博,张妙月,赵曼,等.基于X射线衍射及ICP-MS的土壤纳米颗粒定量方法[P].广东省:CN202111410511.7,2023-06-20.

>基于**深度残差收缩网络**的方法，利用矿物PDF卡片和X射线衍射数据，获得不同矿物的元素特征；

[563] 张登银,张莹,冯莹莹,等.一种基于细节恢复的单幅图像去雾方法[P].江苏省:CN202310176162.X,2023-05-23.

>搭建实现图像细节恢复的细节恢复网络，引入**残差收缩模块**和空间注意力机制。

[564] 孙有朝,晏传奇,吴红兰,等.基于眼动数据评估飞行员对不同编码信息感知的方法与装置[P].江苏省:CN202211253086.X,2023-05-16.

>将灰度图像数据作为训练好的**深度残差收缩网络**模型的输入，得到评估结果。

[565] 冯奇,陈丽,刘芳.一种基于VAE-GAN的DSSS信号波形生成方法[P].河北省:CN202310120445.2,2023-05-12.

>模型中添加了自注意力机制和**深度残差收缩网络**使模型能够对具有不同长度扩频码的目标信号进行学习，模型灵活易训练，因此具有实际应用价值。

[566] 李庆生,龙家焕,张兆丰,等.一种结合持续学习更新的电力系统暂态稳定评估方法[P].贵州省:CN202211529046.3,2023-04-14.

>利用**深度残差收缩网络**建立特征输入与稳定结果输出之间的映射关系，从而实现端到端的暂态稳定评估；

[567] 林涛,吉萌萌.一种基于改进TCN的空气污染物浓度预测方法[P].天津市:CN202011558387.4,2023-04-07.

>构建**残差收缩网络**，**残差收缩网络**由串联的j个**残差收缩网络块**构成，一个**残差收缩网络块**包括l个**残差收缩块**，l个**残差收缩块**依次串联构成一个**残差收缩网络块**，每一个**残差收缩块**均包含一个空洞因果卷积模块和**残差收缩**路径模块，将空洞因果卷积模块的输入和**残差收缩**路径模块的输出进行跳跃连接，得到该**残差收缩块**的输出；第一个**残差收缩块**的输入为步骤2.2中的一维全卷积层的输出C(X-σ)，最后一个**残差收缩块**的输入为倒数第二个**残差收缩块**的输出，最后一个**残差收缩块**的输出为**残差收缩网络**块的输出；

[568] 熊盛武,王丹.一种基于短语音的声纹识别方法[P].湖北省:CN202110696040.4,2023-03-24.

>帧级特征提取网络为一种改进的残差网络(ResNet)—**深度残差收缩网络(DRSN)**，该网络在ResNet基础上加入软阈值化作为收缩层，用于去除冗余信息；

[569] 胡昊,马鑫,郑野,等.一种基于深度残差网络下的变压器油中气体故障识别方法[P].河南省:CN202111093886.5,2023-03-24.

>利用半软阈值函数替换掉共通道**深度残差收缩网络**中的软阈值，得到子通道阈值**深度残差收缩网络**；最后，利用子通道阈值**深度残差收缩网络**分别对训练集和测试集进行训练和测试...

[570] 高军峰,赵佳,张冰洋,等.一种基于增强雷达波信号的定位方法、毫米波雷达、装置[P].湖北省:CN202211430352.1,2023-03-10.

>利用训练完成的**深度残差收缩网络**和恒虚警检测方法，对所述点云数据进行检测和多普勒过滤，并确定一个或多个目标；

[571] 孟苓辉,周振威,时林林,等.电子电路间歇故障诊断方法、装置、系统和计算机设备[P].广东省:CN202211396042.2,2023-03-07.

>故障深度分析诊断模型采用历史电子电路故障状态特征数据和历史状态预警数据对**深度残差收缩神经网络**进行训练得到。

[572] 孟苓辉,周振威,卢冠兰,等.牵引变流器故障诊断方法、装置、计算机设备和存储介质[P].广东省:CN202211395520.8,2023-03-07.

>将目标特征数据输入**深度残差收缩网络**模型进行故障预测，得到第一故障预测结果...

[573] 陈龙淼,李明,王满意,等.一种永磁同步电机不平衡样本匝间短路故障诊断方法[P].江苏省:CN202210988049.7,2023-02-03.

>利用同步电机仿真数据训练**深度残差收缩网络**，通过生成对抗网络对真实数据样本进行扩张，采用训练好的**深度残差收缩网络**实现电机匝间短路故障的分类。

[574] 陈磊,陈蔚,全永兵.噪音识别的方法、装置、电子设备及介质[P].广东省:CN202110687656.5,2023-01-06.

>从而避免相关技术中存在的仅具备单一斜率的**深度残差收缩网络**所出现的去噪效果不明显的问题。

[575] 张必银,周倩文,刘玖周.一种小样本图像分类方法及系统[P].湖北省:CN202111434831.6,2023-01-03.

>将小样本图像输入至**深度残差收缩网络**中，获取小样本图像的特征向量；根据所述小样本图像的特征向量对小样本图像进行分类；其中，**深度残差收缩网络**为深度残差网络、注意力机制和软阈值函数集成的网络；训练**深度残差收缩网络**时，采用筛选出的若干基类的特征向量对新类的特征向量进行校准，获取新类的特征向量。

[576] 陈磊,张明扬,陈蔚,等.一种故障检测方法及装置、家电、计算机存储介质[P].广东省:CN202110640044.0,2022-12-09.

>利用压缩后的**深度残差收缩网络**处理所述输入信号，以输出分类结果；其中,所述压缩后的**深度残差收缩网络**包括第一残差单元和第二残差单元...

[577] 冯志珍,闫宗奎,高明亮,等.螺钉数量检测方法、装置、设备和存储介质[P].山东省:CN202210942670.X,2022-11-22.

>通过**深度残差收缩模型**对所述输入图像进行螺钉识别，得到带有螺钉标记的输出图像；

[578] 胥泽龙,秦瑾,蒋永录,等.一种基于通信调度指令的语音识别的智能系统及方法[P].甘肃省:CN202210829783.9,2022-11-08.

>利用**深度残差收缩网络DRSN**-CS对语音数据进行降噪或者冗余信息处理。

[579] 张宇军,于艳,孙兴洪,等.一种基于图像识别的扒渣机控制方法和系统[P].上海市:CN202110354364.X,2022-10-14.

>构建并训练改进的**深度残差收缩网络**，用以将每一个子区域的渣面积输入到改进的**深度残差收缩网络**中，所述改进的**深度残差收缩网络**输出最优扒渣路径；

[580] 程广河,王星星,袁慧苗,等.一种应用于计算机视觉的软阈值注意力机制[P].山东省:CN202210692398.4,2022-09-13.

>借鉴**深度残差收缩网络**的思想，使用同时考虑通道和位置信息的CA注意力机制来代替SENet与软阈值化方法结合，提出一种新的软阈值注意力模块...

[581] 孙有朝,毛浩英,李龙彪.一种航空发动机故障风险预警方法及系统[P].江苏省:CN202210607401.8,2022-09-06.

>故障风险预警模型为根据待训练航空发动机的灰度图和故障类型对改进**深度残差收缩网络**进行训练得到的；改进**深度残差收缩网络**包括依次连接的LSTM、深度残差卷积收缩模块和全连接层；

[582] 张飞,付合英,郝斌,等.语音识别模型及其训练方法、语音识别方法及装置[P].内蒙古自治区:CN202210643822.6,2022-09-06.

>将**深度残差收缩网络**和门控卷积网络引入到电网调度语音识别中，通过**深度残差收缩网络**中的收缩模块移除阈值区域的冗余信息来提高卷积神经网络特征提取能力，通过门控卷积网络捕获有效上下文。

[583] 翟江涛,许历隆,林鹏,等.一种基于多模块融合的加密流量分类方法[P].江苏省:CN202111580226.X,2022-08-30.

>步骤4：构建**残差收缩模块**；步骤5：通过自注意力机制模块从原始流量数据灰度图中提取特征信息，通过**残差收缩模块**对所提取特征自适应滤除冗余特征，全局平均池化降维特征信息，输出分类结果；步骤6：将所述训练集输入**深度残差收缩网络**模型中训练深度学习模型，对加密流量分类。

[584] 年睿,钱玉琪,何波,等.拖曳式传感器阵列多维时间序列自编码器去噪方法[P].山东省:CN202210311897.4,2022-07-15.

>将其生成器的卷积神经网络替换为**深度残差收缩网络**，实现对高低阈值噪声去除的目的；通过引入**残差收缩网络**，改进的**残差收缩网络**适合于各个样本中噪声含量不同的情况，适用于去除阈值内的噪声信号；

[585] 胡昊,马鑫,郑野,等.基于深度残差网络下的变压器油中气体复合成像识别方法[P].河南省:CN202111095213.3,2022-06-07.

>利用交叉方向乘子和FISTA算法对共通道**深度残差收缩网络**中的软阈值优化目标函数进行优化，得到子通道阈值**深度残差收缩网络**；最后，利用子通道阈值**深度残差收缩网络**分别对训练集和测试集进行训练和测试。

[586] 徐欣,张尹,纪卓捷,等.一种基于特征通道融合和深度学习的癫痫预测系统[P].江苏省:CN202210216836.X,2022-06-03.

>搭建逐通道不同阈值的**深度残差收缩神经网络**作为分类器，采用网络的软阈值去噪和注意力机制,使用生成的样本特征完成分类器的训练；

[587] 舒明雷,王海生,田岚,等.一种心电信号的质量评估方法[P].山东省:CN202110322895.0,2022-04-22.

>**残差收缩网络**能够将数据中存在的很多与当前任务无关的原始信息通过软阈值处理删除掉，获得与当前任务最相关的信息。卷积神经网络具有参数共享和稀疏连接的优点，能够将**残差收缩网络**提取出的深度特征进一步提纯优化，获得最适合当前任务的深度特征。

[588] 汤会增,张孝远,张利,等.GIL机械故障诊断模型的构造方法及其应用、计算机可读介质、故障诊断系统[P].河南省:CN202111509009.1,2022-04-15.

>构建**深度残差收缩网络**初始模型，使用训练集样本训练**深度残差收缩网络**初始模型，得到用于诊断GIL第一类机械故障的GIL机械故障诊断模型；

[589] 朱韶平,朱乐平,邱小群,等.一种基于大数据的工业设备亚健康状态智能监测方法及其装置[P].广东省:CN202111423582.0,2022-03-01.

>展开基于**深度残差收缩网络**的亚健康状态识别模型研究，并与主流机器学习和集成学习算法进行性能比较...

[590] 杨蒲,耿慧琳,柳鹏.一种基于深度学习的航空发动机转子系统故障诊断算法[P].江苏省:CN202111237432.0,2022-01-21.

>设置Pytorch下的新型**深度残差收缩网络**故障诊断模型，并使用训练集进行故障诊断模型的训练，该网络使用Adam优化算法，由首层宽卷积层和数个**残差收缩模块**以及全连接层、Softmax分类器组成，最后通过Softmax分类器输出故障分类结果，新型**深度残差收缩网络**故障诊断模型的结构参数如下...

[591] 伍海华,孙科,瞿翊.一种语音识别方法及系统[P].上海市:CN202111170413.0,2022-01-04.

>利用预设**深度残差收缩网络**模型中的**深度残差收缩网络**去除原始语音频谱所包含的无关特征，使得在强噪声环境下得到无噪声等特征的文本信息，提高在强噪声环境下对语音信号的识别率。

[592] 高崇,康忠建,张祥海,等.一种基于频谱共振的自适应脉动水力压裂技术[P].山东省:CN202111226245.2,2021-12-10.

>基于自适应模态经验分解、神经**残差收缩网络**算法等理论测定目标储层固有频率；

[593] 陶来发, 郝杰, 苏铉元, 等. 一种基于关联图网络的供电系统级故障关联增强认知与诊断[P]. 北京市:CN202110884231.3, 2021-11-23.

>依据**深度残差收缩网络**算法进行供电系统故障诊断。

[594] 宋清昆, 李伟龙. 一种基于深度学习的滚动轴承故障诊断方法[P]. 黑龙江省:CN202110541690.1, 2021-08-10.

>基于**深度残差收缩网络**的故障诊断方法：在对样本进行分类的时候，样本中不可避免地会有一些噪声，更广义地讲，样本中包含着与当前分类任务无关的信息，这些信息理解为噪声；

[595] 王璐. 一种锁扣丢失故障检测方法、系统及装置[P]. 黑龙江省:CN202011390378.9, 2021-07-16.

>将提取出的特征输入训练好的改进**深度残差收缩网络**，通过训练好的改进**深度残差收缩网络**输出锁扣部件的位置信息和类别信息；所述改进**深度残差收缩网络**包括残差网络模块、软阈值模块和注意力机制模块。

[596] 常俊, 张力, 黄彬, 等. 基于WiFi信道状态信息的室内入侵检测方法及系统[P]. 云南省:CN202110308772.1, 2021-06-25.

>利用**深度残差收缩网络**对相位信息进行特征提取与训练，对模型参数进行优化；

[597] 汪鑫奕, 杨博, 刘琦, 等. 一种三电平逆变器IGBT开路故障诊断方法[P]. 上海市:CN202011170214.5, 2021-05-04.

>步骤4：构建阈值独立的残差模块和**深度残差收缩网络**；步骤5：训练所述**深度残差收缩网络**；

[598] 王英龙, 石京京, 舒明雷, 等. 一种心电图异常信号中的房颤信号自动检测方法[P]. 山东省:CN202011544301.2, 2021-04-20.

>将图像匹配相对应的数据标注信息，标注后的图像用作**深度残差收缩网络**的输入，将图像加载到**深度残差收缩网络**的卷积层,对图像进行卷积处理；

[599] 崔良中, 孙佳杰, 牛雅萌. 基于类别增量学习的自动调制识别方法[J/OL]. 海军工程大学学报, 1-9[2024-12-11].

>针对这一挑战，提出了一种基于类别增量学习的自动调制识别技术，即使用**深度残差收缩网络**作为特征提取器，利用一种动态扩充网络模型的方法，对保存的部分旧调制信号和新调制信号进行类别的增量学习，以适应动态环境下的自动调制识别。

>利用一维**深度残差收缩网络**作为特征提取器对调制信号进行自适应降噪并进行有效的特征提取...

[600] 赵文翔, 普运伟. 一种改进生成对抗网络的遥感图像去云方法[J]. 遥感信息, 2024, 39(05): 78-85.

>网络的生成器主要结构为**深度残差收缩网络**，可以更好地去除噪声，并将生成器网络中的批归一化更换为组归一化以提高模型训练效率；

>生成器引入了**深度残差收缩网络**，具有更好的特征提取能力和噪声抑制能力，这使得该模型在处理含噪声数据时能够更好地提取有用特征，同时抑制噪声干扰，从而获得更好的去云效果。

>通过引入软阈值函数，**深度残差收缩网络**能够更好地处理具有噪声或复杂性的数据，从而提高模型的性能和泛化能力。在深度残差网络的基础上，**深度残差收缩网络**进一步引入了一个小型子网络。子网络学习得到阈值，对特征图通道进行软阈值化，实现特征选择。卷积层赋予重要特征较大值、冗余特征较小值。子网络阈值区分这两种特征，软阈值化剔除冗余特征，保留重要特征。

>本研究通过结合**深度残差收缩网络**并将批归一化更换为组归一化来构建光学遥感图像去云模型...

>对于SSIM指标，分别增加了0.03、0.01和0.01,说明引入**深度残差收缩网络**可以有效提升模型的去云性能。

>使用以**深度残差收缩网络**作为主要结构的生成器对于含噪声数据具有较好的处理结果，生成的图像在PSNR和SSIM两个评价指标方面均得到更好的结果，展现出更好的图像效果质量，同时具有更高的去云效率。

[601] 宋文歌. 基于注意力残差深度网络的滚动轴承故障诊断方法研究[J]. 机械设计, 2024, 41(06): 67-72.

>**残差收缩块**通过挤压激励结构对输入特征自适应设置阈值，之后再通过软阈值函数对系数小于阈值的特征进行删除，使ADRN在训练中具有抵抗噪声、去除冗余信息的功能。

[602] 林楠, 唐凯鹏, 牛勇鹏, 等. 基于双阶段特征提取网络的ECG降噪分类算法[J]. 郑州大学学报(工学版), 2024, 45(05): 61-68.

>本文针对心电信号中同时含有时空特征的特点，对**残差收缩网络**模块进行了改进，并以其来提取信号中的空间特征，使用LSTM与注意力模块结合来提取信号中的时间特征，提出了一个端到端的自动降噪分类模型。

>在空间特征提取阶段，由深度耦合软阈值化去噪方法的**残差收缩网络**从输入的12导联标准心电信号中提取空间特征；

>本文采用改进的**深度残差收缩网络**将数据预处理阶段中的降噪处理与空间特征提取阶段耦合...

>本文所提出的基于改进的**残差收缩网络**的深度学习模型在两个指标上均优于其他参考模型。

[603] 赵铁柱, 梁校伦, 杨秋鸿, 等. 基于异质信息对齐和重排序的跨模态行人重识别方法[J]. 山东科技大学学报(自然科学版), 2024, 43(02): 79-89.

>本研究还采用**残差收缩模块**(residual shrinkage building unit, RSBU)提取行人特征，减少行人特征受图像噪声的影响，增加行人特征的鲁棒性。

>从本质上讲，**残差收缩模块**是由残差模块、压缩与激励模块(squeeze-and-excitation module)和软阈值化函数的集成。首先，压缩与激励模块通过Sigmoid函数将全连接层的输出值缩放至0~1范围内;将缩放后的全连接层输出值乘以每个通道平均池化后的值，以自适应的方式学习到每个通道的软阈值τ;将经过软阈值化的特征值与原本的特征值相加，得到新的特征。

[604] 刘媛媛, 程双全, 朱路, 等. 多尺度关键信息融合的轻量级图像超分辨重建[J]. 光电子·激光, 2024, 35(11): 1145-1154.

>本文引用**残差收缩模型**的理论，对其进行改进和优化，构建KIEM，KIEM可以去除更多的冗余信息，使网络充分关注到关键信息达到提升性能的目的，且网络模型更小。

[605] 杨靛青, 毛艳萍. 基于改进深度学习的航拍滑坡检测方法[J]. 计算机工程与设计, 2024, 45(01): 268-274.

>为及时发现滑坡险情展开应急救援，提出一种结合逐通道不同阈值的**深度残差收缩网络**(DRSN-CW)方法的更快速区域卷积神经网络(Faster-RCNN)模型的航拍图像滑坡检测算法。

>**深度残差收缩网络**将软阈值作为收缩层引入残差网络中，借助注意力机制，根据各特征图的特点自适应地设置不同的阈值，形成一种有效消除无关特征信息以及噪声的方式。

[606] 古天龙, 张清智, 李晶晶. 基于时-频注意力机制网络的水声目标线谱增强[J]. 电子与信息学报, 2024, 46(01): 92-100.

>频率注意力机制通过将**深度残差收缩网络**中收缩子网络的全链接层设计为1维卷积层，增加了模型在频域的注意力。

>频域注意力机制模块采用了改进的**深度残差收缩网络**，其由多个堆叠的**深度残差收缩模块**组成，每个**残差收缩模块**在传统**残差收缩模块**的基础上，将收缩子网络中的全链接层设计为1维卷积层，使频域注意力阈值可以更加精准地区分线谱和噪声。

[607] 朱乐文, 田兴, 李宪华. 基于ISAM-Drsnet的故障识别模型及其应用[J]. 机电工程, 2024, 41(02): 216-225+270.

>针对滚动轴承故障诊断时网络模型在复杂环境下有效特征提取困难，无法充分挖掘具有周期性的滚动轴承故障数据时序特征的问题，提出了一种基于改进条纹注意力机制与**深度残差收缩网络**的滚动轴承故障诊断模型(ISAM-Drsnet)。

>该**残差收缩单元(residual shrinkage building units，RSBU) **包含了残差网络的特点，并将软阈值引入到该单元中，即构成了**深度残差收缩网络**结构模型的基本单元。

[608] 张浩, 高树辉. 基于高光谱技术的现场车漆物证识别模型研究[J]. 分析测试学报, 2023, 42(07): 817-824.

>本文提出了一种结合高光谱成像和**深度残差收缩网络**（DRSN）快速无损鉴别白色车漆品牌的新方法。该方法融合了注意力机制和软阈值化降噪算法，可去除数据中的噪声并保留残差网络的性能，以98.6%的准确率区分了18种来自不同品牌或型号的白色车漆样本，分类效果显著高于SVM、RF和LR与1D-CNN。

>该文基于光谱检测可无损成像、操作简单的优点，探索了高光谱成像技术结合**深度残差收缩网络**识别现场车漆物证的方法。

>结合高光谱数据的特点，建立了针对性的一维**深度残差收缩网络**（1D-DRSN）识别模型。

>该完整的**深度残差收缩网络**模型结构依次是输入层、卷积层、残差收缩模块、拉伸层、全连接层输出，模块的优势在于实现了数据去噪并保留了残差网络性能，提升了高光谱数据的分类效果。

[609] 杨晓岗, 夏涛. 基于多尺度融合模型的化工故障诊断[J]. 电子测量技术, 2023, 46(13): 8-16.

>该方法将注意力机制分别与软阈值方法和多尺度学习相结合，构建了多尺度**深度残差收缩网络**....

>本文提出了一种基于MDRSN-BIGRU融合模型的故障诊断方法，该方法引入**残差收缩结构**与多尺度卷积核，将注意力机制与软阈值相结合，在提取高维多尺度空间特征的同时自适应的将注意力集中到更加有用的特征信息上，以达到增强有效信息，减弱噪声信息的目的。

[610] 刘云鹏, 来庭煜, 刘嘉硕, 等. 特高压直流换流阀饱和电抗器振动声纹特性与松动程度声纹检测方法[J]. 电工技术学报, 2023, 38(05): 1375-1389.

>该文提出一种基于优化S变换和改进**深度残差收缩网络**的饱和电抗器铁心松动程度声纹识别模型。

>最后采用五个不同方位测点的铁心松动数据代入基于自适应参数修正线性单元的改进**深度残差收缩网络**中进行训练，来消除声纹图中的冗余信息，并对不同松动程度下的特征进行独立映射，从而增强共同特征的学习能力。

[611] 黄志静, 邵慕义, 张庭瑞, 等. 基于深度学习的野生动物识别[J]. 电子测试, 2022, 36(22): 69-71+10.

>运用深度学习技术对野生动物的图像进行识别，并且为了降低噪声信息的干扰及提高野生动物图像识别的准确率，提出了基于**深度残差收缩网络**的野生动物识别模型。

>将**深度残差收缩网络**与深度残差网络模型对相同野生动物数据集进行训练作对比，同时对部分野生动物图像进行了测试。实验结果表明，**深度残差收缩网络**提高野生动物图像识别准确率。

[612] 林涛, 吉萌萌, 付崇阁, 等. 基于改进时间卷积网络的空气质量预测研究[J]. 计算机仿真, 2022, 39(10): 451-456+501.

>利用**深度残差收缩网络**中特殊注意力机制和软阈值化的思想对TCN中的残差模块进行了改进，解决了因输入样本中的冗余信息不同导致的重要信息权重分散问题。

[613] 周晔, 章坚武, 程继承. 面向复杂声学环境的伪装语音检测[J]. 传感技术学报, 2022, 35(10): 1355-1362.

>针对以上问题，提出了一种基于**深度残差收缩网络(Deep Residual Shrinkage Networks, DRSN)**的多特征联合语音欺骗检测方法，首先**DRSN**利用基于深度注意力机制的自适应阈值学习模块和软阈值模块提高了在复杂声学环境下的特征学习能力...

[614] 刘芯志, 彭成, 满君丰, 等. 改进残差结构的轻量级故障诊断方法[J]. 计算机工程与设计, 2022, 43(08): 2303-2310.

>改进**深度残差收缩模块**，提高模型复杂噪声场景的鲁棒性。

>在**深度残差收缩结构**中，全局平均池化层会忽略大量有效的局部或长距离依赖空间信息，在信息丢失的情况下，再使用全连接层将各个通道的空间信息组合不能进一步提升软阙值的效果。

>改进**深度残差收缩模块**，设计空间信息增强模块代替原有的全局平均池化层，提高模型噪声环境下的鲁棒性。

[615] 邹文骏, 曹张保, 杨力战. 基于信息物理系统的电压不平衡度及电能质量分析预警方法研究[J]. 城市轨道交通研究, 2022, 25(07): 70-73+79.

>将专家经验法及**深度残差收缩网络**法相结合得到合理阈值，并提出了三相电压不平衡度的预警方案。

>将专家经验法和**深度残差收缩网络**法相结合，可实现主客观结合，让专家经验法在机器学习输出阈值的基础上，调整至更为合理的阈值，从而实现高精度的报警。

[616] 张晓锋, 郝如江, 段泽森, 等. 基于改进残差网络的齿轮箱故障诊断研究[J]. 国防交通工程与技术, 2022, 20(03): 35-37+34.

>**残差收缩模块**(RSNB)利用注意力机制根据重要程度不同来对特征进行加权，自动地给各个样本设置不同的阈值，在降噪的同时最大程度的保护数据的原始特征。

[617] 张晓锋, 郝如江, 程旺, 等. 多尺度特征融合与改进ResNet结合的齿轮箱故障诊断研究[J]. 机械科学与技术, 2023, 42(10): 1699-1704.

>将注意力机制与软阈值化加入到网络中构建**残差收缩模块(RSNB)**，针对在工业环境下会产生噪声等干扰因素这一问题，在网络中设置自适应阈值块，根据噪声的不同强度自适应生成阈值，该模块使网络获得良好的降噪效果。

[618] 赵迪, 王呈. 基于改进胶囊网络的运维知识库故障分类方法[J]. 电子测量与仪器学报, 2022, 36(05): 104-112.

>针对运维图像存在的多噪声问题，引入**深度残差收缩网络**(deep residual shrinkage networks, DRSN)提高模型在含噪声数据上的特征提取效果。

>模型首先通过**深度残差收缩模块**替代经典胶囊网络单一卷积结构实现图像深层特征的提取，利用自适应阈值的结构对无效特征进行过滤，增强模型抗噪声干扰能力。

[619] 徐成霞, 阎庆, 李腾, 等. 基于联合注意力机制的单幅图像去雨算法[J]. 计算机应用, 2022, 42(08): 2578-2585.

>引入**深度残差收缩网络**，以利用残差模块中嵌入的软阈值非线性变换子网络来通过软阈值函数将冗余信息置零，从而提升CNN在噪声中保留图像细节的能力。

[620] 刘亚, 刘可, 黄庆安, 等. 基于视频深度学习的小鼠恐惧情绪识别与分析方法研究[J]. 生命科学仪器, 2021, 19(04): 37-44.

>本文引入了**深度残差收缩网络**模型来降低图像噪声对小鼠分割的影响。**深度残差收缩网络**具有三个基本模块：软阈值化、残差网络、SENet通道注意力机制。

>本文引入的**深度残差收缩网络**模块在残差网络基础上引入了一个小型子网络。该子网络首先对输入特征图内的所有元素取绝对值。在U-Net网络的下采样层中，嵌入了**深度残差收缩网络**模块...

[621] 刘云峰, 杨晋彪, 韩晋锋, 等. 基于边缘增强生成对抗网络的电力设备热成像超分辨率重建[J]. 电力建设, 2021, 42(07): 83-89.

>该网络在超分辨率生成对抗网络(super-resolution generative adversarial networks, SRGAN)的基础上新增了**深度残差收缩网络**模块，在降低图像噪声的基础上，提高了训练的稳定性。

>增加**残差收缩网络**(residual shrinkage network，RSN) 模块，并提取边缘特征进行加强训练，以获得更好的重建效果，最后利用红外图像数据集对所提方法进行验证。

[622] 史宝岱, 张秦, 李瑶, 等. 基于改进残差注意力网络的SAR图像目标识别[J]. 激光与光电子学进展, 2021, 58(08): 114-122.

>首先分析了对网络添加注意力机制的必要性，接着在残差注意力网络中引入**残差收缩块**，从识别率和参数量的角度进行实验分析。

[623] 孙瑶, 姜千一, 王志坚, 等. 一种三相鼠笼式异步电机转子断条小样本故障诊断方法[P]. 北京市:CN202411221230.0, 2024-12-10.

>首先采用改进**残差收缩网络**对于电流及振动数据滤除噪声分量，提高少量可利用训练样本的参考价值，提取更多有效特征；其次采用密集连接机制连接每个**残差收缩模块**，实现特征重用以避免**残差收缩模块**滤除有效信息；

[624] 缪金, 张涛, 陈静静, 等. 一种GIS局部放电类型识别方法、装置、终端及介质[P]. 江苏省:CN202411235257.5, 2024-12-10.

>利用所述样本集对构建的**深度残差收缩网络DRSN**识别模型进行训练，并以SLoss损失函数最小为目标对模型的网络参数进行优化；

[625] Zhang C, Luo S, Cao S, et al. Evaluating Pilot Mental Workload Using fNIRS-Based Functional Connectivity Features with a **Deep Residual Shrinkage Network** Under Emergency Flight Scenarios[J]. International Journal of Human–Computer Interaction, 2024, 1-16.

[626] Li X, Wang J, Wang J, et al. The research of digital twin models for CNC spindle systems based on **deep residual shrinkage network**[C]. In Journal of Physics: Conference Series, 2024, vol. 2921, no. 1, p. 012023).

[627] 任文娟,秦子竣,杨战鹏,等.雷达工作状态识别方法、装置、设备、介质和程序产品[P].北京市:CN202410445752.2,2024-09-10.

>将目标关联特征输入两级**残差收缩网络**，得到脉冲序列的语义特征。将语义特征输入双向门循环控制单元，确定雷达工作状态。

>两级**残差收缩网络**是将两个**残差收缩网络**进行级联，第一个**残差收缩网络**的输出为第二个**残差收缩网络**的输入。对关联特征进行预卷积可以得到目标关联特征，将目标关联特征输入两级**残差收缩网络**，可以得到脉冲序列的语义特征。两级**残差收缩网络**中的每个**残差收缩网络**均包括残差块结构、批正则化模块和空间注意力模块。

[628] 潘广旭,宫池玉,裴丽伟,等.一种基于机器学习的非侵入式负荷监测与辨识方法及系统[P].山东省:CN202410464817.8,2024-09-06.

>引入**残差收缩网络**以提取负荷数据的特征并进行相似性或相异性的判断，将负荷数据输入到**残差收缩网络**中，通过网络的前向传播过程，提取负荷数据的特征表示；所述**残差收缩网络**为预训练好的残差网络，且网络引入收缩机制提取负荷数据中隐藏的高阶特征，**残差收缩网络**利用自身的层次结构，通过多层的非线性变换来增强特征的表达能力，刻画负荷数据中的复杂模式和规律；

[629] 仁庆道尔吉,卢颖,李雷孝,等.一种基于预训练模型和Transformer的蒙古语多模态情感分析方法[P].内蒙古自治区:CN202410485956.9,2024-08-16.

>对蒙古语音频数据进行分帧，并采用**深度残差收缩网络**获得语音情感特征；

>提取蒙古语音频数据的梅尔频谱系数，输入到**深度残差收缩网络**模型中，所述**深度残差收缩网络**通过堆叠多个残差块，提取和融合音频特征序列，得到整个音频序列的高级特征信息，即为语音情感特征。

>本步骤的**深度残差收缩网络**主要由深度残差网络、注意力机制和软阙值函数三部分组成，是一种利用注意力机制和软阈值函数去除数据中噪声的深度神经网络。**DRSN**使用的自注意力机制在消除无效特征和噪声的同时选择相关特征，从而提升了深度神经网络从噪声数据中提取有价值特征的能力。

[630] 杨玉欢.一种非侵入式负荷检测与分解方法、装置及存储介质[P].四川省:CN202311515833.7,2024-02-23.

>基于**深度残差收缩网络**根据所述暂态数据集提取暂态特征，并对所述稳态特征和所述暂态特征进行采样及拼接，得到融合特征，根据所述融合特征计算相似度生成第一用电设备及其状态识别结果集；

[631] 邹复好,李开,甘早斌,等.一种电子鼻气体识别方法、系统、电子设备及存储介质[P].湖北省:CN202110772874.9,2024-02-20.

>所述预设气体识别网络包括**残差收缩网络**、全局特征提取网络和分类器；所述残差收缩网络，用于提取每一个第二时间子序列数据的多个分支特征；

[632] 梁栋, 沈冠宇, 张亚蓉, 等. 一种基于Lamb波的复合材料板结构抗噪损伤分类方法[P]. 江苏省: CN202311113802.9, 2024-01-05.

>加入**深度残差收缩网络**结构，利用**残差收缩网络**的软阈值化特点结合注意力机制实现对含噪数据的处理。

>在网络结构中嵌入**残差收缩网络**模块，在基础网络架构上加入软阈值函数，可以有效的消除噪声对信号损伤特征提取时造成的影响；

[633] 赖国书, 黄春竹, 黄天富, 等. 一种关口计量装置运行状态辨识方法、系统、设备及介质[P]. 福建省: CN202311089567.6, 2023-09-19.

>本实施例所构建的**深度残差收缩网络**模型结构如图3所示。**深度残差收缩网络**堆叠了一定数量的自适应阈值残差收缩单元（RSBU‑CW），卷积层（Conv），批标准化（BN），激活函数（ReLU），全局平均池化(GAP)，全连接层(FC)等，网络自适应学习样本特征，通过软阈值化减小噪声对当前任务的影响。

[634] 章昕亮, 李天昀, 龚佩, 等. 联合深度神经网络和专家先验特征的信号调制识别方法及系统[P]. 河南省: CN202210095595.8, 2023-08-18.

>在卷积网络CNN中，利用通道共享阈值的**残差收缩网络**，将**残差收缩网络**中残差块单元输入与输出的特征向量相加，经过批量归一化层的归一化操作和ReLu激活函数处理后作为**残差收缩网络**中下一个残差块单元的输入，利用**残差收缩网络**来捕捉输入的信号特征；**残差收缩网络**中残差块单元利用软阈值化子神经网络来自动调制用于消除噪声的阈值...

[635] 孟苓辉, 谢锦阳, 陈义强, 等. 故障诊断方法、装置、计算机设备和存储介质[P]. 广东省: CN202310120357.2, 2023-06-02.

>通过**深度残差收缩网络**，根据所述时频域特征中各维度子特征对故障分析的贡献度，对所述时频域特征进行解析，得到所述电子电路的第一诊断结果；

[636] 韩慧慧, 王坚. 一种工业加工过程中内胆附着力质量预测方法和系统[P]. 上海市: CN202110535227.6, 2022-10-25.

>将所述静态产品质量数据集中的有标签数据送入**深度残差收缩网络**中，提取特征，并运用分类器对内胆附着力进行二分类评估，得到初步训练的**深度残差收缩网络**；

>将带有伪标签的动态数据和有标签的静态数据送入初步训练的**深度残差收缩网络**中，进一步训练**深度残差收缩网络**，得到最优的内胆附着力产品质量预测**深度残差收缩网络**模型。

[637] 赵转莉, 李景丽, 袁英, 等. 一种基于物联网技术的教学用实验平台[P]. 河南省: CN202210843170.0, 2022-10-11.

>基于CNN‑PSO‑**残差收缩网络**算法的图像预测模型对所述程序流程图进行识别，得到图像识别结果；

[638] 任广振, 赵深, 曹俊平, 等. 一种电缆故障诊断方法、系统及可读存储介质[P]. 浙江省: CN202210653681.6, 2022-09-27.

>将灰度图导入**深度残差收缩网络**中的卷积层进行卷积计算，得到第一特征图；

[639] 章昕亮, 李天昀, 龚佩, 等.联合深度神经网络和专家先验特征的信号调制识别方法及系统[P].河南省:CN202210095595.8,2022-04-29.

>利用通道共享阈值的**残差收缩网络**，将**残差收缩网络**中残差块单元输入与输出的特征向量相加，经过批量归一化层的归一化操作和ReLu激活函数处理后作为**残差收缩网络**中下一个残差块单元的输入，利用**残差收缩网络**来捕捉输入的信号特征。

[640] 董绍江, 刘娟, 方鹏. 一种基于MES的刀具磨损检测方法及其系统[P].重庆市:CN202111536697.0,2022-04-05.

>建立基于强噪声下**深度残差收缩网络**的刀具磨损状态识别模块，对深度残差网络进行优化，在模型中加入软阈值化函数，构建基于软阈值化的**深度残差收缩网络**，让深度训练模型在处理数据时自适应去掉信号中的噪声成分...

[641] 郝明,王东辉.一种岩性识别方法及系统[P].四川省:CN202011611215.9,2021-05-07.

>对岩石数据集进行归一化处理，把岩石数据样本的元素含量的取值归一化，输入进训练完毕的**残差收缩网络**将地层岩石数据样本的岩性进行分类。

[642] 王昀, 李铎, 张岩, 等. 消极服务评价的确定方法及装置[P]. 河北省: CN202111296073.6, 2023-05-09.

>将人脸表情数据集Fer2013输入**深度残差收缩网络**进行训练，将训练后的**深度残差收缩网络**作为所述表情识别模型。

[643] 蔡华闽,陈昌金,乐晋昆,等.一种机床故障诊断及展示方法、装置、设备及存储介质[P].四川省:CN202211354750.X,2023-05-05.

>所述目标故障元模式识别模型为采用故障元数据集结合**深度残差收缩网络**模型建立的识别模型；

[644] 饶云江,吴明埝,刘杰,等.基于深度学习的光纤光栅传感系统降噪方法及其相关设备[P].江苏省:CN202111556911.9,2023-04-07.

>基于深度学习的光纤光栅传感系统降噪方法，其特征在于，所述**残差收缩单元**包括三个**残差收缩网络**，每个**残差收缩网络**的工作原理描述为...

[645] 吕国华,池强,王西艳,等.基于自监督和小样本学习的跨域高光谱图像分类方法[P].山东省:CN202210720249.4,2022-09-06.

>构建的深度神经网络由输入层、映射层、**深度残差收缩网络**、软标签学习网络、自监督学习网络、小样本分类网络、无监督域适应模块以及分类器组成；

>**深度残差收缩网络**用于提取输入的映射后的高光谱图像数据的光谱空间特征并完成分类预测，其中，**深度残差收缩网络**由特征提取器和分类层构成，该三维的**残差收缩网络**是在残差网络的基础上加入收缩模块...

[646] 冯晶,胡鹏,刘娟.一种单导联心电异常信号识别方法[P].湖北省:CN202110517995.9,2021-07-30.

>搭建通道间共享阈值的**深度残差收缩网络**DRSN‑CS模型，通过预设数量的通道间共享阈值的**残差收缩模块**RSBU‑CS进行堆叠，削减噪声相关的特征；

[647] 冀爽,张明,王磊,等.基于CNN-SVM的配网设备红外图像识别方法和系统[P].吉林省:CN202410933760.1,2024-11-12.

>利用**深度残差收缩网络**对特征数据进行软阈值化处理，使每个特征都能生成其独立的阈值；

>在特征经过一连串的卷积处理后，当它们抵达**深度残差收缩网络**时，会分流为两条处理路径。

[648] 陈雪勤,赵玉琪.一种基于频域F比分析的语音情感识别方法及系统[P].江苏省:CN202411398278.9,2024-11-08.

>针对高鉴别频段部署**深度残差收缩网络**模型进行情感特征的分析包括：所述**深度残差收缩网络**模型是在深度残差网络的基础上增加注意力机制，并将软阈值化作为非线性层引入，对所有输入特征取平均值后，经过全局平均池化层将每个通道的特征图转换为一个标量；

[649] 徐荣.扁线电机定子表面缺陷检测方法、装置、设备及存储介质[P].江苏省:CN202410805742.5,2024-10-18.

>依据所述历史扁线电机定子表面图像数据训练一个**深度残差收缩网络**，所述**深度残差收缩网络**包含多个残差模块，每个模块内部集成自适应软阈值函数...

>选择**深度残差收缩网络**（DRSN）作为噪声识别和抑制的模型；

[650] 高德欣,杜玉蓉,杨清,等.基于机器视觉的全自动BLDC电机绕线机产品缺陷检测方法[P].山东省:CN202111611195.X,2024-09-13.

>将Resblock‑body中的ResNet(残差网络)模块替换为DRSN(**残差收缩网络**)模块。**残差收缩网络**为深度学习+软阈值化+注意力机制，其中软阈值化是信号降噪算法的核心步骤...

[651] 李鹏, 林俊强, 刘毅, 等. 一种水利水电工程多维安全调度方案辅助智能决策方法[P]. 北京市:CN202410395223.6, 2024-07-05.

>采用基于交叉熵损失权重的**深度残差收缩网络**作为实体图像的特征提取器，随后利用正交投影矩阵法获取基于实体的图像特征...

[652] 马宇恒,张华坤,李可瑞,等.一种用于矿用卡车的故障处理设备及处理方法[P].福建省:CN202311840904.0,2024-04-26.

>采用**深度残差收缩网络**来滤波得到有效数据，并且使用了软阈值化来消除与噪声相关的特征；将软阈值化作为非线性层嵌入到残差构建模块之中...

[653] 郭洪飞,任亚平,何智慧,等.一种基于动力电池循环老化衰退决策主动再制造时域的方法[P].广东省:CN202311594059.3,2024-04-19.

>构建**深度残差收缩网络**对动力电池单体性能参数数据进行提取；

>**深度残差收缩网络**包括残差模块、软阈值函数和注意力机制，其中，软阈值函数用于对数据进行降噪处理

[654] 殷正凌,邹修国,赵中豪,等.一种平养鸡舍黄羽鸡多目标跟踪方法[P].江苏省:CN202110793190.7,2024-03-12.

>所述MobileNetV2中Inverted residual模块与**深度残差收缩网络**相结合组成DRSN－Inverted residual模块...

>**深度残差收缩网络**(DRSN)解决了当样本中含有噪声，或者与标签无关的冗余信息时，深度学习算法的效果会有所降低这一问题。**深度残差收缩网络**集成了深度残差网络、软阈值化和注意力机制。软阈值化将绝对值小于某个阈值的特征删除，将绝对值大于这个阈值的特征朝着零的方向进行收缩...

>在引入**深度残差收缩网络**之后，模型的各个精度指标均有所提升，同时，检测速度方面仅有5.93％的损失，不影响检测的实时性。

[655] 刘楚雄,宋亮,代秀琼,等.语音拒识方法、装置、电子设备及存储介质[P].重庆市:CN202311277225.7,2023-12-22.

>利用**深度残差收缩网络**对该条语音进行降噪、滤波和去除无用信息的处理，其中，所述**深度残差收缩网络**已通过基于深度学习的训练，能对语音进行降噪、滤波和去除无用信息的处理；

[656] 吴克河,李天慧,梁迪昌.一种基于混合深度学习的网络流量异常检测方法[P].北京市:CN202310722345.7,2023-09-15.

>将所提取的数据送入**残差收缩网络**中进行学习，该网络的残差结构和软阈值化机制能够更有效减少对噪声及其相关特性的影响，解决梯度退化与过拟合问题，挖掘网络流量特征；

>所述DRSN‑BiLSTM模型构造方法，其特征在于，在**残差收缩网络**之前再加入注意力层，增加流量特征提取的能力，从而有效获取更关键的特征

[657] 周学武,康珮珮,邓中翰,等.辐射源个体信息识别方法、装置、电子设备和介质[P].北京市:CN202211041677.0,2022-11-25.

>将上述样本的第一信号域集输入至**深度残差收缩网络**模型的信号加噪模块，得到加噪后的第一信号域集，作为第三信号域集。其中，**深度残差收缩网络**(Deep Residual Shrinkage Network，DRSN)模型包括信号加噪模块、残差收缩滤波模块和全连接降维模块。

>将上述第四信号域集输入至**深度残差收缩网络**模型的全连接降维模块，得到降维之后的第四信号域集。

[658] 李颖,匡慈维,徐勇.一种真实复杂场景图像超分辨率的模型训练方法及装置[P].广东省:CN202210675580.9,2022-10-18.

>提出了基于**残差收缩网络**与密集连接的超分辨率模型，具有泛化性强、应用广泛的特点，可应用于多种真实场景下的自然图像超分。

[659]陶冠宏,吴文兵.一种基于多源频谱特征的风机轴承故障智能诊断方法[P].四川省:CN202210493501.2,2022-08-12.

>利用训练集训练**深度残差收缩网络**，获取故障诊断模型，再通过验证集对故障诊断模型进行调整；

>本方法采用**深度残差收缩网络**训练数据，该模型可以自适应信号降噪，同时有效提取数据深层特征...

[660] 葛磊蛟,李京京.知-智融合协同的微电网群两阶段主动应急自愈学习方法[P].天津市:CN202410853309.9,2024-11-08.

>基于耦合不确定性及时空信息、微网高精度信息等的数据驱动，结合**深度残差收缩网络**和深度对抗神经网络，提出一种深度融合神经网络自主辨识算法；

>构建**深度残差收缩网络**(Deep  Residual  Shrinkage  Network，DRSN)的**残差收缩模块**(Residual  Shrinkage  Building  Unit，RSBU)；

[661] 石争浩,李成建,尤珍臻,等.数据再平衡损失指导的轻量级时频融合信号分类方法[P].陕西省:CN202410220339.6,2024-06-21.

>特征提取模块包括**深度残差收缩网络**DRSNs、多尺度时通融合注意力MTCA和多层卷积+ReLU模块CRL；

>时间序列z通过**深度残差收缩网络**DRSNs处理自适应降噪获得去噪后信号

>该模块包括**深度残差收缩网络**(DRSNs)、多尺度时通注意力模块(MTCA)(如图2(a)所示)和两层卷积(Conv1D)+归一化(BN)+ReLU模块(CBL)组成。其中，**深度残差收缩网络**(DRSNs)负责动态去噪。

[662] 王福运,刘哲,张贵元,等.一种用于LNG接收站的BOG压缩机组状态监测的系统和方法[P].北京市:CN202311538628.2,2024-03-19.

>设置一种**深度残差收缩网络**模型，首先对LNG接收站BOG压缩机组进行长达数月的数据采集工作...

>由于神经网络具有较强的拟合能力，因此软件会将报警后的异常数据进行随机打散，然后将此数据集作为一种**深度残差收缩网络**模型的输入层进行训练，最后输出分类结果，并展示在软件平台上，完成故障诊断。

[663] 肖幸鑫,张志勇,孙丰诚,等.一种变工况下滚动轴承故障诊断方法及相关组件[P].浙江省:CN202311478195.6,2024-02-06.

>网络结构包含特征提取层(**深度残差收缩网络**)，域分类层以及全连接分类层...

[664] 陈晓霞,李国平,吴梓源,等.一种工业叶片的故障检测方法、系统及装置[P].广东省:CN202311463401.6,2024-01-30.

>对所述时域特征利用时域注意力机制的**残差收缩网络**进行训练，得到时域基学习器；

[665] 王海,柳彦伊,张敏,等.基于小波变换和多模态特征融合的自动调制分类方法[P].陕西省:CN202310587426.0,2023-09-12.

>在原始的**深度残差收缩网络**中，使用离散小波变换DWT替换其中的池化层和跨步卷积层，得到图像模态特征提取网络；

>使用二维离散小波变换代替**深度残差收缩网络**中的平均池化层和跨步卷积层，以抑制图像中的噪声对模型分类性能的影响。

[666] 石争浩,李成建,尤珍臻,等.基于时频信息融合注意力的生理信号片段分析方法[P].陕西省:CN202310556580.1,2023-08-08.

>特征提取模块包括**深度残差收缩网络**DRSNs、多尺度卷积注意力MSCA和多层卷积+ReLU模块CRL；

>首先，通过**深度残差收缩网络**(DRSNs)进行自适应降噪；

[667] 陆超文,吴海玲.一种基于猪只声音的猪只健康预警方法及系统[P].四川省:CN202111087024.1,2023-03-17.

>使用**深度残差收缩网络**过滤噪声，提取有用的特征信息，解决传统音频分类因为模型音频的噪音多和模型的结构简单导致的判断不准确的结果。

[668] 王继晨,赵巨峰,崔光茫,等.口腔检测装置、口腔图像处理方法及系统[P].浙江省:CN202210396035.6,2022-07-15.

>将样本图像输入至**深度残差收缩网络**中，由**深度残差收缩网络**中的特征提取网络对所述样本图像进行特征提取，并由分类器基于所提取的特征进行类型预测，获得预测结果；

[669] 魏日令,徐晓刚,王军,等.基于混合高斯模型的脉搏波身份认证方法、装置和介质[P].浙江省:CN202210090684.3,2022-03-01.

>在时域特征提取中，采用以**深度残差收缩网络**为主干网络加TDNN网络的结构；在频域特征提取中，采用**深度残差收缩网络**和LSTM的网络结构；

[670] 李孟凡,张夏,班世豪,等.基于首层宽卷积核深度残差网络的输电线路短路故障诊断方法[P].湖北省:CN202011016531.1,2020-12-25.

>**深度残差收缩网络**GAP层中的高维数据经过t-SNE方法处理后的二维空间投影如图...

>这表明**深度残差收缩网络**DRSN可以应用于输电线路短路故障识别，其注意力机制下的软阈值化特点，在输电线路短路故障识别的精度、稳定性及抗噪能力等方面有着突出的优势。

[671] 刘铜玉,王文家,陆守香.故障电弧检测方法、装置、设备以及存储介质[P].安徽省:CN202411250683.6,2024-12-03.

>本申请预设的故障电弧检测模型可以理解为**深度残差收缩网络**模型，本申请通过**深度残差收缩网络**模型对联合特征向量进行训练和故障识别。且**深度残差收缩网络**模型是一种结合了残差网络和注意力机制的深度学习模型，能够在保持模型深度的同时减少噪声对特征提取的影响。其主要特点是通过残差连接和收缩函数有效地抑制噪声，并提高故障检测的精度。

>本申请的联合特征向量经过**深度残差收缩网络**模型检测分类之后对于低压配电系统的串联型故障电弧有着很好的检测效果。

[672] 邓建辉,张晶晶,彭辉,等.一种电源的故障智能监测方法、装置及设备[P].北京市:CN202410373802.0,2024-08-09.

>该智能监测模型是基于**深度残差收缩网络**建立...，还引入了通过引入软阈值化，能够去除信号中的冗余信息，更好地实现信号特征的提取和学习。总的来说，**深度残差收缩网络**中引入了注意力机制，通过软阈值和跨层恒等映射等方式来关注输入数据中的重要信息，抑制冗余信息，提高网络的表达能力和性能。

[673] 岳高峰,李文武,王淑敏,等.一种设计理性知识网络的知识融合方法、装置及存储介质[P].北京市:CN202311475638.6,2024-01-30.

>将所述目标技术文献中同一文档结构或者不同文档结构中的知识节点根据**深度残差收缩网络**的预设规则，将相同含义或者相近含义的知识节点进行合并；

>采用基于文档结构按照**深度残差收缩网络**（DRSN，Deep Residual Networks）知识融合规则对设计意图信息、设计论证信息、设计方案信息或备选方案信息等相同的实体和关系的进行合并，消除知识冗余，消除二义性。

[674] 王雷,陈铖,于博,等.目标提取方法、装置、电子设备及存储介质[P].北京市:CN202310930932.5,2023-10-17.

>将所述第一特征集以及所述第二特征集输入**残差收缩网络**模块，以增强模型的优化能力。

[675] 李惠军,刘正方.基于振动和声音数据的融合诊断方法、系统、设备及介质[P].广东省:CN202310821548.1,2023-08-04.

>需要说明的是，预设的故障诊断模型为**深度残差收缩网络**模型，包含输入层、卷积层、一系列的基本模块以及全局均值池化和全连接输出层，其中，基本模块是通过一个小型子网络。

>故障诊断设备将8段电变压器正常运行的历史信号分别输入8个**深度残差收缩网络**模型中...

>电变压器外壳上设置有一个监测点，则对该监测点设置一个**残差收缩网络**模型...

[676] 阳建宏,罗泽超,黎敏,等.基于5G三轴温振一体技术的轧机早期故障监测与诊断系统[P].北京市:CN202210768980.4,2022-11-04.

>通过深度学习算法中的**深度残差收缩网络**对数据进行降噪处理。

>针对故障信号早期微弱问题，通过**深度残差收缩网络**对数据进行降噪处理，有效消除噪声信息，获得更准确的故障特征，帮助实现轧机运行状态的预警和故障识别。

[677] 郭健,孙瑜,蔡云飞,等.一种果树田垄的识别方法及电子设备[P].江苏省:CN202210711029.5,2022-09-16.

>通过**深度残差收缩网络**进行特征值的提取，**深度残差收缩网络**的全连接输出层为分类器，进行果树、田垄分类识别。

[678] 李文淮,丁鹏,陈澍,等.核反应堆故障分类方法、装置、计算机设备以及存储介质[P].广东省:CN202111653107.2,2022-04-15.

>通过预设故障分类模型中的**深度残差收缩网络**中进行深度学习，将能够根据状态估计矩阵中多维度的状态数据有效识别出状态故障分类结果以及状态故障分类结果对应的置信度，从而实现初步的故障分类诊断。

>**深度残差收缩网络**相较于普通的深度学习方法的优势主要在于：更加适合含噪声数据的特征提取。因为**深度残差收缩网络**在其结构中采用了软阈值化作为非线性层，是信号降噪的核心步骤，相当于将降噪集成进了深度神经网络中，将其作为可训练的步骤。

[679] 裴凤雀,林耀杰,蒋锐锐,等.一种车间设备多模态数据融合的故障诊断方法[P].江苏省:CN202411165562.1,2024-11-22.

>通过引入多尺度组卷积的思想，改进了**深度残差收缩网络**DRSN，使之在故障信号类别差异较大时，实现较好的多模态信号特征提取及降噪效果。

[680] 刘尧,方磊,焦点,等.一种旋转机械无监督域适应故障诊断方法及系统[P].陕西省:CN202410740301.1,2024-09-27.

>其中时域编码器和频域编码器采用**深度残差收缩网络**作为网络结构，时域投影头和频域投影头采用一维卷积神经网络作为网络结构。

>分别对源域和目标域拼接融合由**深度残差收缩网络**提取的时域、频域特征。

[681] 胡肇洋.智能型解说音轨生成方法、装置、设备以及存储介质[P].北京市:CN202410577708.7,2024-07-23.

>所述场景关键词提取模型是采用场景关键词提取数据集对**深度残差收缩网络**模型进行训练得到的...

[682] 陈瀚,许奇功,倪文书,等.一种面向高噪声人脸识别方法及装置[P].福建省:CN202311753305.5,2024-04-19.

>通过将**深度残差收缩网络**和通道注意力机制融合，先应用深度残差网络和软阈值去噪网络对待识别图像进行特征提取以及去噪，再应用通道注意力对特征通道进行特征加权，能够在过亮、过暗或其他特殊复杂环境中获取待识别图像中有效的人脸特征，极大提高了特殊复杂环境中的人脸识别准确率，从而减少了模型的误判率，提升用户体验。

[683] 吴红兰,李瑞航,孙有朝.一种基于语音情感的飞行员工作负荷实时评估方法[P].江苏省:CN202310488480.X,2023-10-27.

>采用**深度残差收缩网络**计算音频差分倒谱特征权重；

>先计算倒谱特征的一阶和二阶差分形成3个通道的特征集，引入**深度残差收缩网络**获得二维网络3个通道的权重，再将倒谱特征输入。

[684] 许杨俊,赵亮,惠小东,等.基于多源数据的变电智能网关设备状态检测方法及装置[P].广东省:CN202310531726.7,2023-09-08.

>状态检测模型采用**深度残差收缩网络**搭建，该状态检测模型包括一个输入层、一个卷积层、一定数量的**残差收缩模块**、一个批标准化、一个ReLU激活函数、一个全局均值池化和一个全连接输出层。其中，**残差收缩模块**为通道间共享阈值的**残差收缩模块**(RSBU‑CS)，替换了深度残差网络中普通的残差构建模块。而一定数量的**残差收缩模块**被堆叠起来，从而噪声相关的特征被逐渐削减。最后通过全局均值池化层和全连接输出层处理后输出得到初始检测结果。

[685] 李超,殷光强,杨钊贤,等.一种基于跨级特征增强的目标馕的识别及计数方法[P].四川省:CN202210505926.0,2023-05-30.

>所述深层网络采用**残差收缩网络**，采用注意力机制，自适应调整网络激活函数阈值τ，当输入小于τ时输出为0，大于τ时输出值为输入‑τ。

>并跨级连接至经过**深度残差收缩网络**提取特征后的特征网络，以提高对馕产业中馕细小差异的识别准确度和计数速度。

[686] 庄园,王轩,曹晓祥,等.一种融合滤波网络的车辆位置估测方法及计算机可读介质[P].湖北省:CN202310068343.0,2023-05-09.

>本方法提出一种基于**深度残差收缩网络**的虚拟里程计用于替代传统的轮速里程计，降低了该方案的使用要求。

>基于**深度残差收缩网络**的虚拟里程计用于替代传统的轮速里程计，通过设置软硬阈值、注意力机制和恒等路径，该网络在训练过程中实现自动软阈值化，自适应地学习消除噪声和冗余信息，对于处理这种包含噪声样本的速度估计具有明显优势。

[687] 蔡赛华,陈锦富,林薇,等.一种基于改进的时间卷积网络的漏洞检测方法[P].江苏省:CN202111257188.4,2022-02-18.

>构建基于**深度残差收缩网络**DRSN的时间卷积网络TCN_DRSN，在时间卷积网络的残差块中添加DRSN中的通道阈值学习模块，用于学习每个通道对应的阈值...

[688] 张东晓,陈云天,李健,等.一种测井数据降噪方法、装置、计算机设备和存储介质[P].广东省:CN202410676009.8,2024-11-19.

>图2中的结构是在传统的**深度残差收缩网络**的基础上做出的改进...

>该模型的训练与传统的**深度残差收缩网络**、多头注意力机制的训练方式类似。

[689] 陈杰,张朝琛,马克,等.一种基于视觉基础模型的SAR图像舰船分割方法及系统[P].安徽省:CN202411441463.1,2024-11-15.

>所述自适应小波软阈值模块基于**深度残差收缩网络**，利用注意力机制自动获取软阈值，结合离散小波变换，对分解后不同频率范围的特征子带分别实施软阈值去噪处理。

[690] 张焱,吴嘉明,张万成,等.一种针对接收机迁移问题的射频指纹识别方法[P].北京市:CN202410741593.0,2024-10-15.

>设计的神经网络基于**深度残差收缩网络**，在其中嵌入高斯编码器以获得射频指纹的深度隐藏特征...

>在**深度残差收缩网络**后加入我们设计的高斯编码器，之后再连接两个分类器，其中接收机分类器前加入梯度反转层。

[691] 朱胜阳,巫江,张庆铼,等.一种用于浮置板轨道钢弹簧的损伤检测方法及系统[P].四川省:CN202410547220.X,2024-08-16.

>基于**深度残差收缩网络**构建所述钢弹簧损伤检测模型。

>在一些实施例中，可以基于**深度残差收缩网络** (Deep Residual Shrinkage Network，DRSN)构建钢弹簧损伤检测模型。

[692] 徐涛,林俊强,刘毅,等.一种基于知识图谱嵌入式的水利工程风险智能调控方法[P].北京市:CN202410395220.2,2024-07-05.

>采用**深度残差收缩网络**对图像数据进行处理，该模型在Imagenet3基础之上完成预训练

[693] 周国伟,杨杰,邹晖,等.电抗器故障检测方法、装置、电子设备和存储介质[P].浙江省:CN202311572085.6,2024-02-23.

>所述故障识别模型包括输入层、卷积层、**残差收缩单元**、批标准化层、自适应参数修正线性单元、全局平均池化层和全连接层；

>了提高类内相同特征、类间差异特征的学习能力，将注意力机制下的激活函数APReLu嵌入到**深度残差收缩网络**中，通过深度学习自适应获取合适的权值，改善同类信号原始特征投影后的聚类效果。

>**残差收缩单元**采用软阈值函数去噪。其根据通道间阈值是否共享，分为阈值独立型和阈值共享型两种结构。

[694] 林琳,何文辉,付松,等.基于特征扩增的航空发动机故障诊断方法[P].黑龙江省:CN202310018871.5,2023-04-28.

>所述故障诊断网络为卷积神经网络CNN、长短期记忆网络LSTM、时间卷积网络TCN或**深度残差收缩网络**DRSN‑CW。

[695] 李品逸,刘嘉超,刘孟绅,等.模型训练方法、图像识别方法、装置、设备及存储介质[P].广东省:CN202111257914.2,2022-01-04.

>所述对属于同种类别的样本图像执行第二特征提取操作，可以是利用卷积神经网络、深度残差网络、**深度残差收缩网络**、前向反馈网络、霍普菲尔网、逆图像网络、AlexNet网络、vgg网络、googlenet网络、resnet网络等可以提取图像特征的一种或多种网络...

[696] 杨洋.产品宣传人工智能检测系统及方法[P].江苏省:CN202011413481.0,2021-11-02.

>还可以采用**深度残差收缩网络**（Deep  Residual  Shrinkage  Network，DRSN）来替换深度残差网络。**深度残差收缩网络**是一种人工智能算法，其实是深度残差网络（Deep Residual Network，ResNet）的新型改进，将软阈值化作为非线性层引入ResNet的网络结构之中，其目的是提高深度学习方法在含噪声数据或复杂数据上的特征学习效果。更具体的话，**深度残差收缩网络**的原型可认为来自于Squeeze‑and‑Excitation Network（SENet），本质上就是将SENet中各个特征通道的加权替换成了各个特征通道的软阈值化。

[697] 陈名亮,陈书楷,杨奇.一种金属分类方法、装置、设备及存储介质[P].福建省:CN202110797634.4,2021-10-22.

>所述金属分类模型的中间层可以为多个**残差收缩模块**RSBU‑CS构成，**残差收缩模块**RSBU‑CS可以为**深度残差收缩网络**中的残差收缩层，是一个通道间共享阈值的残差模块，英文名为Residual Shrinkage Building Unit with Channel‑Shared thresholds，简称RSBU‑CS。相比于传统的**残差收缩模块**，RSBU‑CS残差模块里多了一个小型的子网络，这个子网络可以自适应地设置阈值。

[698] 李广垒,陈祖涛.一种基于语音识别及转写技术的实时字幕上屏直播系统[P].安徽省:CN202110297837.7,2021-07-02.

> 语音消噪模块中的**深度残差收缩网络**通过自适应阈值的软阈值化层，自动消除与当前任务无关的信息，进行强噪数据的准确识别，并消除掉强噪音，强噪音被消除后即得到被消除噪音的语音信息。

[699] 张诗雨,赵乐乐.心电信号处理方法、装置、计算机设备及存储介质[P].上海市:CN202111051663.2,2024-09-24.

>神经网络模型可以为卷积神经网络模型、多层感知器、**残差收缩网络**模型等等...

[700] 张可,李烽,刘潇逸,等.一种基于电力系统网络的硬件故障分析方法及应用服务器[P].江苏省:CN202410397691.7,2024-06-21.

>对上一步骤的非时序的特征使用带有回馈机制的**深度残差收缩网络**拟合，通过多个BatchNorm的Relu卷积层叠加...

>其中的**深度残差收缩网络**融合了深度残差网络、SENet和软阈值函数，将重新加权替换成为阈值软化，在小型网络中获取权值系数作为数据融合的权值。

[701] 李依珂.恶意应用检测方法、装置、设备及存储介质[P].山东省:CN202311758372.6,2024-03-19.

>所述安全敏感数据特征提取网络是循环神经网络，所述流量特征提取网络是**深度残差收缩网络**。

[702] 冯宇杨,谢志清.一种智能报警系统[P].广东省:CN202210736525.6,2023-12-22.

>所述深度学习软件包括卷积神经网络、残差网络和**残差收缩网络**...

[703] 李天桢,高世伟,党小超,等.一种基于CNN-LKA的稀疏图注意力软测量建模方法[P].甘肃省:CN202311283491.0,2023-12-12.

>使用测试集对训练好的遮蔽卷积注意力**残差收缩网络**模型进行评估。

[704] 马少立,李桂民,曹磊.一种复杂声场环境中机器设备故障诊断系统[P].广东省:CN202311071545.7,2023-11-24.

>采用**深度残差收缩网络**作为分类器模型，并在模型基础上引入注意力机制和软阈值，不仅适用于故障声音数据样本较少的情况，同时可以进一步实现降噪功能。

[705] 朱志亮,张维通,闫正兵,等.一种工业机器人轴承故障边缘检测方法及系统[P].浙江省:CN202310822385.9,2023-10-13.

>首先，将滚动轴承数据集作为源域数据送入基于**深度残差收缩网络**所构建的轴承故障诊断模型进行预训练...

[706] 李玥,雷晓龙,刘晓燕,等.一种基于多维度信号分析的泵机异常工况在线检测方法[P].四川省:CN202310550154.7,2023-07-28.

>对时域特征集利用时域注意力机制**残差收缩网络**训练，得到N个时域基学习器；对频域特征集，利用通道域注意力机制**残差收缩网络**训练，得到M个通道域基学习器...

[707] 张玉楼.一种配置边缘服务器中神经网络模型的系统及装置[P].广东省:CN202110738374.3,2022-12-30.

>神经网络模型包括但不限于多层感知机神经网络模型、卷积神经网络模型、循环神经网络模型以及**残差收缩网络**等。其中，**残差收缩网络**是卷积神经网络模型的改进...

[708] 金耀,李知强,王俊博,等.结构健康监测信号压缩采样方法及装置[P].北京市:CN202210791350.9,2022-11-01.

>引入基于**深度残差收缩网络**构建的预训练诊断分类模型，在对所述信号数据集进行分类之前进行数据截断，得到特征提取模型；

[709] 张秀再,邱野.一种行人目标检测方法、系统、装置及存储介质[P].江苏省:CN202210709260.0,2022-09-23.

>所述行人目标检测模型包括**深度残差收缩模块**，所述**深度残差收缩模块**由软阈值函数、D‑SE注意力机制和残差模块结合构成；

>在行人目标检测模型的特征提取模块中加入**深度残差收缩模块**，将软阈值函数、D‑SE注意力机制和残差模块相结合，以增强有用特征信道，削弱冗余特征信道，提高检测的精确度；

[710] 杨蒲,耿慧琳,文琛万.一种基于残差网络的滚动轴承跨领域故障诊断算法[P].江苏省:CN202210525367.X,2022-07-29.

>将验证集输入到训练好的**深度残差收缩网络**模型中，识别测试样本的故障类型；

[711] 杨京礼,高天宇,姜守达.一种基于SDRSN的多特征健康因子融合方法[P].黑龙江省:CN202011606166.X,2022-07-29.

>**深度残差收缩网络**借鉴了压缩激励网络的子网络结构，以实现注意力机制下的软阈值化。

[712] 周祥全,蔡海军,陈盛福,等.目标图像的获取方法、存储介质和电子设备[P].广东省:CN202111679948.0,2022-04-12.

>目标图像结构中可以但不限于包括神经网络模型，如卷积神经网络、**残差收缩网络**、生成对抗网络等；

[713] 尤志翔,冯伟,孙铭蔚.一种基于ShrinkNet3D网络的特征分类图像处理方法及系统[P].浙江省:CN202111476632.1,2022-04-08.

>所述**残差收缩模块**用于将不重要特征经软阈值函数置零，并控制加强神经网络对保留的重要特征经含有噪声的信号提取有用特征；

[714] 丁荣军,张大勇,关照议,等.一种电机故障诊断方法、装置及相关组件[P].湖南省:CN202011096051.0,2021-01-29.

>本步骤以提取到的故障特征及转速信息作为电机故障诊断分类器的输入向量，将这些数据输入到DRSN(Deep Residual Shrinkage Network，**深度残差收缩网络**)诊断模型中进行诊断并输出故障诊断结果。

[715] 周泓,赵保中,李翔,等.一种行为树驱动虚拟人的控制方法[P].江苏省:CN202310940537.5,2024-12-06.

>本发明提出的一种基于改进**深度残差收缩网络**的轴承故障诊断方法，与现有技术相比较，其具有以下有益效果...

[716] 朱世杰,王英伟,冯月丽,等.一种基于遗传-神经网络的水平井生产动态预测方法[P].北京市:CN202310641946.5,2024-12-03.

>引入用于提高不同油藏参数下模型的鲁棒性的软阈值技术，建立**深度残差收缩网络**，创建一套适用于不同参数在不同条件下的鲁棒性较强且克服网络退化的油气生产预测技术。

[717] 陈杜煜.对象识别方法、装置、电子设备及存储介质[P].广东省:CN202210072098.6,2024-11-29.

>一神经网络可以包括卷积神经网络、深度残差网络、**深度残差收缩网络**、前向反馈网络、霍普菲尔网络、逆图像网络、AlexNet网络、vgg网络、googlenet网络、resnet网络等用于提取目标图像的特征的一种或多种网络...

[718] 李波,孔爱祥,勇妍,等.车牌号码重识别方法、装置、计算机设备及存储介质[P].北京市:CN202111011764.7,2024-11-12.

>本实施例中的神经网络模型包括但不限于卷积神经网络、**残差收缩网络**、多层感知机、玻尔兹曼机等网络模型。

[719] 王晓明,夏丽雯,刘林芽,等.一种基于改进BP神经网络的轨道病害监测方法及系统[P].江西省:CN202411266682.0,2024-10-18.

>在本步骤中，构建**残差收缩网络**（Residual Shrinkage Networks，RSN）...

[720] 邵杰,蔡田田,李肖博,等.低压配电网串联电弧故障检测方法、装置、设备和介质[P].广东省:CN202410588034.0,2024-09-13.

>针对连续小波变换得到的时频图特征设计了**深度残差收缩网络**的电弧故障检测模型。

[721] Yang T, Tang T, Wang J, et al. A novel cross-domain fault diagnosis method based on model agnostic meta-learning. Measurement, 2022, 199, p.111564.

>Meanwhile, the training strategy of MAML is optimized to adapt to the cross-domain problem, and the **residual shrinkage network** and the large-margin Gaussian Mixture (L-GM) loss are applied to improve the classification accuracy of the model.

[722] Zhang J, Xing L, Tan Z, et al. Multi-head attention fusion networks for multi-modal speech emotion recognition. Computers & Industrial Engineering, 2022, 168, p.108078.

>In unimodal, we use a two-layer Transformer’s encoder combination model to extract speech and text features separately, and MoCap is modeled using a **deep residual shrinkage network**.

[723] Wu X, Xu B, Luo H, et al. Adulteration quantification of cheap honey in high-quality Manuka honey by two-dimensional correlation spectroscopy combined with deep learning. Food Control, 2023, 154, p.110010.

>The combination of synchronous 2D-COS and **deep residual shrinkage networks** (**DRSN**) achieved the best performance compared to the other models, with the root mean square errors of prediction (RMSEP) of 3.1166 for Manuka honey and 2.3188 for acacia honey, respectively.

[724] Xu X, Zhang Y, Zhang R et al. Patient-specific method for predicting epileptic seizures based on **DRSN**-GRU. Biomedical Signal Processing and Control, 2023, 81, p.104449.

>A patient-specific seizure prediction method based on **deep residual shrinkage network** (**DRSN**) and gated recurrent unit (GRU) was then proposed.

[725] Xing Z, He Y, Chen J, et al. Health evaluation of power transformer using deep learning neural network. Electric Power Systems Research, 2023, 215, p.109016.

>And then, the significant features are extracted by DLNN which contains improved **Deep Residual Shrinkage Networks** (IDRSN) and the one-dimension convolution neural network (1DCNN).

[726] Ma X, Hu H, Ren Y. A hybrid deep learning model based on feature capture of water level influencing factors and prediction error correction for water level prediction of cascade hydropower stations under multiple time scales. Journal of Hydrology, 2023, 617, p.129044.

>A new hybrid model based on a refined **deep residual shrinkage network** and an optimized gated recurrent unit – long term memory network (GRU-LSTM) model is proposed for water level prediction at different time scales.

[727] Su Z, Yu J, Xiao X, et al. Deep learning seismic damage assessment with embedded signal denoising considering three-dimensional time–frequency feature correlation. Engineering Structures, 2023, 286, p.116148.

>Seismic signals are first transformed into time–frequency maps using NAMEMD (noise-assisted multivariate empirical mode decomposition) and non-parametric time–frequency analysis with Duhamel integral, and the seismic damage level is predicted with a **deep residual shrinkage network** (DRSNet).

[728] Zhang R, Jia J, Zhang R.EEG analysis of Parkinson's disease using time–frequency analysis and deep learning. Biomedical Signal Processing and Control, 2022, 78, p.103883.

> By combining time–frequency analysis with deep learning, tunable Q-factor wavelet transform with **deep residual shrinkage network** (TQWT-DRSN) and the wavelet packet transform with **deep residual shrinkage network** (WPT-DRSN) are applied to classify four kinds of clinical sleep EEG data in Shaanxi Provincial People's Hospital...

[729] Quan R, Liu P, Li Z, et al. A multi-dimensional residual shrinking network combined with a long short-term memory network for state of charge estimation of Li-ion batteries. Journal of Energy Storage, 2023, 57, p.106263.

>To solve these problems, a fusion network combining a multi-dimensional **residual shrinkage network** (MRSN) with a long short-term memory network (LSTM) is proposed for SoC estimation. 

[730] Mandava M. MDensNet201-IDRSRNet: Efficient cardiovascular disease prediction system using hybrid deep learning. Biomedical Signal Processing and Control, 2024, 93, p.106147.

>Finally, a deep learning-based improved **deep residual shrinkage network** (IDRSNet) is employed to predict cardiovascular disease.

[731] Li H, Zhang Z, Zhang C.Data augmentation via variational mode reconstruction and its application in few-shot fault diagnosis of rolling bearings. Measurement, 2023, 217, p.113062.

>Next, the augmented balanced dataset is utilized to train a **deep residual shrinkage network** (**DRSN**), which is then employed for the classification of test samples.

[732] Dai C, Hu S, Zhang Y, et al. Cavitation state identification of centrifugal pump based on CEEMD-**DRSN**. Nuclear Engineering and Technology, 2023, 55(4), pp.1507-1517.

>A closed cavitation test bench of a centrifugal pump is constructed, and a method for precisely identifying the cavitation state is proposed based on Complementary Ensemble Empirical Mode Decomposition (CEEMD) and **Deep Residual Shrinkage Network** (DRSN). First, we compared the cavitation sensitivity of pressure fluctuation, vibration, and liquid-borne noise and decomposed the liquid-borne noise by CEEMD to capture cavitation characteristics. The decomposition results are sent into a 12-layer **deep residual shrinkage network** (**DRSN**) for cavitation identification training.

[733] Dai C, Hu S, Zhang Y, et al. Cavitation state identification of centrifugal pump based on CEEMD-DRSN. Nuclear Engineering and Technology, 2023, 55(4), pp.1507-1517.

>This paper presents an Efficient Shrinkage Temporal Convolutional Network (ESTCN) model, which combines the Temporal Convolutional Network (TCN) and an improved **Deep Residual Shrinkage Network** (**DRSN**) to forecast PV power output.

[734] Chen J, Lin W, Cai S, et al. BiTCN_**DRSN**: An effective software vulnerability detection model based on an improved temporal convolutional network. Journal of Systems and Software, 2023, 204, p.111772.

>To overcome the limitations of the traditional TCN, we propose a bidirectional TCN model based on the **Deep Residual Shrinkage Network** (**DRSN**), namely BiTCN_DRSN. 

[735] Yin H, Xu H, Fan W, et al. Fault diagnosis of pressure relief valve based on improved deep Residual Shrinking Network. Measurement, 2024, 224, p.113752.

>Specifically, we combined the Elastic Weight Consolidation (EWC) algorithm with **Deep Residual Shrinkage Network** (**DRSN**) to achieve high diagnostic accuracy.

[736] Wu X, Xu H, Zhou H, et al. Improving lithofacies prediction in lacustrine shale by combining deep learning and well log curve morphology in Sanzhao Sag, Songliao Basin, China. Computers & Geosciences, 2024, 193, p.105735.

>In this study, the lower Qingshankou member in the Sanzhao Sag was selected as the research target, and the **Deep Residual Shrinkage Network** (**DRSN**), known for its ability to handle complex nonlinear relationships and mitigate the effects of noisy data through residual connections and shrinkage mechanisms, was employed as a deep learning framework for predicting lithofacies in lacustrine shale formations for the first time.

[737] Ma C, Tu X, Zhou G, et al. Source-free cross-domain fault diagnosis of rotating machinery using the Siamese framework. Knowledge-Based Systems, 2024, 300, p.112179.

>Specifically, a **deep residual shrinkage network** with parallel spatial and channel-wise attention mechanisms (**DRSN**-SCW) is used for feature extraction to suppress background noise.

[738] Jiarun Y, Yafeng, W. MDTCNet: Multi-Task Classifications Network and TCNN for Direction of Arrival Estimation[J]. China Communications, 2024, 21(10), pp.1-19.

>To overcome the DoA estimation challenge without the prior information about signal sources number and multipath number in millimeter wave system, the multi-task **deep residual shrinkage network** (MT-**DRSN**) and transfer learning-based convolutional neural network (TCNN), namely MDTCNet, are proposed.

[739] Zhan J, He S, Wang C et al. Improved TCN-Vine Copula Method for Wind Speed Prediction Using 5G+ Technology Data Transmission[C]. In 2024 6th International Conference on Industrial Artificial Intelligence (IAI) (pp. 1-6)

>Initially, the residual module in TCN is improved by using the attention mechanism and soft thresholding concept from **deep residual shrinkage network** (**DRSN**) for preliminary prediction.

[740] Wang Y, Cai X, Tang X, et al. HSRA-Net: Intelligent Detection Network of Anomaly Monitoring Data in High-Speed Railway[J]. IEEE Transactions on Intelligent Transportation Systems.2024.

>To achieve the end-to-end classification, the anomaly detection module improves the residual network by creating a **deep residual shrinkage network** with self-attention (**DRSN**-SA).

[741] Wang F, Chen D, Zhang X, et al. Study on a novel electrode with automatic replenishment of conductive fluid for use in the built environment[J]. IEEE Transactions on Instrumentation and Measurement. 2024.

>this study proposes a method to improve the efficiency of preform lifting alignment based on the **deep residual shrinkage network** (**DRSN**).

[742] Guo H, Zhao, X. MSDFM-ASTRSB: A rolling bearing fault diagnosis method with limited samples[J]. IEEE Transactions on Instrumentation and Measurement. 2024.

>Then, asymmetric soft threshold **residual shrinkage block** (ASTRSB) is designed, by constructing asymmetric threshold block (ATB), adaptive slope block (ASB) and Asymmetric soft threshold function...

[743] Yu J, Yao S, Jiang X, et al. Stretchable Capacitive Tactile Sensor Array for Accurate Distributed Pressure Recognition[J]. IEEE Sensors Journal. 2024.

>An improved bilinear convolutional neural network (BCNN) integrated with **deep residual shrinkage network** (**DRSN**) is proposed to actually heighten the feature extraction capability and thus precise distributed pressure recognition.

[744] Fang L, Liu Y, Li X, et al. Intelligent Fault Diagnosis of Rolling Bearing Based on Deep Transfer Learning[C]. In 2024 6th International Conference on Natural Language Processing (ICNLP) (pp. 753-757).

>Secondly, a **Deep Residual Shrinkage Network** (**DRSN**) is used to filter out the sample noise and automatically extract the data features;

[745] Su N, Liu F. A method of EEG emotion recognition based on residual contraction network[C]. In 2024 2nd International Conference on Signal Processing and Intelligent Computing (SPIC) (pp. 141-144).

>Then the **residual shrinkage module** is combined with the improved deep separable convolutional network to remove redundant features and reduce the network computing cost while solving the problem of model gradient disappearance.

[746] Zhang X, Liu C, Yuan W, et al. Sparse Prior-Guided Deep Learning for OTFS Channel Estimation[J]. IEEE Transactions on Vehicular Technology, 2024.

>In this paper, we propose a **deep residual shrinkage neural network** (DRSNN) based on sparse prior for solving the orthogonal time frequency space (OTFS) channel estimation problem.

[747] 王文平,申广俊,李洋.基于人工智能大数据分析的用户满意度预测方法及装置[P].湖北省:CN202410531047.4,2024-08-06.

>通过充分整合数据采集分析技术及工具，可以利用图片扫描识别技术对采集的图片数据进行图像识别，包括：卷积神经网络、残差网络、**残差收缩网络**、神经网络图像识别技术等。

[748] 陈尚俭,钟宜桑,王江峰,等.图像快速匹配方法、装置、计算机设备和存储介质[P].浙江省:CN202410405069.6,2024-07-02.

>深度学习网络模型也可以由卷积神经网络模型、残差收缩网络模型等其他网络模型来替换，对此并不进行限制。

[749] 马峰,李明子.混响与噪声抑制方法、装置、电子设备及存储介质[P].陕西省:CN202111027452.5,2024-06-11.

>其中降噪的方法和去混响信号的方法可以是维纳滤波进行线性滤波降噪，还可以是**深度残差收缩网络**进行非线性降噪...

[750] 李天桢,高世伟,党小超,等.一种基于伪标签优化的集成学习半监督工业数据预测方法[P].甘肃省:CN202410306361.2,2024-06-04.

>使用测试集对训练好的遮蔽卷积注意力**残差收缩网络**模型进行评估。

[751] 吕喆,梁燕萍,余立.一种信息处理方法、装置及设备[P].北京市:CN202211523599.8,2024-05-31.

>归一化后的数据依次通过两个**深度残差收缩模块**(即图中的**深度残差收缩模块**‑I和**深度残差收缩模块**‑II，对应于上述第一**深度残差收缩层**和第二**深度残差收缩层**)进行特征提取；**深度残差收缩模块**处理后的数据并行输入到用户数估计分支与多径数估计分支；

[752] 潘贤真,魏世奇,裘斌,等.一种快递单安全接入系统[P].广东省:CN202410315783.6,2024-05-31.

>以BiLSTM神经网络模型（双向长短期记忆神经网络）为基础，引入**DRSN**网络（**深度残差收缩网络**），构建DRSN‑BiLSTM模型，得到网络异常检测模型。

[753] 汪建涛,杨卫华,陈凯妍,等.白内障分级方法及装置、电子设备、存储介质[P].广东省:CN202410260300.7,2024-05-31.

>白内障特征提取器可以基于卷积神经网络、深度残差网络、**深度残差收缩网络**等构建形成。

[754] 杨庆友,尹少春,王君珂,等.业务处理方法、装置、设备及存储介质[P].北京市:CN202410211459.X,2024-05-28.

>其中神经网络模型可以是基于多层感知机、反向传播神经网络(back  propagation  network)、卷积神经网络(convolutional  neural  networks，CNN)、**残差收缩网络**、生成式对抗网络(generative  adversarial  networks，GAN)、支持向量机(support  vector  machines，SVM)或深度残差网络(deep  residual  networks，DRN)等神经网络中的至少一种构建得到的。

[755] 李丹洪,邸皓轩,张晓武.退出二维码的方法和装置[P].广东省:CN202111136786.6,2024-05-14.

>终端设备可以基于下述一种多种神经网络模型，构建用于翻腕识别的神经网络模型，例如：基于门控循环单元的循环神经网络(gated recurrent unit，GRU)、反向传播神经网络(back propagation network)、卷积神经网络(convolutional neural networks，CNN)、**残差收缩网络**...

[756] 杨新宇,邵思羽,池福临,等.一种深度降噪迁移学习的滚动轴承变工况故障诊断方法[P].陕西省:CN202410087893.1,2024-05-10.

>其中特征提取层使用**深度残差收缩网络**提取变工况下滚动轴承的深层故障特征，其网络的每个特征提取块网络结构如图2所示。

[757] 程逸,胡阳,刘吉臻,等.风机轴承故障诊断模型训练方法、装置、电子设备及介质[P].北京市:CN202311695252.6,2024-04-12.

>初始分类模型具体可以为**深度残差收缩网络**。

[758] 于水,张钰,韩明良.基于特征融合的高温泵故障诊断方法及相关装置[P].陕西省:CN202410230855.7,2024-04-12.

>高温泵故障诊断模型的一个分支为基于**深度残差收缩网络**的第一特征提取模块。

[759] 李君,张茜茜,朱明浩,等.基于密集无线网络的功率控制方法[P].江苏省:CN202110738351.2,2024-03-29.

>步骤3、构建**DRSN**框架并初始化**DRSN**参数；

>**深度残差收缩网络**(**DRSN**)是深度残差网络的一种新的升级版本，其实是深度残差网络、注意力机制(参照Squeeze‑and‑Excitation Network，SENet)和软阈值化的深度集成。在一定程度上，**DRSN**的工作原理，可以理解为：通过注意力机制注意到不重要的特征，然后通过软阈值化将它们置为零；或者说，通过注意力机制注意到重要的特征，将它们保留下来，从而加强深度神经网络从含噪声信号中提取有用特征的能力。换言之，**DRSN**面向的是带有“噪声”的信号，将“软阈值化”作为“收缩层”引入残差模块之中，并且提出了自适应设置阈值的方法。实际上，这里的“噪声”可以宽泛地理解为“与当前任务无关的特征信息”。

[760] 谢文刚.模型迭代优化方法、装置、电子设备和可读存储介质[P].重庆市:CN202111135976.6,2024-02-02.

>利用携带有样本标签的训练样本对构建的模型进行训练，其中，构建的模型可以是神经网络模型，包括但不限于多层感知机、卷积神经网络、**残差收缩网络**等。

[761] 吴建国,高明亮,付长昭,等.服务器的机盖开度检测方法及装置、存储介质及电子设备[P].江苏省:CN202311412298.2,2024-01-30.

>第一子网络模型可以是包含深度残差网络(或者，**深度残差收缩网络**)的网络模型...

[762] 王君.基于深度学习的图像识别和分类算法[P].黑龙江省:CN202311015126.1,2023-11-03.

>该步骤采用的算法包括但不限于：深度优先搜索、广度优先搜索、**残差收缩网络**等方式...

[763] 李锋,徐文元,邹武合,等.外挂检测方法、装置、计算机设备和存储介质[P].浙江省:CN202310636574.7,2023-10-03.

>可以利用卷积神经网络(CNN)、循环神经网络(RNN)以及**残差收缩网络**(**RSN**)等中的一个或多个对组合特征进行时序特征提取。

[764] 文井辉,李帅永,韩明秀,等.基于**DRSN**和麻雀搜索优化的设备剩余寿命预测方法[P].重庆市:CN202111049621.5,2023-09-15.

>对振动信号做归一化处理，构建数据集；搭建**DRSN**模型，将数据集输入训练好的**DRSN**模型，模型输出得到健康指标；

[765] 余道德,孙海涛.基于物联网的数据存储拓展方法、装置、设备及存储介质[P].广东省:CN202310561133.5,2023-07-25.

>可以利用**深度残差收缩网络**从所述单位功率图谱中提取出目标锋形特征，可以使用sigmoid函数对所述目标锋形特征进行归一化，得到目标锋形编码。

[766] 吴桐,林峰,唐旭升.一种基于毫米波感知心脏特征的连续身份识别系统[P].江苏省:CN202310442350.2,2023-07-25.

>在本次实施方案中，神经网络为**深度残差收缩网络**(**DRSN**)，特征维度为32，分类器为SVM/RandomForests/KNN。

[767] 刘钦锐.一种三维虚拟沙盘的热点标注方法、装置和存储介质[P].广东省:CN202310136834.4,2023-06-23.

>所述深度识别根据图像识别中的深度学习进行的，可以是自构建的深度学习的神经网络模型，也可以使用现有的进行深度学习的神经网络模型，例如卷积神经网络、残差网络或**残差收缩网络**。

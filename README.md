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

**论文网址**：https://ieeexplore.ieee.org/document/8850096

**作者主页**(**赵明航**-**哈工大教师主页**)：http://homepage.hit.edu.cn/zhaominghang

**百度百科**：https://baike.baidu.com/item/深度残差收缩网络

**作者谷歌学术主页**：https://scholar.google.com/citations?user=k82TzLwAAAAJ&hl=zh-CN

## Additional Notes (备注)

There might be some problems in the Keras code. The TFLearn code is recommended for usage.

## Thanks for the Applications (感谢以下文献及作者)

**According to incomplete statistics, deep residual shrinkage networks have been directly applied or improved by over 1000 literatures to many fields such as machinery, electricity, vision, medical, speech, text, radar, remote sensing.(根据不完全统计，深度残差收缩网络已经被超过1000篇文献直接应用或改进后应用于机械、电力、视觉、医疗、语音、文本、雷达、遥感等众多领域)**

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

[178] 谢涛.基于深度学习的微细粒矿物识别研究[D].中国矿业大学,2020.

>基于这些影响，本文在 Faster R-CNN 的共享网络 ResNet-50 中引入了**深度残差收缩网络**，此网络利用注意力机制实现与当前任务目标有关的重要特征提取，抑制无关因素干扰。

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

[466] 秦思危.基于运行数据的多冷水机组能耗预测和节能优化研究[D].重庆理工大学,2024.

>然后通过引入自注意力机制和**残差收缩结构**改进原始的时间卷积网络建立冷水机能耗预测模型

[467] 刘云峰, 杨晋彪, 韩晋锋, 等.《2.1 **残差收缩网络**》基于边缘增强生成对抗网络的电力设备热成像超分辨率重建[J]. 电力建设, 2021, 42(07): 83-89.

[468] 史宝岱, 张秦, 李宇环, 等.《2 **残差收缩网络**》基于混合注意力机制的SAR图像目标识别算法[J]. 电光与控制, 2023, 30(04): 45-49.

[469] 马贵林, 李世超, 高宏力, 等.《2.1 **深度残差收缩网络**》考虑噪声抑制的高超声速风洞气动力识别方法[J]. 航空动力学报, 2023, 38(02): 420-430.

[470] 雷宇, 刘少儒, 徐寅林.《1.1 **DRSN**分类诊断模型的设计》具有自动抗噪功能的心电信号分类算法[J]. 电子测量技术, 2021, 44(21): 49-55.

[471] 乔春阳.基于小样本学习的不同型号滚动轴承故障诊断方法研究[D].哈尔滨理工大学,2022.

>构建改进的关系网络，在关系网络的嵌入模块中引入**残差收缩模块**和缩放指数型线性单元...

[472] 张渝东.流量调节阀多开度干扰下故障诊断关键技术研究[D].哈尔滨工程大学,2022.

>通过分析结果，确定了聚类算法的最佳参数并证明了生成对抗插补网络与**残差收缩神经网络**在实际应用过程中的优越性与稳定性。 

[473] 张秀再, 邱野, 张晨.《2.2.1 **深度残差收缩网络**》改进YOLOv5s算法的地铁场景行人目标检测[J]. 激光与光电子学进展, 2023, 60(06): 144-153.

[474] 贺才郡, 李开成, 董宇飞, 等.《2.3 **DRSN**》基于知识蒸馏与RP-MobileNetV3的电能质量复合扰动识别[J]. 电力系统保护与控制, 2023, 51(14): 75-84.

[475] 池强. 基于深度学习的小样本高光谱图像分类关键算法研究[D]. 齐鲁工业大学, 2023.

>为了增强模型表征能力，设计了一种**残差收缩网络**作为特征提取器，并在模型中加入无监督域适应方法缓解训练中的域偏移问题。

[476] 陈作懿, 邓超, 吴军, 等.《2.1 **残差收缩网络**》基于收缩自注意关系网络的机械装备故障智能检测与定位方法[J]. 中国科学:技术科学, 2023, 53(07): 1214-1228.

[477] 朱元梅. 基于少样本特征学习的轴承故障诊断研究[D]. 大连海事大学, 2023.

>设计一种基于**残差收缩**卷积网络特征学习网络(Residual shrinkage modular Convolutional Neural Network，RCNN)的非线性度量方法。该方法首先在特征提取阶段采用**残差收缩模块**，将源域样本输入到模型中进行训练...

[478] 宋绍剑, 姜屹远, 刘斌.《1 基于SSA优化的**DRSN**-TCN短期光伏功率点预测模型》一种TCN的改进模型及其在短期光伏功率区间预测的应用[J]. 计算机应用研究, 2023, 40(10): 3064-3069.

[479] 闫文恒, 程永强, 郝润芳.《1.4 **深度残差收缩网络**》双重融合的轻量级卷积神经网络轴承故障诊断[J]. 组合机床与自动化加工技术, 2023, (05): 174-177+183.

[480] 李大鹏, 周晓彦, 王基豪, 等.《1.2 **DRSN**》基于Mel频谱值和深度学习网络的鸟声识别算法[J]. 应用声学, 2023, 42(04): 825-832.

[481] 阮慧, 黄细霞, 李登峰, 等.《1.2 **深度残差收缩网络**》滚动轴承细粒度故障诊断研究[J]. 计算机工程与应用, 2024, 60(06): 312-322.

[482] 王爱玲, 马文臻, 邹自明, 等. 基于领域自适应的卫星工程参数异常检测[J]. 计算机工程, 2023, 49(05): 29-37+47.

>利用**深度残差收缩网络**(**DRSN**)结构框架，在训练过程中将无标签的目标域卫星工程参数数据加入网络训练过程...

[483] 李帅永, 张超, 梅琳, 等.《1.1 **深度残差收缩网络**》基于改进Holt双指数模型的轴承剩余寿命预测方法[J]. 自动化与仪器仪表, 2023, (02): 87-93.

[484] 陈佳, 章坚武, 张浙亮.《1.1 **深度残差收缩网络**》基于上下文信息与注意力特征的欺骗语音检测[J]. 电信科学, 2023, 39(02): 92-102.

[485] 余佳润, 王亚峰.《2.3 基于**DRSN**的LOS径DoA估计方法》一种低信噪比下基于深度学习的DoA估计方法[J]. 北京邮电大学学报, 2022, 45(06): 115-121.

[486] 李书轩. 基于内容的旅游图像检索系统研究与开发[D]. 扬州大学, 2022.

>本文拟采用**深度残差收缩网络**(**Deep Residual Shrinkage Networks**，简称**DRSN**)算法对旅游图像进行特征提取，在保证原始特征信息不丢失的基础上减小低相关度特征的权重，同时研究其在小规模旅游图像数据集上的表现，并基于该算法搭建旅游图像检索系统。

[487] 陈玲玲, 毕晓君. 多模态融合网络的睡眠分期研究[J]. 智能系统学报, 2022, 17(06): 1194-1200.

>首先利用**残差收缩网络**设计各模态特征提取网络用于提取各模态特征，并在通道维度上进行拼接融合，利用通道注意力机制进一步对融合特征进行重标定得到睡眠多导图的时不变特征；

[488] 王延年, 杨恒升, 刘妍妍, 等. 基于改进Retinex-Net的低照度图像增强算法[J]. 西安工程大学学报, 2022, 36(05): 79-86.

>将Retinex-Net网络作为基础模型对输入图像进行分解，在卷积层中引入**残差收缩网络**以去除分解过程中产生的噪声；

[489] 冉文静, 赵晓顺, 霍晓静, 等. 振动监测及减振技术在耕整地机械的应用研究[J]. 中国农机化学报, 2022, 43(06): 32-42.

>最后针对振动信号处理提出局部变换结合时频分析法、**深度残差收缩网络**法两种振动信号处理方法，针对机械减振措施提出采用阻尼材料实现机械减振的建议，期望为耕整地机械乃至其他农机装备振动监测及减振技术提供参考。

[490] 李新玉, 赵知劲.《1.2.1 **深度残差收缩模块DRSN**》基于深度学习的动态主用户频谱感知算法[J]. 电子技术应用, 2024, 50(01): 60-65.

[491] 赖裕,李锵,聂为之,等.基于混合知识蒸馏的轻量级胸部疾病分类算法[J].光电子·激光,2024,35(09):993-1000.

>该算法将优化后的**残差收缩模块**加入到基础网络MobileViT中，利用软阈值化的方式过滤X光片中的背景噪声；

[492] 王旭伟.基于深度学习的PCB裸板缺陷检测研究[D].盐城工学院,2024.

>用引入深度可分离卷积的并联**深度残差收缩网络**重构生成器...

[493] 黄宇, 张宗拾, 刘家兴, 等.《1.1 **深度残差收缩网络**》基于改进时间卷积网络与藤Copula的短期风速预测[J]. 电力科学与工程, 2024, 40(07): 60-69.

[494] 马剑波, 左翔, 丛小飞, 等.《3.1 **深度残差收缩网络**》基于深度学习的水利工控网络流量异常检测方法[J/OL]. 水利水电技术(中英文), 1-14[2024-11-27].

[495] 苌文涵, 张云翔, 顾彬, 等.《2.1 改进**DRSN**》结合改进DRSE-GCNN的电力调度语声识别模型[J/OL]. 应用声学, 1-10[2024-11-27]

[496] 李振坤, 张天翼, 邓莉荣, 等.《3 基于**DRSN**-TCN的韧性在线评估模型》基于模型-数据混合驱动的区域能源互联网韧性在线评估[J]. 电网技术, 2024, 48(10): 4060-4076.

[497] 查燕平, 王红军, 沈哲贤.《1.1 **深度残差收缩网络**》特征融合式轻量化调制识别方法设计与研究[J/OL]. 小型微型计算机系统, 1-10[2024-11-27].

[498] 黎芮彤. 《2.2.5 **深度残差收缩网络DRSN**》面向程序语言和自然语言的查询匹配模型研究[D]. 武汉大学, 2021.

[499] 江伟雄, 王吉, 吴军, 等. 基于模糊**残差收缩网络**与人机协同的机械装备健康评估方法[J/OL]. 仪器仪表学报, 1-13 [2024-12-06].

[500] 何牧耕.《5 基于改进**残差收缩**D3QN的噪声环境故障诊断》非完备弱数据环境下基于深度强化学习的旋转机械故障诊断研究[D]. 重庆大学, 2023.

[501] 文秀华.《3 基于**深度残差收缩网络**的无线设备识别方法》信号指纹特征提取与识别方法研究[D]. 海南大学, 2022.

[502] 廖晓青, 陈历, 许建远, 等. 基于残差注意力自适应去噪网络和Stacking集成学习的局部放电故障诊断[J]. 电子技术应用, 2024, 50(11): 66-73.

>受**深度残差收缩网络**（**Deep Residual Shrinkage Network**, **DRSN**)和CAM启发，本文提出一种残差注意力自适应去噪网络（RAADNet），通过深度结构自适应设置去噪阈值，从而使得模型有效消除冗余特征和噪声信息，避免人工设置去噪阈值带来的误差...

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

[732] Wu X, Peng H, Cui X, et al. Multichannel Vibration Signal Fusion Based on Rolling Bearings and MRST-Transformer Fault Diagnosis Model. IEEE Sensors Journal. 2024 Apr 10.

>The MRST-Transformer comprises an enhanced **residual shrinkage building unit** with channel-wise (RSBU-CW) and a shallow cross-vision transformer (Cross Vit).

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

[762] 王君. 基于深度学习的图像识别和分类算法[P]. 黑龙江省: CN202311015126.1, 2023-11-03.

>该步骤采用的算法包括但不限于：深度优先搜索、广度优先搜索、**残差收缩网络**等方式...

[763] 李锋, 徐文元, 邹武合, 等. 外挂检测方法、装置、计算机设备和存储介质[P]. 浙江省: CN202310636574.7, 2023-10-03.

>可以利用卷积神经网络(CNN)、循环神经网络(RNN)以及**残差收缩网络**(**RSN**)等中的一个或多个对组合特征进行时序特征提取。

[764] 钱陈栋, 张洋, 庄博, 等. 一种基于三维激光扫描技术的智能监测系统及方法[P]. 江苏省: CN202110225937.9, 2021-05-28.

>深度学习模块运用相关AI深度学习的算法模型如卷积神经网络、**残差收缩网络**等，对三维激光图像阈值软化并特征识别。

[765] 余道德,孙海涛.基于物联网的数据存储拓展方法、装置、设备及存储介质[P].广东省:CN202310561133.5,2023-07-25.

>可以利用**深度残差收缩网络**从所述单位功率图谱中提取出目标锋形特征，可以使用sigmoid函数对所述目标锋形特征进行归一化，得到目标锋形编码。

[766] 吴桐,林峰,唐旭升.一种基于毫米波感知心脏特征的连续身份识别系统[P].江苏省:CN202310442350.2,2023-07-25.

>在本次实施方案中，神经网络为**深度残差收缩网络**(**DRSN**)，特征维度为32，分类器为SVM/RandomForests/KNN。

[767] 刘钦锐.一种三维虚拟沙盘的热点标注方法、装置和存储介质[P].广东省:CN202310136834.4,2023-06-23.

>所述深度识别根据图像识别中的深度学习进行的，可以是自构建的深度学习的神经网络模型，也可以使用现有的进行深度学习的神经网络模型，例如卷积神经网络、残差网络或**残差收缩网络**。

[768] 魏国,刘万青,周文健,等.基于深度学习的UWB NLOS传播误差抑制方法[P].湖南省:CN202310265780.1,2023-06-23.

>该方法基于深度学习技术，使用训练好的**深度残差收缩网络**(**Deep Residual Shrinkage Network**，**DRSN**)模型进行误差抑制。

[769] 戴会超,毛劲乔,龚轶青,等.改善珍稀鱼类种群生境的水利工程调控系统及调控方法[P].北京市:CN202211022511.4,2023-06-09.

>第一阈值设定的算法包括但不限于**深度残差收缩网络**法和假设检验P值拒绝域法。

[770] 章昕亮,李天昀,龚佩,等.基于深度学习的通信信号调制方式开集识别方法及系统[P].河南省:CN202210095612.8,2023-05-23.

>特征映射单元利用在卷积层添加**残差收缩模块**来对输入的信号数据卷积运算以提取特征信息...

>因为**残差收缩网络**可以有效地抑制信号中的噪声，所以可在卷积层部分加入残差收缩模块对输入的I/Q数据进行卷积运算提取特征信息。

[771] 杨喜业,黄博,王伟民,等.一种基于AI算法的实时血压预测方法的血压仪[P].广东省:CN202211654639.2,2023-05-23.

>训练AI算法血压预测模型的模型时，使用的神经网络模型为**深度残差收缩网络**(**Deep Residual Shrinkage Network**，**DRSN**)...

[772] 颜林,霍伟明.空调器及其控制方法、计算机可读存储介质[P].广东省:CN202111012776.1,2023-04-07.

>睡眠温度预测模型还可以是其他类型的机器学习模型，如多层感知机、**残差收缩网络**等。

[773] 李建华,于传帅.数据处理方法、装置、电子设备和可读存储介质[P].广东省:CN202110898463.4,2023-02-17.

>所述待处理网络模型可的具体类型不做限定，其可以是卷积神经网络模型(CNN，Convolutional neural networks)、**残差收缩网络模型**...

[774] 汤俊伟,徐微,胡博超,等.基于熵谱密度和自适应收缩卷积的安卓恶意软件检测方法[P].湖北省:CN202211263564.5,2023-01-13.

>为对特征进行去噪，本文在**深度残差收缩网络**研究的基础上，引入了软阈值激活函数，借助软阈值化将这些噪声所对应的特征置为零，并通过注意力机制动态地根据每个样本的情况单独的为每个样本设置阈值，作为非线性变换层集成到本单元中。

[775] 张燧,徐少龙.设备剩余寿命预测方法、装置、计算机设备及介质[P].北京市:CN202110761542.0,2023-01-06.

>作为示例，可以使用**深度残差收缩网络**方式进行降噪处理。

[776] 殷安云,戴明,程洁,等.一种心室导管泵的监测方法及装置[P].安徽省:CN202211237884.3,2022-12-13.

>上述初始神经网络模型可以为卷积神经网络。更为具体的，可以为**深度残差收缩网络**。

[777] 赵俊豪.弹窗管理方法、装置及存储介质[P].广东省:CN202110792145.X,2022-12-06.

>初始模型可以是基于多层感知机、反向传播神经网络(back propagation network)、卷积神经网络(convolutional neural networks，CNN)、**残差收缩网络**...

[778] 逄岭,屠志鹏.CT扫描参数的调整方法、装置、存储介质和CT设备[P].辽宁省:CN202210763346.1,2022-11-11.

>具体地，神经网络(Neural Networks，NN)模型可以是卷积神经网络(Convolutional Neural Networks，CNN)模型、**残差收缩网络**(**Deep Residual Shrinkage Network**，**DRSN**)模型...

[779] 钱海波,钱海燕.一种智能建筑的外部作业人员实时跟踪记录系统[P].上海市:CN202210941874.1,2022-11-08.

>特征提取的算法包括有卷积神经网络、深度残差网络、**深度残差收缩网络**等...

[780] 胡郡郡,唐大闰.模型生成方法、装置、计算机设备和存储介质[P].北京市:CN202210772572.6,2022-10-18.

>具体可通过卷积神经网络、深度残差网络或**深度残差收缩网络**对视频序列进行特征提取。

[781] 廖正凯,胡金龙,侯立升,等.一种车位检测方法、装置及电子设备[P].浙江省:CN202210868622.0,2022-10-14.

>本申请实施例中基于待检测图像提取出待检测特征集的方式可以为卷积神经网络模型，也可以为**深度残差收缩网络**模型...

[782] 陈雁翔,朱玉鹏,盛振涛,等.基于有监督对比学习和卷积神经网络的滚动轴承故障诊断方法[P].安徽省:CN202011564313.1,2022-09-13.

>这里根据信号的复杂程度可以选择更为复杂的**深度残差收缩网络**作为特征提取器。

[783] 杨奕飞,刘世界,苏贞,等.一种船舶动力设备剩余寿命预测系统及方法[P].江苏省:CN202210550575.5,2022-08-09.

>**深度残差收缩网络**依次连接的输入层、卷积层、四个**残差收缩单元**、池化层、全连接层；

[784] 刘娟,黄忠,陶孟元,等.基于残差收缩结构和非局部注意力的行为检测方法[P].安徽省:CN202210401553.2,2022-08-02.

>基于深度3D残差卷积神经网络并借鉴**深度残差收缩网络**的思想，在残差模块中嵌入收缩结构和软阈值化，设计3D‑**DRSN**结构，其残差收缩模块如图3所示。

[785] 包永挺,张宏杰,武美辰.一种样本成分分析方法、装置、设备及存储介质[P].上海市:CN202210397976.1,2022-07-29.

>神经网络模型的模型类型包括但不限于多层感知机、卷积神经网络模型、**残差收缩网络模型**、全连接网络模型...

[786] 鞠光亮,刘月.医学影像的检测方法、装置、存储介质和计算机设备[P].辽宁省:CN202210099872.2,2022-05-27.

>具体地 ，神经网络 (Neural Networks，NN) 模型可以是卷积神经网络(Convolutional  Neural  Networks，CNN)模型、**残差收缩网络**(**Deep Residual Shrinkage Network**，**DRSN**)模型...

[787] 戴捷,李亮.一种图像分类模型训练方法及图像分类方法、系统[P].江苏省:CN202011204792.6,2022-05-24.

>在实际应用中可以根据样本数据及实际需求选择其他网络模型，例如**深度残差收缩网络**、超深度卷积网络(VGG-16)等主流的图像分类训练模型...

[788] 李君,张茜茜,朱明浩,等.基于密集无线网络的功率控制策略[P].江苏省:CN202110738351.2,2022-05-24.

>构建**DRSN**框架，并初始化神经网络权重；

>对训练数据所有批次进行遍历，以批次为例，作为**DRSN**输入信号并得到相应的输出信号，构建损失函数；

[789] 崔洋洋,王星宇.音频获取的方法、装置、电子设备及存储介质[P].广东省:CN202111571347.8,2022-05-06.

>作为一种实施方式，电子设备可以通过**深度残差收缩网络**对说话音频片段进行优化处理。

[790] 李曦,王阳,付晓薇.一种固体氧化物燃料电池系统燃烧室火焰图像的处理方法[P].湖北省:CN202210016219.5,2022-04-15.

>而此处的识别处理，具体可以交由感知机、卷积神经网络、**残差收缩网络**等不同类型的神经网络模型来执行...

[791] 梁俊斌.音频处理方法、装置、计算机设备和存储介质[P].广东省:CN202111241118.X,2022-04-15.

>神经网络模型具体可以是卷积神经网络模型、**残差收缩网络**模型或多层感知机神经网络模型等。

[792] 孔令韬,苏新锋,孔亮,等.一种确定目标业务的方法、装置、电子设备及存储介质[P].北京市:CN202111586000.0,2022-04-08.

>获得分类图像所使用的图像分类模型可以包括卷积神经网络模型、**残差收缩网络模型**、SVM神经网络模型以及小卷积核神经网络模型等。

[793] 曾超明,杨顺,杨飞飞,等.一种支持浮动电价的电动自行车充电桩及其充电方法[P].江苏省:CN202111074590.9,2022-02-25.

>上述配电网的预估负载率、充电站的预估负载率由神经网络训练模型获得，如卷积神经网络、**残差收缩网络**等模型...

[794] 陈姿.一种音乐推荐方法、装置以及可读存储介质[P].广东省:CN202111137216.9,2021-12-21.

>物品分析网络具体可以为卷积神经网络、残差网络、**残差收缩网络**等，本申请实施例对物品分析网络的具体类型不做限定。

[795] 冯小峰,冯浩洋,郭文翀,等.一种电网数据异常检测方法及装置[P].广东省:CN202110537094.6,2021-07-09.

>识别模型所采用的机器学习模型可以是现有技术中广泛应用的已经成熟的机器学习模型，例如，多层感知机、卷积神经网络、**残差收缩网络**等...

[796] 刘哲.基于改进DQN网络的滚动轴承故障诊断方法研究[D].哈尔滨理工大学, 2021.

>针对原有DQN网络特征提取不足问题，提出通过**深度残差收缩模块**搭建DQN模型的网络部分，同时对输出层部分做了改进，提高了模型的稳定性和诊断准确率，并通过理论分析和多组对比实验深入研究数据不平衡和变负载问题。

[797] 刘颖,郑力新.一种用于人体关键点检测的改进算法[J].现代计算机,2020,(30):61-65.

>并且将其使用的基本单元（残差网络）改为改进后的**深度残差收缩网络**，在保注意力机制训练的同时也保存原有信息，将每个中间监督输出信息经过使用反卷积操作...

[798] 吕杰.航线维修增强现实视觉关键技术研究[D].中国民航大学,2020.

>针对发动机训练数据集无包裹外壳和特征复杂的问题，使用软阈值改进残差网络的**残差收缩网络**用于图像识别...

[799] 吴守尊,张婧菲,台树杰,等.基于迁移学习的电网图像自主判读及运行态势感知研究[J].环境技术,2021,39(06):189-194.

>然后利用**深度残差收缩网络**对数据池预先训练集进行电网图像异常特征知识学习辨识，构建时间正序下的电网图像异常特征全息感知机制；

[800] 曾诚,吴佳媛,罗霞.城市轨道交通短时客流预测文献综述[J].铁道运输与经济,2021,43(08):105-111+125.

>最后建议应用态势感知、**深度残差收缩网络**、Transformer等新的预测方法，为短时客流预测方向的学者提供借鉴和参考。

[801] 董绍江,裴雪武,汤宝平,等.基于FNER性能退化指标及IDRSN的滚动轴承寿命状态识别方法*[J].机械工程学报,2021,57(15):105-115.

>针对滚动轴承退化性能难以评估、寿命状态难以识别的问题，提出一种基于特征噪声能量比(Feature-to-noise energy ratio，FNER)指标及改进**深度残差收缩网络**(Improved **deep residual shrinkage network**，IDRSN)的滚动轴承寿命状态识别新方法。

[802] 李嘉琪.基于深度学习的恶意代码家族分类研究[D].北京邮电大学,2021.

>针对恶意代码中含有冗余信息的问题，本文继续对网络结构进行修改，通过引入**深度残差收缩网络**的结构，利用注意力机制在不同通道上对恶意代码图像上进行冗余信息的过滤，提高了恶意代码特征图在整个卷积网络特征图中的影响力。

[803] 刘亚.基于视频深度学习的小鼠恐惧情绪识别与分析系统研究[D].东南大学,2021.

>在U-Net网络下采样的卷积层嵌入SENet通道注意力机制模块和**深度残差收缩网络**模块并分别比较了分割性能，后者在本文自制的小鼠数据集上各项指标提高了2～3%，分割效果更好，其中交并比(Io U)指标达到0.903。

[804] 顾瑞洁.基于深度学习的电子鼻气体识别技术研究[D].华中科技大学,2021.

>针对时序数据多通道的空间无关性问题，使用一维卷积的方法，设计了基于多尺度的**残差收缩网络**MSRSN和基于Inception网络的电子鼻气体分类方法Inception-Time。

[805] 匡健.医学图像中肋骨骨折检测与分类算法研究[D].苏州大学,2021.

>本文提出了一种改进的3D**残差收缩网络**实现肋骨骨折的多分类。该方法可以针对肋骨图像数据中存在的噪声，借助注意力机制，实现了特征的软阈值化，从而达到了降噪的目的。

[806] 王润.基于人工蜂群算法优化的集成分类手势识别方法的研究[D].兰州理工大学,2021.

>本文在**深度残差收缩网络**的基础上提出了一种改进的**深度残差收缩网络**，通过替换性能更佳的激活函数、简化注意力机制的底层结构来优化网络的性能，并且对比了改进前后**深度残差收缩网络**的识别效果，验证了该网络的有效性；

[807] 牛广利.基于医学特征抽取和学习的肝硬化肝纤维化定量分析研究[D].上海工程技术大学,2021.

>针对肝硬化病程分类的问题，提出基于改进的胶囊网络(Capsule Network to Liver Capsule， Caps Net2LC)和**深度残差收缩网络**(**Deep Residual Shrinkage Network**，**DRSN**)的双流融合诊断网络，其中改进的胶囊网络对肝包膜特征块进行特征学习，**深度残差收缩网络**对肝实质特征块进行特征学习，最后通过特征拼接、非线性激活函数等为对肝硬化进行分期诊断。

[808] 吉萌萌.基于深度学习的特定区域空气质量预测研究[D].河北工业大学,2021.

>该模型利用时间卷积网络的空洞因果卷积，保证了较长的历史信息输入及未来信息的保密；并结合**深度残差收缩网络**中特殊注意力机制和软阈值化的思想对时间卷积网络中的残差模块进行了改进，解决了单一空气质量站点预测中因输入样本中的冗余信息不同而导致的重要信息权重分散问题。

[809] 吴思璠.合成语音检测的关键技术研究与实现[D].电子科技大学,2021.

>设计基于**残差收缩**的合成语音检测模型(RSBU-EETCN)。研究了噪声对EETCN模型性能的影响，结合**深度残差收缩模块**在降噪方面的良好表现，对EETCN模型进行优化改进。

[810] 胡盛翔.复杂背景条件下微小无人机目标检测和跟踪的研究与实现[D].南京理工大学,2021.

>在基础模型中加入**残差收缩模块**。该模块首先使用注意力机制来学习各特征通道的阈值。然后对特征进行软阈值化,以增强检测模型对复杂背景干扰的抑制作用。

[811] 薛晓倩.数控机床铣刀磨损状态预测技术研究[D].哈尔滨工程大学,2021.

>本文采用具有自适应降噪性能的**深度残差收缩网络**(**DRSN**)代替CNN，搭建DRSN-LSTM模型，并采用未降噪的信号灰度图作为网络模型输入训练模型，最终所得模型预测效果更好。

[812] 张正辉.水稻田主要虫害远程监测识别装备研发[D].山东农业大学,2022.

>网络是在Mask R-CNN识别网络的基础上，使用Swish激活函数对特征提取网络Res Net 101及其内部的深度残差块进行优化，提高识别网络的精度，同时将改进的**深度残差收缩块**引入特征提取网络。

[813] 朱学超.电网调度语音识别技术研究[D].内蒙古科技大学,2022.

>为了增强模型抗噪能力，本文将**深度残差收缩网络**和门控卷积网络引入到电网调度语音识别中来，通过**深度残差收缩网络**中收缩模块移除阈值区域的冗余信息来提高卷积神经网络特征提取能力，通过门控卷积网络捕获有效上下文。

[814] 肖潇.非协作通信信号识别技术研究[D].桂林电子科技大学,2022.

>为进一步提升低信噪比识别率，在CNN-Bi LSTM中加入具有软阈值降噪功能的**残差收缩模块**(**Deep Residual Shrinkage Module**，DRSM)，得到改进后的CBDDNN，在-10d B～0d B信噪比范围内，该网络在仿真数据集和RML2016.10a数据集的识别率比CNN-Bi LSTM分别提高了0.29%和2.63%。

[815] 王振东.基于深度学习的危险品掩膜标签生成算法研究[D].东北大学,2022.

>首先给定一个离散的初始轮廓，然后通过圆卷积的方式预测初始轮廓到基准轮廓的偏移量并在圆卷积过程中引入**深度残差收缩网络**并减少循环次数，进一步提升轮廓点预测的精度...

[816] 张力.基于Wi-Fi-CSI的人体行为与活动位置联合识别研究[D].云南大学,2022.

>针对上述问题，本文对无线感知联合识别任务进行了大量研究，进行了数据集的采集和相关实验，结合**深度残差收缩网络**，提出了一种利用Wi-Fi进行人体行为与活动位置联合识别方法。

[817] 刘畅.基于深度学习的行人检测算法研究[D].东北石油大学,2022.

>为了使改进后的算法在训练过程中能够更加稳定，检测精度更加准确，提出了一种引入**深度残差收缩结构**的SSD算法，将算法中的分类网络替换成**深度残差收缩结构**DRSN-CW。

[818] 赵迪.基于深度学习的智能运维知识库系统[D].江南大学,2022.

>利用**深度残差收缩网络**结合特征融合策略对胶囊网络的特征提取结构进行改进。通过**深度残差收缩网络**结构解决了图像噪声导致的模型鲁棒性问题。

[819] 王爱玲.融合深度学习和迁移学习的卫星工程参数异常检测方法[D].中国科学院大学(中国科学院国家空间科学中心),2022.

>为了解决这一问题，提出了一种基于融合深度学习和迁移学习的异常检测模型，模型采用**深度残差收缩网络**作为主网络的架构，在此基础上加入领域自适应的迁移方法。

[820] 苏昊.基于CNN与迁移学习的变工况下高速列车滚动轴承故障诊断研究[D].北京交通大学,2022.

>针对轴承现有故障诊断方法在工况变化后的准确率不足问题，对残差网络进行改进，提出了多尺度**深度残差收缩网络**的故障诊断模型。

[821] 魏胜强.基于深度残差网络的轴承故障诊断模型研究[D].河南理工大学,2022.

>首先改进**残差收缩模块**中的通道注意力网络并引入空间注意力网络，构建一种同时考虑内部通道和跨通道特征的混合注意力机制。

[822] 刘希.基于深度学习的生活垃圾分拣技术研究[D].东南大学,2022.

>基于稠密生成抓取配置算法的思路，在以**深度残差收缩网络**作为基本残差块的基础上，结合多模态先验信息、特征融合以及轻量级技术，提出一种轻量级的抓取姿态预测算法对姿态未知不规则目标物体的最优抓取参数进行预测，并与其他算法进行对比。

[823] 孙志铭.基于深度学习的海浪有效波高预报方法研究[D].大连理工大学,2022.

>针对信号处理领域所用的特征提取算法会导致输入序列大幅增多的问题，本文将通道注意力机制，空间注意力机制以及**残差收缩机制**相结合，对普通卷积残差网络的残差块结构进行了改进，提出了一种注意力**残差收缩块结构**，并对比了单独使用以及组合使用注意力机制和**残差收缩机制**的模型的海浪有效波高预测精度。

[824] 肖健.基于深度学习的智能超表面通信信道估计研究[D].湖南理工学院,2022.

>将**深度残差收缩网络结构**引入多任务网络的共享层中以实现自适应的软阈值化，从而缓解通信噪声的干扰，提高低信噪比下信道估计精度。

[825] 黄心成.侧扫声呐图像目标提取算法研究[D].江苏海洋大学,2022.

>根据初始分割的完成的一维数据，改进了一种**深度残差收缩网络模型**，使其在训练时能够更好地削弱干扰因素的影响，以学习一维特征。

[826] 张宇航.基于机器学习的离心泵空化状态识别方法研究与实现[D].江苏大学,2022.

>通过搭建一个12层的DRSN**深度残差收缩网络**，采用CEEMD对泵液载噪声进行分解,并将分解结果作为样本进行训练。

[827] 高英宁.基于深度学习的语音情感识别研究[D].长江大学,2022.DOI:10.26981/d.cnki.gjhsc.2022.000178.

>针对提出的生成对抗网络下的语音情感识别方法中存在的问题，设计了一种新改进方法，使用多生成器网络和多输出判别器网络来构建生成对抗网络结构，使用**深度残差收缩网络**(**DRSN**)和双线性插值法构建生成器网络，进一步降低噪声干扰，使得合成的模拟样本质量更高，加快了模型收敛速度。

[828] 张俊丰.基于多模态特征融合的语音情感识别研究[D].河北大学,2022.

>本文主要工作分为以下两部分：首先，模型使用Bi LSTM(Bi-directional Long Short-Term Memory，Bi LSTM)分别对语音和文本进行情感特征提取，而动作模态使用**深度残差收缩网络**进行噪声过滤和情感特征提取。

[829] 冯奇.基于生成对抗网络的帧结构及DSSS信号生成技术研究[D].中国电子科技集团公司电子科学研究院,2022.

>提出了一种改进的VAE-GAN信号重构算法，利用**深度残差收缩网络**(**Deep Residual Shrinkage Networks**，**DRSN**)对样本信号进行降噪处理...

[830] 孟雪晴.球磨机负荷状态诊断与预警分析技术研究[D].湖南大学,2022.

>首先采用宽卷积神经网络提取振动信号短时特征，并构建三层**深度残差收缩网络**，利用软阈值函数实现非线性变换...

[831] 张嘉文.基于深度学习的数字信号调制识别技术的研究[D].电子科技大学,2022.

>本文采用了具有更加强大降噪能力的**深度残差收缩网络**(**Deep Residual Shrinkage Network**，**DRSN**)作原始模型，并在其基础上进一步优化设计，作为识别架构中的分类器进行调制判决。

[832] 朱玉清.基于迁移学习的不同工况下滚动轴承故障诊断方法研究[D].重庆交通大学,2022.

>针对噪声和不同转速的复杂工况下滚动轴承故障诊断问题，提出一种**深度残差收缩**迁移网络的复杂工况下滚动轴承故障诊断方法。

[833] 徐成霞.基于深度学习的单幅图像去雨研究[D].安徽大学,2022.

>模型引入**深度残差收缩网络**，通过软阈值非线性变换子网络中的软阈值函数将冗余信息置零，提升神经网络在噪声中保留图像细节的能力。

[834] 柯翔.基于半监督机器学习的波阻抗反演方法[D].长安大学,2022.

>本文借鉴深度残差收缩网络的思想，首次将**深度残差模块**应用在卷积神经网络中。

[835] 张黎.深度脉冲神经P系统模型构建[D].西华大学,2022.

>在网络优化方面，尝试了改变了网络结构的层数，用混合膨胀卷积替换膨胀卷积来减少栅格效应的发生以提取更多的数据，引入了**深度残差收缩结构**来学习复杂数据的特征。

[836] 钱若浩.复杂场景下的无人机车辆目标检索[D].西安电子科技大学,2022.

>本文设计的特征提取主干网络借鉴了**深度残差收缩网络**以及Inception V3的设计思想，将注意力机制和**残差收缩网络**以及inception结构进行融合，构造了特征增强模块(FEM)模块...

[837] 关哲欣.基于时频矩阵检测的宽带跳频信号捕获技术[D].西安电子科技大学,2022.

>然后搭建并训练深度学习目标检测网络，利用**残差收缩单元**，提升网络的稳健性，同时降低网络复杂度提高网络的运算速度；

[838] 邓雅文.基于迁移学习的加密恶意流量检测技术研究[D].湖北大学,2022.

>使用**深度残差收缩网络**在CICIDS 2017数据集上进行预训练，对复杂网络环境中产生的大量流量数据进行降噪处理，提高模型对于流量特征的学习能力。将训练完成的**深度残差收缩网络**连接在Inception-v4网络的stem模块之后，组成一个串行网络模型。

[839] 毛浩英.基于数据的航空发动机故障风险预测模型研究[D].南京航空航天大学,2022.

>在模型中融入深度注意力机制网络与**残差收缩块**相结合的子网络，将样本信号在深度注意力机制下软阈值化，有效地抑制了冗余信息。

[840] 喻海霞. 面向图像域轴承故障诊断的深度学习方法研究[D]. 西京学院, 2023.

>针对使用连续小波变换转图像时小波函数选择困难和时间关系弱问题，提出了融合多小波生成图像和基于**残差收缩**TCN时间网络的诊断方法。

[841] 李洪, 万舒, 杨博男, 等. 华龙一号汽辅泵故障诊断系统设计与实现[J]. 电子技术应用, 2023, (S1): 224-228.

>故障诊断模块能够通过**深度残差收缩网络法**，自动识别设备故障原因，为运维人员提供准确的参考信息。

[842] 史宝岱, 徐艳召, 崔俊杰, 等. 基于卷积神经网络的无人机图像自动识别算法[J]. 信息工程大学学报, 2023, 24(05): 526-532.

>首先对**残差收缩网络**进行改进，构建特征提取模块，用自适应K值的一维卷积取代全连接层，并在网络中加入空间注意力，提高阈值提取效率；

[843] 张天瑞, 曲胤熹, 魏希. 基于1DDRSN的轴承故障诊断研究[J]. 机械设计, 2023, 40(06): 58-65.

>针对这一问题，文中提出一种基于一维**深度残差收缩网络**的轴承故障诊断模型，该模型将注意力机制及软阈值化引入残差网络，通过减小冗余信息的干扰，提高特征提取的能力。

[844] 柳彦伊. 基于多模态特征融合的自动调制分类算法研究[D]. 西安电子科技大学, 2023.

>将信号序列通过格拉姆角场编码为二维图像，将其馈入**深度残差收缩网络**以提取图像的高维特征。

[845] 胡博超. 面向安卓平台的恶意软件检测与分类方法研究[D]. 武汉纺织大学, 2023.

>使用改进的**残差收缩网络**、词袋模型等基模型提取多维度特征。

[846] 赵志强.基于深度神经网络的雷达辐射源智能识别算法研究[D].杭州电子科技大学,2023.

>该算法首先采用**深度残差收缩网络**对辐射源信号进行软阈值去噪，以提高输入信号的信噪比;

[847] 王松聿.基于深度学习的低碳钢多层单道GMAW焊缝尺寸预测研究[D].山东大学,2023.

>分别通过残差网络和**残差收缩网络**对图像、电信号进行特征提取，采用特征融合模块实现多信息特征的融合。

[848] 陈作懿.典型欠数据场景下机械装备故障检测与诊断方法研究[D].华中科技大学,2023.

>通过引入**残差收缩网络**，消减噪声干扰和随机波动的影响，捕捉正常状态固有的内在状态信息;

[849] 杨王旺.面向需求响应的居民用电行为分析与时变潜力评估研究[D].华中科技大学,2023.

>利用图像编码技术-格拉姆角场与图像视觉模型-**残差收缩网络**，实现了负荷特征的升维与智能识别

[850] 马贵林.支架-天平一体化测力系统及载荷辨识方法研究[D].西南交通大学,2023.

>提出了一种基于**深度残差收缩网络**的智能载荷辨识技术。

[851] 蒋婧宇.基于深度学习的图像超分辨率重建方法研究[D].西安工业大学,2023.

>在残差子网络中使用由基础残差网络模块进行改进而获得的**深度残差收缩网络**，增设软阈值函数并结合注意力机制，解决了模型中存在噪声相关特征的问题，且能够增强特征提取率、提高模型鲁棒性;

[852] 吴靖.脑电多通道采集技术与伪迹去除方法研究[D].杭州电子科技大学,2023.

>设计了一种基于通道阈值**残差收缩单元**的脑电伪迹分离模块...

[853] 彭海峰.基于深度学习和多维特征提取的信道编码盲识别研究[D].海南大学,2023.

>提出了一种基于**深度残差收缩网络**的信道编码识别器，实现了信道编码的参数识别。

[854] 于广增.基于深度学习的轴承故障检测的研究[D].浙江理工大学,2023.

>为进一步挖掘MCWD的输出特征，搭建了基于**DRSN**-Bi GRU网络的特征提取模块，其中**深度残差收缩网络**DRSN用于分析信号的细节特征，**DRSN**中软阈值化的结构与MCWD结合可以实现多尺度小波分解和自适应滤波。

[855] 贺超,陈进杰,金钊,等.基于多模态时-频特征融合的信号调制格式识别方法[J].计算机科学,2023,50(04):226-232.

>为了进一步提高模型整体的性能，在频域编码器中引入**残差收缩模块**来提取信号时频图的频域特征...

[856] 魏丹.基于光-声耦合技术的大口黑鲈摄食欲望评估模型研究[D].浙江大学,2023.

>结合快速傅里叶变换算法和改进的**深度残差收缩网络**(DRSN-16)实现对鱼群摄食强度的识别与分级。

[857] 巴胤竣,孙文磊,张克战,等.基于CWT-IDRSN的风机滚动轴承故障诊断[J].组合机床与自动化加工技术,2024,(11):166-171.

>提出了一种基于连续小波变换(continuous wavelet transform, CWT)和改进的**深度残差收缩网络**(improved **deep residual shrinkage network**, IDRSN)的故障诊断模型。

[858] 朱宽,余勤.基于多尺度特征融合的调制识别算法[J].计算机应用与软件,2024,41(10):133-139+183.

>提出一种基于多尺度特征融合的**残差收缩网络**(MFRSN)调制识别算法。

[859] 崔萌萌.基于深度学习的电磁信息泄漏信号特征提取方法研究[D].集美大学,2024.

>在编码器与解码器之间加入中间层,中间层是残差单元、注意力机制和软阈值函数组合的**残差收缩单元**...

[860] 李成建.基于Transformer的睡眠呼吸暂停综合征检测方法研究[D].西安理工大学,2024.

>通过由**深度残差收缩网络**、多尺度卷积注意力模块和多层卷积模块组成的时域特征提取器获得时域信息。

[861] 杜甜甜.面向不平衡心电数据的数据增强方法研究[D].齐鲁工业大学,2024.DOI:10.27278/d.cnki.gsdqc.2024.000112.

>通过采用**深度残差收缩网络**、多头注意力机制以及长短期记忆神经网络分别设计了生成器和鉴别器...

[862] 朱荣华.基于深度学习的精子质量辅助诊断技术研究[D].北京邮电大学,2024.

>首先在外观特征度量阶段，提出采用基于**深度残差收缩模块**的深层卷积神经网络（R-DCNN）提取深度特征

[863] 朱乐文.基于改进ResNet的滚动轴承故障识别方法研究[D].安徽理工大学,2024.

>提出了一种结合改进条纹注意力机制和**深度残差收缩网络**(ISAM-Drsnet)的滚动轴承故障诊断模型。

[864] 陈楚凡.基于无监督学习的行人重识别算法研究[D].河北大学,2024.

>并在两个分支中分别嵌入非局部注意力块以及**深度残差收缩块**以提高模型的非局部关注能力以及抑制无关信息干扰的能力...

[865] 李沂阳.基于深度学习的复杂工况轴承故障诊断研究[D].石家庄铁道大学,2024.

>使用残差网络、半软阈值函数、自适应参数化修正线性单元和压缩激励网络构建改进的**残差收缩单元**...

[866] 高越.强噪声条件下基于对抗学习与域迁移的齿轮箱故障诊断方法[D].北京化工大学,2024.

>DSAAN通过引入改进的**残差收缩模块**以实现对于噪声的滤除和故障特征的准确提取...

[867] 吴璟龙.基于变工况和不确定性量化的电主轴剩余寿命预测方法研究[D].吉林大学,2024.

>阐述了**深度残差收缩网络**(**DRSN**)及双向长短时神经网络(Bi LSTM)的基本理论。

[868] 王康.深度残差网络地震波阻抗反演研究[D].长江大学,2024.

>本文提出了一种基于带逐通道阈值的全卷积**残差收缩网络**(FCRSN-CW)的地震波阻抗反演方法。

[869] 阮慧,黄细霞,王乐,等.基于DCGAN与**DRSN**的滚动轴承细粒度故障诊断[J].制造业自动化,2024,46(04):79-86.

>提出一种基于深度生成对抗网络（Deep Convolutional Generative Adversarial Networks，DCGAN）和**深度残差收缩网络**（**Deep Residual Shrinkage Networks**，**DRSN**）的滚动轴承细粒度故障诊断方法。

[870] 陈佳琳,尚志武,张雷.基于IDRSN-BiLSTM的铣削加工表面粗糙度预测方法[J].仪器仪表学报,2024,45(04):27-36.

>利用**深度残差收缩网络**(**DRSN**)中软阈值化结构和注意力机制对输入信号进行降噪处理。

[871] Ma X, Hu H, Shang Y. A new method for transformer fault prediction based on multifeature enhancement and refined long short-term memory[J]. IEEE Transactions on Instrumentation and Measurement, 2021, 70, 1-11.

>First, this study constructs a cross-entropy loss function with variable thresholds and dynamic weights to reduce error transmission in the **deep residual shrinkage network**, enhancing the sensitivity of the normal and abnormal transformer states by the network. Second, the multiobjective particle swarm algorithm and random walk strategy are adopted to optimize the long short-term memory (LSTM) network to ensure the prediction model's objectivity. Finally, the improved subchannel threshold depth **residual shrinkage network** is integrated with the optimized LSTM network.

[872] Hu J, Li W, Zheng X, et al. Prior knowledge-based residuals shrinkage prototype networks for cross-domain fault diagnosis[J]. Measurement Science and Technology, 2023, 34(10), 105011.

> First, our method combines general supervised learning and metric meta-learning to extract prior knowledge from the labeled source data by utilizing a denoised **residual shrinkage network**.

[873] Shu Y, He C, Qiao L, et al. Vibration Control with Reinforcement Learning Based on Multi-Reward Lightweight Networks[J]. Applied Sciences, 2024, 14(9), 3853. 

>This paper proposes a reinforcement learning method using a **deep residual shrinkage network** based on multi-reward priority experience playback for high-frequency and high-dimensional continuous vibration control.

[874] Meng Y, Xu H, Ma Z, et al. Detail-semantic guide network based on spatial attention for surface defect detection with fewer samples[J]. Applied Intelligence, 2023, 53(6), 7022-7040.

>In the first stage, we design a new semantic branch based on the modified **residual shrinkage network** and the proposed joined atrous spatial pyramid pooling (JASPP) module. This is the first time that **residual shrinkage network** is applied to defect detection and achieves good results.

[875] Liu F, Li W, Wu Y, et al. Fault Diagnosis of Imbalance and Misalignment in Rotor-Bearing Systems Using Deep Learning[J]. Polish Maritime Research, 2024, 31(1), 102-113.

>In this paper, a fault diagnosis method based on an improved **deep residual shrinkage network** (IDRSN) is proposed with the aim of achieving end-to-end fault diagnosis of a rotor-bearing system.

[876] Tao L, Liu H, Zhang J, et al. Associated fault diagnosis of power supply systems based on graph matching: a knowledge and data fusion approach[J]. Mathematics, 2022, 10(22), 4306.

>To this end, this paper proposes a graph-matching approach for the associated fault diagnosis of power supply systems based on a **deep residual shrinkage network**.

[877] Sun C, Xue M, Zhao N, et al. A Deep Learning Method for NLOS Error Mitigation in Coastal Scenes[J]. Journal of Marine Science and Engineering, 2022, 10(12), 1952.

>We employed data augmentation and a **deep residual shrinkage network** in order to alleviate the adverse effects of NLOS errors.

[878] Zhang H, Zhou F, Wu Q, et al. SSwsrNet: A Semi-Supervised Few-Shot Learning Framework for Wireless Signal Recognition[J]. IEEE Transactions on Communications. 2024.

>To overcome this challenge, a novel SSwsrNet framework is proposed by using the **deep residual shrinkage network** (**DRSN**) and semi-supervised learning.

[879] Song Z, Qing X, Zhou M, et al. Mine underground object detection algorithm based on TTFNet and anchor-free[J]. Open Computer Science, 2024, 14(1), 20240015.

>First, CenterNet and TTFNet algorithms are introduced, then pooling is introduced into CSPNet basic structure to design a lightweight feature extraction network, at the same time optimizing the feature fusion way in the original algorithm, optimizing **residual shrinkage network** structure, and introducing it into object detection task.

[880] Wu Z, Jiang C, Jiang F, et al. An improved displacement sensor accuracy calibration method for ball screw positioning error compensation[J]. IEEE Sensors Journal. 2024.

>In this article, an ultrasonic sensor accuracy calibration method is proposed, namely, frequency feature extraction **deep residual shrinkage network** (FFE-DRSN), which used probability statistics and test data to enhance the resolution of ultrasonic sensors.

[881] Dianqing Y, Yanping M. Remote sensing landslide target detection method based on improved Faster R-CNN[J]. Journal of Applied Remote Sensing, 2022, 16(4), 044521-044521.

>Finally, multiscale feature fusion is performed by adding a feature pyramid network structure to optimize the extracted landslide small target features, and then the backbone network is set as **deep residual shrinkage network** 50 to make the model more focused on information useful for landslide detection.

[882] Zhang Z, Zhang C, Zhang X, et al. A self-adaptive DRSN-GPReLU for bearing fault diagnosis under variable working conditions[J]. Measurement Science and Technology, 2022, 33(12), 124005.

>To solve this problem, a self-adaptive **deep residual shrinkage network** with a global parametric rectifier linear unit (DRSN-GPReLU) is proposed in this paper.

[883] 刘国伟, 陈历, 许建远, 等. 环网柜的局部放电信号的故障识别方法、装置和系统[P]. 广东省:CN202411445500.6, 2024-11-15.

>该网络模型结构主要包含输入层、卷积层（Conv）、多个串接的通道级阈值**残差收缩块**（RBU）、批量归一化（BN）、激活函数（ReLU）...

[884] 薛庆生,韩轩,于布为,等.一种麻醉深度评估方法、装置、电子设备及存储介质[P].江苏省:CN202411067536.5,2024-09-03.

>可以选取性能最先进技术（State‑of‑the‑art，SOTA）的用于进行麻醉深度评估的方法，例如可以选取可解释的预测（Interpretable Forecasts）BIS、**深度残差收缩**卷积网络（**DRSN**‑CW‑CON）与混合网络（CombineNET）...

[885] 高雪瑶,张澐凯,张春祥.三元组网络的多视图特征融合三维模型分类方法[P].黑龙江省:CN202410813063.2,2024-09-24.

>视图特征提取网络**DRSN**包括：输入层、8个基本**残差收缩模块**、批归一化层、全局池化以及全连接层，其中，基本**残差收缩模块**由2个卷积层、2个批归一化、1个ReLU激活函数、1个恒等映射以及1个阈值学习子网络组成；

[886] 司乔瑞,宣以鹏,王鹏,等.一种一体化污水处理设备的MBR膜池加热温度控制系统[P].江苏省:CN202410631984.7,2024-07-16.

>构建引入**残差收缩模块**的深度残差神经网络模型；

[887] 赵明华,董爽爽,都双丽,等.基于光流特征的微表情识别方法[P].陕西省:CN202211509095.0,2023-04-07.

>在Conv1后面连接两个**残差收缩模块**RSBlock1和RSBlock2，以增强神经网络的抗噪能力；两个**残差收缩模块**后面添加了一个融合通道注意力机制的残差块ARBlock...

[888] 张俊峰,张扬,赵彬宇,等.一种态势估计方法及装置[P].北京市:CN202211427335.2,2023-06-09.

>将自适应阈值块加入到残差网络中改进为**残差收缩模块**，从而达到剔除或减弱噪声的目的。

[889] 梁振虎,孟林源,王长津.基于TB-TF-BiGRU模型处理脑电波信号的睡眠监测方法[P].江苏省:CN202210899835.X,2022-11-01.

>映射函数包含一个卷积层，Q个改进的DRSM(**深度残差收缩**)层和平均池化层；

[890] 朱明甫,倪水平,宋成,等.一种禁停区域违章停车监测方法[P].河南省:CN202210944314.1,2022-11-04.

>优选连续使用6个**残差收缩单元**对每个输入的图像对反复进行6次去噪声处理，得到去除大部分噪声的高质量图像对；

[891] 李参宏,韩平军,徐翠兰.一种基于深度学习的算力资源空闲预测方法和存储介质[P].江苏省:CN202310603689.6,2024-05-17.

>将自适应阈值块加入到残差网络中改进为**残差收缩模块**，从而达到剔除或减弱噪声的目的。

[892] 谢自磊,叶刚,闫东锋.一种具有防辐射功能的医用自动门控制系统[P].广东省:CN202310752675.0,2023-07-25.

>最后由**深度残差收缩模块**的三个不同检测头进行图像中的人体识别。

[893] 房建东,刘帆,赵于东.课堂参与度评价方法及系统[P].内蒙古自治区:CN202210580416.X,2022-11-08.

>所述预设目标检测算法还包括时空**残差收缩算法**；

[894] 吴勇,柯晨怡,陈晞,等.区域风险识别方法、装置、设备及存储介质[P].上海市:CN202211658951.9,2023-04-25.

>在上述实施例的基础上，可以通过使用**深度残差收缩神经网络**(**DRSN**)，进行区域风险特征的提取。其中，**深度残差收缩神经网络**中可以包括全局池化层和卷积层。**深度残差收缩神经网络**可以将深度学习注意力机制和降噪阈值的确定相结合，形成了降噪阈值的动态确定。具体的，**深度残差收缩神经网络**通过注意力机制生成权重系数，并将权重系数与全局池化层输出的初始特征数据相乘，得到降噪阈值...

[895] 李宁,王赞,毋琳,等.基于多域信息融合网络的雷达有源干扰识别方法、系统、存储装置和电子设备[P].河南省:CN202410857768.4,2024-10-29.

>维神经网络通过半软阈值**残差收缩块**提取时域特征，二维神经网络通过多尺度卷积块、空间注意力CBAM提取时频域特征，损失函数设定为交叉熵与三元组联合函数。

[896] 张哲,李伟.集成多源信息融合智能故障判断方法[P].江苏省:CN202410847643.3,2024-10-29.

>所述双流网格由动态卷积网络模块、**残差收缩模块**、通道注意力模块、交叉注意力模块、Dropout层和下采样层组成。

[897] 高海静,方勇军,赵海,等.一种考虑城镇化进程与气候变化的设计暴雨修正方法及系统[P].浙江省:CN202410888112.9,2024-09-24.

>所述残差长短期记忆网络包括输入层、全连接层、**残差收缩层**、全连接层、LSTM层、隐藏层、全连接层和输出层；

>所述**残差收缩层**中利用自适应阈值函数进行优化

[898] 朱波,李劲魁,马君亮.一种共享车辆的防超载方法、装置及电子设备[P].浙江省:CN202110476740.2,2021-07-20.

>在本实施例中，可以使用**残差收缩神经网络**、卷积神经网络和多层感知神经网络等等构建本实施例中的神经网络模型...

[899] Zhong Z, Liu H, Mao W, et al. Imbalanced bearing fault diagnosis based on RFH-GAN and PSA-DRSN[J]. IEEE Access, 2023, 11, pp.131926-131938.

>To address this issue, we propose employing a residual factorized hierarchical search-based generative adversarial network (RFH-GAN) and a **residual shrinkage network** with pyramidal squeezed attention (PSA-DRSN) for unbalanced fault diagnosis.

[900] Zeng L, Jian J, Chang X, et al. A meta-learning method for few-shot bearing fault diagnosis under variable working conditions[J]. Measurement Science and Technology, 2024, 35(5), p.056205.

>In this approach, a **deep residual shrinkage network** is employed to extract salient features from bearing vibration signals.

[901] Feng Q, Zhang J, Chen L, et al. Waveform Reconstruction of DSSS Signal Based on VAE‐GAN[J]. Wireless Communications and Mobile Computing, 2022(1), p.3667592.

>In this method, the **deep residual shrinkage network** (**DRSN**) and self‐attention mechanism are added to the encoder and discriminator of VAE‐GAN.

[902] Li K, Chen M, Lin Y, et al. A novel adversarial domain adaptation transfer learning method for tool wear state prediction[J]. Knowledge-Based Systems, 2022, 27;254:109537.

>Firstly, the dual-path **deep residual shrinkage network** was used to extract the tool wear multiscale sensitive features from the spindle vibration signals.

[903] Liu S, Chen Z, Yuan L, et al. State of health estimation of lithium-ion batteries based on multi-feature extraction and temporal convolutional network[J]. Journal of Energy Storage, 2024, 75, p.109658.

>Concurrently, to enhance the adaptive threshold training ability of the model with multiple input parameters, a **residual shrinkage network** was introduced.

[904] Wang H, Pan X, Zhu Y, et al. Maize leaf disease recognition based on TC-MRSN model in sustainable agriculture[J]. Computers and Electronics in Agriculture, 2024, 221, p.108915.

>Focusing on the accurate recognition of maize leaf diseases in complex backgrounds, this paper proposes a texture-color dual-branch multiscale **residual shrinkage network** (TC-MRSN) model based on deep learning.

[905] Qu N, Wei W, Hu C.Series arc fault detection based on multimodal feature fusion[J]. Sensors, 2023, 23(17), p.7646.

>Finally, an arc fault detection model is constructed based on a one-dimensional convolutional network and a **deep residual shrinkage network** to achieve high accuracy.

[906] Guo J, Lu L, Li J.Smart Contract Vulnerability Detection Based on Multi-Scale Encoders[J]. Electronics, 2024, 13(3), p.489.

>Finally, to focus the model’s attention on vulnerability-related characteristics, we employ the **Deep Residual Shrinkage Network** (**DRSN**).

[907] Hu C, Qu N, Zhang S. Series arc fault detection based on continuous wavelet transform and DRSN-CW with limited source data[J]. Scientific Reports, 2022, 12(1), p.12809.

>In order to solve this problem, an arc fault detection method based on continuous wavelet transform and **deep residual shrinkage network** with the channel-wise threshold (DRSN-CW) is proposed.

[908] Xu X, Deng R, Zhao G, et al. Deep Domain Generalization-Based Indoor Pedestrian Identification Using Footstep-Induced Vibrations[J]. IEEE Transactions on Instrumentation and Measurement, 2024.

>Second, a **deep residual shrinkage network** (**DRSN**) specially designed for noise component suppression is used as a backbone network to automatically extract features.

[909] Chinnappan B, Hakim K, Kumar NS et al. Blockchain and IoT integration for secure short-term and long-term air quality monitoring system using optimized neural network[J]. Environmental Science and Pollution Research, 2024, pp.1-16.

>Predictions utilize Graph attention-based **deep Residual shrinkage Network** and Bidirectional long short Term Memory (GRNBTM) categorized into five levels.

[910] Liu J, Qu Q, Yang H, et al. Deep learning-based intelligent fault diagnosis for power distribution networks[J]. International Journal of Computers Communications & Control, 2024, 19(4).

>Second, a fusion **deep residual shrinkage network** (FDRSN) is integrated with IBES and support vector machine (SVM) to form the FDRSN-IBS-SVM model for fault identification.

[911] Fu Z, Zhou Z, Yuan Y. Fault diagnosis of wind turbine main bearing in the condition of noise based on generative adversarial network[J]. Processes, 2022, 10(10), p.2006.

>this article proposes a double-layer fault diagnosis model for the main bearing of the wind turbine that combines the auxiliary classifier generation adversarial network (ACGAN) and the **deep residual shrinkage network** (**DRSN**).

[912] Zhang X, Li J. SDCSN: a hierarchical parallel localization method for pipeline leakage based on vibration signals. Measurement Science and Technology, 2024, 36(1), p.016158.

>Moreover, implementing the **residual shrinkage building unit** module for noise reduction in the network architecture.

[913] Liu H, Wang J, Liu S, et al. Study on Soil Total Nitrogen Content Prediction Method Based on Synthetic Neural Network Model[J]. Sustainability, 2024, 16(8), p.3195.

>a new method of soil total nitrogen content detection based on convolutional noise reduction autoencoder (CDAE)-whale optimization algorithm (WOA)-**deep residual shrinkage network** (**DSRN**) is proposed.

[914] Li L, Li Y, Zhang J. A hybrid remaining useful life prediction method for lithium-ion batteries based on transfer learning with CDRSN-BiGRU-AM[J]. Measurement Science and Technology, 2024, 35(5), p.056124.

>This method first employs a channel-wise **deep residual shrinkage network** to adaptively extract features from input data enhancing important information features and suppressing ineffective ones based on the significance of the feature information.

[915] Xue T, Ma P. TC-net: transformer combined with cnn for image denoising[J]. Applied Intelligence, 2023, 53(6), pp.6753-6762.

>Ingeniously adding a **deep residual shrinkage network** into a transformer block improves the networks ability to deal with noise and its robustness in complex scenes.

[916] Yin L, Xiang X, Liu K, et al. Specific Emitter Identification Based on a Hybrid Deep Neural Network for ACARS Authentication[J]. Wireless Communications and Mobile Computing, 2022(1), p.4748519.

>Our deep learning architecture is a combination of **Deep Residual Shrinkage Network** (**DRSN**), Bidirectional-LSTM (Bi-LSTM), and attention mechanism (AM), which perform the functions of local and global feature learning and feature focusing, respectively, so that the individual information hidden in the signal waveform can be thoroughly mined.

[917] Shi B, Zhang Q, Wang D, et al. Synthetic aperture radar SAR image target recognition algorithm based on attention mechanism[J]. IEEE Access, 2021, 9, pp.140512-140524.

>First, use dual-channel one-dimensional convolution to reconstruct the **residual shrinkage network** to construct a lightweight and efficient feature module, which improved the information extraction of the module with the consumption of a small amount of computing resources.

[918] Su Z, Yu J, Xiao X, et al. Deep learning seismic damage assessment with embedded signal denoising considering three-dimensional time–frequency feature correlation[J]. Engineering Structures, 2023, 286, p.116148.

>We propose a novel deep learning framework, DRSNet (**deep residual shrinkage network**), which incorporates the CNN structure of ResNet and a soft-threshold denoising module for simulta-neous seismic signal denoising and damage assessment.

[919] Zhang A, Li Y, Wang S. 2DDSRU-MobileNet: an end-to-end cloud-noise-robust lightweight convolution neural network[J]. Journal of Applied Remote Sensing, 2024, 18(2), pp.024511-024511.

>Then using the idea of a **deep residual shrinkage network**, we construct a two-dimensional deep shrinkage residual unit (2DDSRU). 

[920] Li Y, Wang R, Mao R, et al. A Fault Diagnosis Method Based on an Improved Deep Q-Network for the Inter-Turn Short Circuits of a Permanent Magnet Synchronous Motor[J]. IEEE Transactions on Transportation Electrification, 2023.

>A 1-D **deep residual shrinkage network** and the prioritized experience replay (PER) strategy are introduced into the original network structure, and the sampling strategy of the original network is optimized.

[921] Zou X, Yin Z, Li Y, et al. Novel multiple object tracking method for yellow feather broilers in a flat breeding chamber based on improved YOLOv3 and deep SORT[J]. International Journal of Agricultural and Biological Engineering, 2023, 16(5), pp.44-55.

>The **DRSN** (**Deep Residual Shrinkage Network**) was integrated with MobileNetV2 to enhance the feature extraction capability of the network.

[922] Li S, Ma G, Gao H, et al. A new aerodynamic identification technology for short-time hypersonic wind tunnels while considering inertial force interference. Aerospace Science and Technology, 2023, 138, p.108310.

>Therefore, this study develops a novel intelligent aerodynamic identification method based on **deep residual shrinkage network** (**DRSN**) deep learning technology and applies this method to aerodynamic force tests in hypersonic wind tunnels.

[923] Yan J, Shi M, Lv X, et al. An Inversion Method for Coupled Typical Error Sources based on Remote Sensing Image. Journal of Imaging Science & Technology, 2022, 66(6).

>The initial values of coupled typical error sources are subsequently determined based on the Deep Residual Shrinkage Network (DRSN).

[924] Lu W, Gao L, Cao H, et al. A comparison of contributions of individual muscle and combination muscles to interaction force prediction using KPCA-DRSN model. Frontiers in Bioengineering and Biotechnology, 2022, 10, p.970859.

>After that, the processed sequence is fed into the **Deep Residual Shrinkage Network** (**DRSN**) to predict the interaction force.

[925] Huang X, Liu Y, Qi X, et al. Intelligent Classification of Metallographic Based on Improved Deep Residual Efficiency Networks[J]. International Journal of Pattern Recognition and Artificial Intelligence, 2024, 38(03), p.2452008.

>In addition, a **deep residual shrinkage network** model based on an attention mechanism is proposed.

[926] Fan F, Zhang M, Yu D, et al. Lightweight Context Awareness and Feature Enhancement for Anchor-Free Remote Sensing Target Detection[J]. IEEE Sensors Journal, 2024.

>Second, we proposed that ELAN-RSN uses an optimized **residual shrinkage network** (**RSN**) to eliminate background noise and conflicting information in the multiscale feature fusion.

[927] Liu Z, Zhang L, Xiao Q, et al. Performance Degradation Assessment of Railway Axle Box Bearing Based on Combination of Denoising Features and Time Series Information[J]. Sensors, 2023, 23(13), p.5910.

>To solve the above problems, an end-to-end performance degradation assessment model of railway axle box bearing based on a **deep residual shrinkage network** and a deep long short-term memory network (DRSN-LSTM) is proposed.

[928] Yan J, Hu X, Zhang K, et al. Detection of Dim Small Ground Targets in SAR Remote Sensing Image based on Multi-level Feature Fusion[J]. Journal of Imaging Science & Technology, 2023, 67(1).

>Cross-level feature fusion is then performed on the spatial pyramid of feature maps, combined with the constructed soft thresholding module which adopts **DRSN** (**Deep Residual Shrinkage Network**)...

[929] Shi H, Gan C, Zhang X, et al. A fault diagnosis method for rolling bearings based on RDDAN under multivariable working conditions[J]. Measurement Science and Technology, 2022, 34(2), p.025003.

> Secondly, a **deep residual shrinkage network** is used for noise reduction and feature extraction.

[930] Hu B, Hao Z, Chen Z, et al. Combination with Continual Learning Update Scheme for Power System Transient Stability Assessment[J]. Sensors, 2022, 22(22), p.8982.

>A **deep residual shrinkage network** (**DRSN**) is selected as a classifier to construct the TSA model of SCP-DRSN at the same time.

[931] Xu D, Li M, Wu Y, et al. Dual Attention-Based Global-Local Feature Extraction Network for Unsupervised Change Detection in PolSAR Images[J]. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2024.

>Subsequently, our DA-GLN utilizes a **deep residual shrinkage network** that incorporates channel attention mechanisms and soft-thresholding to weaken the influence of speckle noise and capture local features.

[932] Wang M, Rao C, Xiao X, et al. Efficient shrinkage temporal convolutional network model for photovoltaic power prediction[J]. Energy, 2024, 297, p.131295.

>This paper presents an Efficient Shrinkage Temporal Convolutional Network (ESTCN) model, which combines the Temporal Convolutional Network (TCN) and an improved **Deep Residual Shrinkage Network** (**DRSN**) to forecast PV power output.

[933] Wang X, Hao Z, Chen Z, et al. Joint prediction of Li-ion battery state of charge and state of health based on the DRSN-CW-LSTM model[J]. IEEE Access, 2023.

> Then we use the data information of Lithium battery voltage, current, temperature, and capacity in the **deep residual shrinkage network** for feature extraction...

[934] Zhang R, Yi J, Tang H, et al. Fault Diagnosis Method of Waterproof Valves in Engineering Mixing Machinery Based on a New Adaptive Feature Extraction Model[J]. Energies, 2022, 15(8), p.2796.

>This fault diagnosis method is based on a new adaptive feature extraction model, with multi-path signals to the improved **deep residual shrinkage network**-stacked denoising convolutional autoencoder (named DRSN-SDCAE).

[935] Muthusamy C.D, Murugesh R. Integrated deep learning approach for automatic coronary artery segmentation and classification on computed tomographic coronary angiography[J]. Network Modeling Analysis in Health Informatics and Bioinformatics, 2024, 13(1), p.39.

>Finally, the improved **deep residual shrinkage network** (IDRSN) model classifies heart blood vessels into four distinct classes: normal, block, narrow, and blood flow-reduced.

[936] Hu J, Zhang Y, Li W, et al. Trustworthy Artificial Intelligence Based on an Explicable Temporal Feature Network for Industrial Fault Diagnosis[J]. Cognitive Computation, 2024, 16(2), pp.534-545.

>First, adaptive features extracted from the improved **deep residual shrinkage network** are combined with empirical features to increase the robustness of the model.

[937] Sun X, Liu J, Qian Y. Enhancing Emotion Recognition in College Students' Online Learning: A Research on Integrating Feature Fusion and Attention Mechanisms[J]. Traitement du Signal, 2024, 41(1).

>then, by combining the channel attention mechanism and soft thresholding to improve the ResNet network, a **Deep Residual Shrinkage Network** (**DRSN**) is constructed to achieve emotion recognition of college students' online learning

[938] Liang H, Shen H, Liu P, et al. Deep learning for sub-Nyquist sampling scanning white light interferometry. Optics Letters, 2023, 48(22), pp.5976-5979.

>The method designs Envelope-**Deep Residual Shrinkage Networks** with channel-wise thresholds (E-DRSN-cw), a network model extracting oversampling envelopes from under sampled signals.

[939] Chen C, Liang R, Song M, et al. Noise-assisted data enhancement promoting image classification of municipal solid waste. Resources, Conservation and Recycling, 2024, 209, p.107790.

>this paper examined the potential of noise-assisted data enhancement methods on two representative MSW classification models: Convolutional Neural Networks (CNN) and **Deep Residual Shrinkage Networks** (**DRSN**)...Notably, **DRSN** demonstrated exceptional robustness under noise conditions, achieving over 90 % accuracy in training and test sets.

[940] Zhang S, Zhang Y, Ma M, et al. GAN-SNR-shrinkage-based network for modulation recognition with small training sample size[C]. In International Conference on Communications and Networking in China (pp. 80-90).

>In addition, a preprocessing module and **residual shrinkage networks** are used to improve the capability of characterizing signal features and the anti-noise performance.

[941] He S, Zhu L, Li H, et al. Cross-condition quantitative diagnosis method for bearing faults based on IDRSN-ECDAN[J]. Measurement Science and Technology, 2023, 35(2), p.025129.

>Therefore, in this work, a cross-condition quantitative diagnostic method for estimating the bearing faults based on an improved **deep residual shrinkage network**-entropy conditional domain adversarial network (IDRSN-ECDAN) was proposed. First, a sub-network was added to the residual module to construct a **residual shrinkage module**, which reduced the noise interference in vibration signals. Next, DropBlock layers were added to the **deep residual shrinkage network**...

[942] Wang H, Chen X, Liu C. Pose-guided part matching network via shrinking and reweighting for occluded person re-identification[J]. Image and Vision Computing, 2021, 111, p.104186.

>so we utilize the **Deep Residual Shrinkage Module** (DRS Module) to eliminate un-important features by automatically determining the soft thresholds.

[943] Li C, Shi Z, Zhou L, et al. Tfformer: A time frequency information fusion based cnn-transformer model for osa detection with single-lead ecg[J]. IEEE Transactions on Instrumentation and Measurement, 2023.

>To address this problem, this article presents a time-frequency information fusion-based CNN-Transformer model (TFFormer) for OSA detection with single-lead ECG, in which a module consisting of a **deep residual shrinkage module**, a multiscale convolutional attention (MSCA) module, and a multilayer convolution module is developed for time-frequency feature extraction.

[944] Li S, Zhang C, Zhang X. A Novel Spatio-Temporal Enhanced Convolutional Autoencoder Network for Unsupervised Health Indicator Construction[J]. IEEE Transactions on Instrumentation and Measurement, 2024.

>SMM enhances the deep mining of local spatial features via **deep residual shrinkage module**.

[945] Kang S, Liang X, Wang Y, et al. Few-shot rolling bearing fault classification method based on improved relation network[J]. Measurement Science and Technology, 2022, 33(12), p.125020.

>The **residual shrinkage module** and the scaled exponential linear unit activation function are introduced into the embedding module of the RN.

[946] Wang L, Xie K. Multi‐function radar work mode recognition based on residual shrinkage reconstruction recurrent neural network[J]. IET Radar, Sonar & Navigation, 2024.

> A **residual shrinkage module** with one‐dimensional convolution is integrated into the temporal classification network,combining the strengths of both RNN and CNN architectures.

[947] Zhang B, Zhang J, Yu P, et al. Asymmetric-Based Residual Shrinkage Encoder Bearing Health Index Construction and Remaining Life Prediction[J]. Sensors, 2024, 24(20), p.6510.

>The encoder component comprises two convolutional layers, two **residual shrinkage modules**, and a fully connected module.

[948] 杜亦康. 《第三章 **深度残差收缩网络**与自注意力机制理论概述》基于混合建模方法的ETF期权定价研究[D]. 上海财经大学, 2022.

>具体而言,将**深度残差收缩网络**(**DRSN**)、自注意力机制(Self-attention)以及滑动平均(Moving-average)方法结合,构建DRSN-SA-smooth模块,利用该模块对Black-Scholes模型和Heston模型的定价偏差进行预测,将预测偏差与Black-Scholes模型和Heston模型的原始定价结果相加,得到更符合市场实际交易情况的期权定价。

[949] 徐圆, 廖恒伟, 贺彦林, 等. 改进的**深度残差收缩网络**滚动轴承故障诊断方法[C]//第35届中国过程控制会议, 2024.

[950] 张浩, 周福辉, 丁家昕, 等. 一种小样本无线信号半监督智能精确识别方法[P]. 江苏省: CN202410938132.2, 2024-12-13.

>所述残差堆叠模块包括依次连接的1×1内核的卷积层、两个**残差收缩单元**和最大池化层...

[951] 王蕾, 吴飞, 刘晓庆, 等. 一种融合语义和句法信息的实体关系抽取方法[P]. 吉林省: CN202411232854.2, 2024-12-13.

>使用自注意力池化层的图卷积神经网络与**残差收缩网络**减少文本中噪声的影响，提升实体间长距离依赖。

[952] 蔡铮印.《5.3.1 多尺度混合域空洞**残差收缩模块**》基于振动信号处理与机器学习的滚动轴承故障诊断研究[D]. 黑龙江大学, 2024.

[953] 池福临, 杨新宇, 邵思羽, 等. 基于深度收缩残差网络的轴承变工况故障诊断[J]. 计算机集成制造系统, 2023, 29(04): 1146-1156.

>本文将在**深度残差收缩网络**的基础上，通过改良其中部分网络结构实现迁移学习骨干网络的搭建。

[954] 竹杭杰.《第三章 基于**DRSN**的通信信号调制方式识别》《3.1 **深度残差收缩网络**》基于深度学习的通信信号调制方式识别与实现[D]. 西京学院, 2023.

>应用**深度残差收缩网络**模型，结合软阈值化和注意力机制提取出调制信号的多种特征...

[955] 丁佳俊.《4.1.1 **残差收缩网络**》神经网络在雷达辐射源信号识别中的应用研究[D]. 江南大学, 2022.

>该算法充分利用**残差收缩网络**优越的特征提取和去噪能力、Bi-LSTM 的时序序列的处理能力...

[956] 刘凯.《第4章 一种混合**深度残差收缩网络**与XGBoost算法的故障诊断方法》基于深度学习的工业过程故障诊断方法研究[D]. 杭州电子科技大学, 2022.

[957] 田宝华.《5.3 **残差收缩网络**结构》基于卷积神经网络的滚动轴承故障诊断研究[D]. 内蒙古科技大学, 2023.

[958] 李进. 基于深度神经网络模型的地震信号识别研究[D]. 河北地质大学, 2021.

>将***残差收缩模块***和残差多尺度模块加入卷积神经网络之后，模型在训练集和测试集上的准确率较QConvNet模型增长了约7个百分点...

[959] 翁敏超.《第三章 基于**深度残差收缩网络**的齿轮箱故障诊断方法研究》基于粒子群优化和改进深度残差网络的齿轮箱故障诊断研究[D]. 昆明理工大学, 2023.

[960] 许金鹏. 基于数据驱动的复杂工业软测量建模方法研究[D]. 西北师范大学, 2023.

>提出了基于贝叶斯优化的多注意力**深度残差收缩网络**（BO-MADRSN）软测量建模方法，在**残差收缩网络**的基础上在支路添加了多注意力融合模块...

[961] 曾诚. 基于态势感知的城市轨道交通短时进站客流预测研究[D]. 西南交通大学, 2022.

>对有特征条件下的特征学习问题，基于压缩-激发模块和**残差收缩模块**，设计深度学习预测框架。 

[962] 肖品宏. 射频指纹无监督盲识别方法设计与实现[D]. 电子科技大学, 2023.

>本文设计实现了**残差收缩网络**，能够学习到一组阈值，并将阈值用于对特征的收缩...

[963] 田锐. 基于深度学习的滚动轴承剩余寿命预测[D]. 大连交通大学, 2022.

>此本章针对含噪声数据的处理，提出了多尺度堆叠**深度残差收缩网络**...

[964] 晏子锐. 基于深度学习的深度伪造检测算法研究[D]. 西南财经大学, 2023.

>设计一种基于扩散过程的噪声添加模块对数据进行增强，并利用**深度残差收缩结构**降低数据噪声使模型提取到更为准确的特征。 

[965] 张杰.《4.4.3 **深度残差收缩网络**》基于Anchor-Free的钢条实时检测研究及应用[D]. 重庆大学, 2022.

[966] 梁瀚钢. 自适应白光干涉包络提取方法研究[D]. 中国科学院大学(中国科学院长春光学精密机械与物理研究所), 2024.

>我们基于该网络结构提出了一种名为具有信道阈值的包络-**深度残差收缩网络**（Envelope-Deep ResidualShrinkage Networks with channel-wise thresholds, E-DRSN-cw）的新型结构...

[967] 吕浩原. 基于深度学习的非接触式心率检测系统研究[D]. 东北石油大学, 2023.

>将空间软阈值注意力模块和DRSN-CW通道软阈值注意力模块并行融入**残差收缩模块**...

[968] 林薇. 基于代码特征学习的软件漏洞检测方法研究[D]. 江苏大学, 2022.

>针对源代码中存在大量与漏洞关联性不足的语句的特点以及源代码作为文本所具有的双向性的特点，融合**深度残差收缩网络**(**Deep Residual Shrinkage Networks**，**DRSN**)和TCN...

[969] 徐晓文. 暗视觉图像边缘检测方法研究[D]. 重庆邮电大学, 2022.

>本论文研究的转换器结构使用**深度残差收缩网络**代替残差网络，并将转换器设计成多分支的网络结构。

[970] 董绍江, 刘文龙, 方能炜, 等. 基于HTMFDE以及ICNN的滚动轴承寿命状态识别方法[J]. 铁道科学与工程学报, 2023, 20(02): 723-734.

>本文提出改进卷积神经网络的轴承寿命状态识别模型，采用双层多通道卷积提取特征，通过**残差收缩模块**以及注意力模块，筛选有用特征，滤除无用特征，有效地增强了模型在噪声环境下的鲁棒性。

[971] 吴懿范. 基于盲源分离与深度神经网络的1000MW火电机组低频振动故障诊断研究[D]. 浙江大学, 2022.

>使用**残差收缩模型**与注意力强化机制模型对深度神经网络进行改进与优化，优化深度网络的传播方式，增强深度网络的恒等映射性能...

[972] 梁栋. 基于动力学仿真数据的双源域自适应滚动轴承故障诊断研究[D]. 北京化工大学, 2024.

>本文所用的公共特征提取器则由多个这样的**残差收缩模块**堆叠而成。 

[973] 朱新丽, 才华, 寇婷婷, 等. 行人多目标跟踪算法[J]. 吉林大学学报(理学版), 2021, 59(05): 1161-1170.

>在检测模块中添加了**深度残差收缩网络**（**DRSN**），使网络模型引入了软阈值函数，并将其作为非线性层，以增强深度学习方法对含噪声数据或复杂数据的特征学习效果...

[974] 闫佳丽. 基于cbow和深度学习的数据竞争检测方法研究[D]. 河北科技大学, 2023.

>本文提出一种基于**DRSN**（**深度残差收缩网络**）与GRU（门控循环单元）的数据竞争检测新方法。

[975] 汪文斌. 基于SwinTransformer的片状颗粒厚度检测[D]. 西南科技大学, 2024.

>同时为了提取到更加精细的特征，在骨干网络的末端使用**深度残差收缩网络**(**Deep Residual Shrinkage Network**，**DRSN**)。

[976] 崔菲凡. 家用低压交流串联故障电弧诊断方法研究[D]. 辽宁工程技术大学, 2023.

>针对构建的图片数据集，使用具有并联卷积的Inception网络与含有通道注意力机制的**DRSN**相结合的方法来充分挖掘图片样本特征量，该引入了软阈值化作用的算法具备从带有噪声的数据中直接进行特征提取和分类的能力。

[977] Ma H, Li T, Fu M, et al. An Intrusion Detection Model of Incorporating Deep Residual Shrinking Networks for Power Internet of Things. In International Conference on Intelligent Computing (pp. 479-490). 2024.

>To address the aforementioned issues, this paper proposes a new intrusion detection model for power Internet of Things systems, which comprehensively utilizes **Deep Residual Shrinkage Network** (**DRSN**), SMOTE algorithm, and Generative Adversarial Network (GAN) to improve the effectiveness of data processing and feature extraction.

[978] Yin H, Xu H, Zhao Y, et al. Fault Diagnosis of Control Valve Based on Fusion of Deep Learning and Elastic Weight Consolidation. BATH/ASME Symposium on Fluid Power and Motion Control (FPMC), 2022.

>Therefore, this paper proposed a fusion of elastic weight consolidation algorithm and **residual shrinkage network** method, sharing common feature layers.

[979] 段卓然.《第三章基于时频注意力机制的双通道**残差收缩模型**的调制识别方法》基于深度学习的多制式通信信号盲识别技术研究[D]. 北京邮电大学, 2024.

[980] 杨山山. 降雹声波信号检测及其量级估计方法研究[D]. 南京信息工程大学, 2023.

>本文提出了一种双通道异构**残差收缩网络**（DCI-**DRSN**）能够同时获取两种不同途径得到的特征阈值。

[981] 刘通. 基于迁移学习的试验环境反演分析方法研究[D]. 哈尔滨工程大学, 2023.

>针对以上问题，本文提出了一种基于模型迁移的特征提取方法，其中，迁移模型采用MPECN模型，该模型由多尺度PRelu卷积网络（Multiscale PRelu Convolutional Network，MPCN）和深度高效卷积**残差收缩网络**（Deep Efficient Convolution **Residual Shrinkage Network**，DECRSN）构成。

[982] He J, Xu C, Yin C. et al. Modulation recognition of communication signals based on deep learning. In 2021 IEEE 2nd International Conference on Information Technology, Big Data and Artificial Intelligence (ICIBA) (Vol. 2, pp. 527-531).

>**Deep residual shrinkage network** was used to realize modulation signals feature extraction and classification recognition according to the characteristics of signals to further improve the accuracy of communication signals modulation recognition under low signal-to-noise ratio.

[983] Liu X, Zhang S, Xiao. Two Feature Fusion Network Based on Efficient Deep Residual Shrinkage Spatial-Temporal Graph Convolution for Emotion Recognition from Gaits. In 2022 34th Chinese Control and Decision Conference (CCDC) (pp. 5824-5829).

>Firstly chebyshev polynomial approximation graph convolution is combined with efficient **deep residual shrinkage network** to obtain efficient deep residual shrinkage spatial-temporal graph convolution network to extract deep features.

[984] Li M, Wang M, Chen L, et al. GAN-DRSN based inter-turn short circuit fault diagnosis of PMSM. In 2022 IEEE International Conference on Mechatronics and Automation (ICMA) (pp. 958-963).

>So first the **deep residual shrinkage network** is pre-trained on the big data simulation dataset.

[985] Liu Y, Xu G, Qi L. Research on Power Transformer Health Indicator Based on Improved Convolutional Neural Network. In 2023 6th Asia Conference on Energy and Electrical Engineering (ACEEE) 2023 Jul 21 (pp. 129-133).

>In this regard, we propose a method for constructing a power transformer HI based on ICNN-DRSN (Improved Convolutional Neural Network and **Deep Residual Shrinkage Network**).

[986] Ba Y, Zhang K, Sun W, Chang S. **DRSN** Fan Rolling Bearing Fault Diagnosis Method Based on DWT with Improvement. In 2023 3rd International Conference on New Energy and Power Engineering (ICNEPE) 2023 Nov 24 (pp. 337-340).

>In view of the strong noise environment traditional bearing fault diagnosis method for fault recognition rate low, is put forward based on the discrete wavelet transform (discrete wavelet transform, DWT and the improved **deep residual shrinkage network** (IDRSN) fault diagnosis model.

[987] Deng K, Tao B, Hu J. Unpaired medical image enhancement based on generative adversarial networks. In Fifteenth International Conference on Information Optics and Photonics (CIOP 2024) 2024 Dec 5 (Vol. 13418, pp. 331-339).

>In the generator, we introduce the **residual shrinkage building unit** with the channel-shared thresholds module (DRSN-CS) to suppress artifacts and image noise and extract medical image information through three paths using different convolution kernels.

[988] Wen X, Cao C, Li Y, Sun Y. **DRSN** with Simple Parameter-Free Attention Module for Specific Emitter Identification. In 2022 IEEE International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom) 2022 Dec 9 (pp. 192-200). 

>The advantages of the parameter-free attention module and **deep residual shrinkage network** are integrated by **DRSN**-SimAM. The parameter-free attention module is introduced into the **residual shrinkage building unit** for adaptively learning thresholds, filtering out redundant information irrelevant to the signal fingerprint.

[989] Hui D, Xu H, Ma Z, Sun F, Zhou J, Meng Y. Study on Intelligent Pressure Reducing Valve and Leakage Diagnosis. In 2022 IEEE 6th Information Technology and Mechatronics Engineering Conference (ITOEC) 2022 Mar 4 (Vol. 6, pp. 584-588).

>Meanwhile, pressure sensors are set in front of the valve and behind the valve to collect data by the **deep residual shrinkage network** to train the pressure.

[990] Peng H, Cao C, Sun Y, Li H, Wen X. Blind identification of channel codes under awgn and fading conditions via deep learning. In 2022 International Conference on Networking and Network Applications (NaNA) 2022 Dec 3 (pp. 67-73).

>For solving these difficulties, based on **deep residual shrinkage network** (**DRSN**), this paper proposes a novel recognizer by deep learning technologies to blindly distinguish the type and the parameter of channel codes without any prior knowledge or channel state, furthermore, feature extractions by the neural network from codewords can avoid intricate calculations.

[991] Yuan C, Chen Z, Chen P, Tian R, Xiong D, Guo W. Fine-Grained Gesture Recognition by Using FMCW Millimeter-Wave Radar. In 2023 Cross Strait Radio Science and Wireless Technology Conference (CSRSWTC) 2023 Nov 10 (pp. 1-3). IEEE.

>Particularly, we design an improved **Deep Residual Shrinkage Network** (**DRSN**) with variable channels to recognize features of fine-grained gestures.

[992] Yan L, Zhiming H, Meng G, Qiulin C, Wang W, YuanJia L, Rongfu Z, Zhi W. Typical Fault Simulation and Fault Diagnosis of High Voltage Circuit Breaker. In 2024 IEEE 7th International Electrical and Energy Conference (CIEEC) 2024 May 10 (pp. 2434-2438).

>Utilizing the denoising and feature extraction capabilities of the Channel-Wise **Residual Shrinkage Module** (**DRSN**-CW) with different thresholds in a deep residual neural network, a fault diagnosis model based on deep residual neural networks is proposed.

[993] Zhang C, Li S, Wen J, Fu S. Remaining useful life prediction method based on the improved holt double exponential model. In 2022 5th International Conference on Pattern Recognition and Artificial Intelligence (PRAI) 2022 Aug 19 (pp. 47-52).

>For the problem of low prediction accuracy due to the difficulty in determining the parameters of Holt double exponential model, a remaining useful life (RUL) prediction method based on **deep residual shrinkage network** (**DRSN**) and Holt double exponential model is proposed.

[994] Zeng R, Wang Y. Improved Tracking Algorithm Based on Motion Trend Prediction. In Proceedings of the 2024 9th International Conference on Cyber Security and Information Engineering 2024 Sep 15 (pp. 752-756).

>The algorithm combines a **Deep Residual Shrinkage Network** (**DRSN**) for appearance feature extraction and non-linear motion model prediction.

[995] Ma P, Xue T. Embedding Chinese Face painting into the StyleGAN latent space. In 2021 Ninth International Conference on Advanced Cloud and Big Data (CBD) 2022 Mar 26 (pp. 145-150). 

>We for the first time propose the application of the **deep residual shrinkage networks** to the image generation problem and verify the effectiveness of the proposed method through experiments on various noises.

[996] Ma G, Xu Z, Gao W, Chen J. Few-Shot Bearing Fault Diagnosis in Time-Frequency Maps Using Prototypical Networks. In 2023 IEEE International Conference on Signal Processing, Communications and Computing (ICSPCC) 2023 Nov 14 (pp. 1-6).

>To this end, we propose a novel few-shot fault diagnosis model using the prototypical network based on the **deep residual shrinkage network** (**DRSN**).

[997] Shi B, Zhang Q, Li Y. Synthetic Aperture Radar image target recognition based on hybrid attention mechanism. In Proceedings of the 2021 International Conference on Pattern Recognition and Intelligent Systems 2021 Jul 28 (pp. 37-42).

>The trunk branch composed of the **residual shrinkage network** and the improved channel attention mechanism is responsible for extracting the main characteristics.

[998] Yu L, Tang P, Jiang Z, Zhang X. Denoise Enhanced Neural Network with Efficient Data Generation for Automatic Sleep Stage Classification of Class Imbalance. In 2023 International Joint Conference on Neural Networks (IJCNN) 2023 Jun 18 (pp. 1-8).

>Meanwhile, we design a **Residual Shrinkage** Sequence Network for Sleep Staging (RsSleepNet) as the baseline to compare other resolutions of class imbalance with ours.

[999] Shu T, Zhang F, Sun X. Gaze behavior based depression severity estimation. In 2023 IEEE 4th International Conference on Pattern Recognition and Machine Learning (PRML) 2023 Aug 4 (pp. 313-319).

>We employ a **deep residual shrinkage network** with channel-wise thresholds (**DRSN**-CW) to process the input gaze sequence and estimate the depression severity score.

[1000] Dai H. LinGAN: an Advanced Model for Code Generating based on Linformer. In Journal of Physics: Conference Series 2021 Nov 1 (Vol. 2082, No. 1, p. 012019). 

>We also propose the pre-norm **residual shrinkage unit** to solve the problem of deep degradation of Linformer.

[1001] Li J, Huang Y. Open-Set Recognition of Underwater Acoustic Communication Signals in Impulsive Noise Environment Based on Feature Fusion and Prototype Classification. In 2023 IEEE International Conference on Signal Processing, Communications and Computing (ICSPCC) 2023 Nov 14 (pp. 1-6).

>In this paper, the impulsive noise is suppressed by INP. Then we use the **deep residual shrinkage network** (**DRSN**) and squeeze and excitation (SE) attention unit to extract and fuse the features of time-frequency spectrums and fusion spectrograms.

[1002] Zhang R, Zhao X, Li J, Zhang S, Shang Z. A malicious code family classification method based on self-attention mechanism. In Journal of Physics: Conference Series 2021 Sep 1 (Vol. 2010, No. 1, p. 012066).

>This paper introduces spatial pyramid pooling (SPP) in the **deep residual shrinkage network** to replace the original GAP, so that the network can accept images of different sizes.

[1003] Li S, Wen H, Deng L, et al. Denoising Network of Dynamic Features for Enhanced Malware Classification. In 2023 IEEE International Performance, Computing, and Communications Conference (IPCCC) 2023 Nov 17 (pp. 32-39).

>To achieve noise reduction, four **residual shrinkage blocks** are incorporated into our neural network...

[1004] Zhao Y, Zhou Y. A Data Augmentation Method Based on GAN for Plant Disease Recognition. In International Conference on Computing, Control and Industrial Engineering 2024 Jun 21 (pp. 186-193).

>In this paper, we integrate the **deep residual shrinkage network** (**DSRN**) and multipath methods for improving the generator.

[1005] Yang ZY, Liu J, Han B, Wang ZN, Dong SS, Rao YJ. Ultra-long Large-Capacity FBG Sensing for Long-Haul Powerlines Monitoring. In International Conference on Experimental Vibration Analysis for Civil Engineering Structures 2023 Aug 29 (pp. 682-688).

>Furthermore, with the proposed deep-learning spectrum denoising model based on **Deep Residual Shrinkage Networks**, the mean OSNR at 150 km is enhanced to 7.1 dB.

[1006] Pan Y, Zhou Y, Ji H, Li C. Automatic Modulation Recognition Based on Dual-Channel Fusion Hybrid Neural Network. In 2023 IEEE 16th International Conference on Electronic Measurement & Instruments (ICEMI) 2023 Aug 9 (pp. 201-207).

>The spatial features of the dual-channel data are extracted by the **deep residual shrinkage network** (**DRSN**)...

[1007] Lin X, Zhang L, Wu Z. Intelligent Cyclic Spectrum Features Based Modulation Recognition Design. In 2021 2nd Information Communication Technologies Conference (ICTC) 2021 May 7 (pp. 189-193). IEEE.

>In order to further improve the classification accuracy with lower computational complexity, in this paper, we propose a CS and **deep residual shrinkage network** (**DRSN**) based MR system.

[1008] Liao H, Zhu W, Zhang B, et al. Application of natural gas pipeline leakage detection based on improved DRSN-CW. In 2021 IEEE International Conference on Emergency Science and Information Technology (ICESIT) 2021 Nov 22 (pp. 514-518).

>This paper develops a novel improved model based on **deep residual shrinkage networks** with channel-wise (**DRSN**-CW), to improve the recognition accuracy of natural gas pipeline leakage.

[1009] Yu S, Ding Y, Qian K, Hu B, Li W, Schuller BW. A glance-and-gaze network for respiratory sound classification. In ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) 2022 May 23 (pp. 9007-9011). IEEE.

>To suppress the noises in the spectrogram, we use a **deep residual shrinkage network** to suppress the noises in the spectrogram.

[1010] Zhang S, Zeng Q. Command Words Recognition Algorithm of Shrinking Residual Network based on MFCC and Dual Micro-Array. In 2021 6th International Conference on Intelligent Computing and Signal Processing (ICSP) 2021 Apr 9 (pp. 46-49).

>**Deep residual shrinkage network** with channel-wise thresholds (DRSN-CW) unit is used to calculate the soft threshold respectively for the feature information of each channel

[1011] Xiong R, Huang X, Guo L. Intelligent seismic horizon picking based on Gabor wavelet transform of seismic attribute. In 84th EAGE Annual Conference & Exhibition 2023 Jun 5 (Vol. 2023, No. 1, pp. 1-5).

>Finally, the support vector machine, random forest, extreme gradient boosting models and **deep residual shrinkage network** are used to horizon picking.

[1012] Wang Y, Cheng L, Mao T, Wu M. Rolling Bearing Fault Diagnosis Based on CWT and Two-Stream Convolutional Neural Network. In 2024 5th Information Communication Technologies Conference (ICTC) 2024 May 10 (pp. 1-6).

>The method incorporates **Deep Residual Shrinkage Network** with Different Thresholds Channel by Channel (DRSN-CW), continuous wavelet transform and multi-scale convolutional network into the model...

[1013] Cai Z, Lu L, Cong S. Rolling Bearing Fault Diagnosis Based on Transfer Learning and Dual-Channel CNN and BiGRU. In 2024 International Conference on Advanced Robotics and Mechatronics (ICARM) 2024 Jul 8 (pp. 819-824). 

>To enhance noise immunity and inter-channel feature information, the **Residual Shrinkage Network** module (**DRSN**-CW) is first introduced. 

>Subsequently, the EAM mechanism is integrated into the **residual shrinkage network** module (RSBU-CW) to address the impact of time-domain feature vectors on the threshold τ.

[1014] Ming X, Cheng W, Zhu R, et al. Human Activities Recognition with Amplitude-Phase of Channel State Information using Deep Residual Networks. In 2022 IEEE 17th Conference on Industrial Electronics and Applications (ICIEA) 2022 Dec 16 (pp. 1-6).

>The results show that the accuracy of activity recognition based on the amplitude-phase of channel state information under **deep residual shrinkage network** is 97.2% on average, which is higher than the accuracy of analyzing the amplitude and phase using CNN, the amplitude of CSI using DRSN and the phase of CSI using DRSN.

[1015] Zhu H, Ma Y, Zhang X, Hao C. Adaptive Denoising With Efficient Channel Attention for Automatic Modulation Recognition. In ICC 2024-IEEE International Conference on Communications 2024 Jun 9 (pp. 2113-2118).

>An Efficient **Residual Shrinkage Block** (ERSB) is proposed to improve **Residual Shrinkage Blocks** (RSB) for feature extraction.

[1016] Lin J, Wang C. Image Classification Algorithm Based on Improved Soft Thresholding and Residual Network. InInternational Conference on Artificial Intelligence in China 2023 Jul 22 (pp. 231-239).

>The soft thresholding technique adopted in this paper is derived from the **deep residual shrinkage networks** (**DRSN**).

[1017] Zhang X, Yuan W, Liu C, et al. Deep learning with a self-adaptive threshold for OTFS channel estimation. In 2022 International Symposium on Wireless Communication Systems (ISWCS) 2022 Oct 19 (pp. 1-5).

>In particular, we consider the sparsity of the OTFS channel and propose a **deep residual shrinkage network** (**DRSN**) to implicitly learn the residual noise for recovering the channel information.

[1018] Wang W, Gu J, Zhang S. Dual Contrastive Learning for Unpaired Image Dehazing. In 2023 3rd International Symposium on Artificial Intelligence and Intelligent Manufacturing (AIIM) 2023 Oct 27 (pp. 51-56).

>Our approach improves the Cycle-Consistent Adversarial Networks (Cyclegan) by incorporating an improved **Deep Residual Shrinkage Network** in the generator...

[1019] Jin Z, Cao Y, Liu L, et al. Research on Predicting Container Vessel Handling Time Based on Improved **Deep Residual Shrinkage Net**. In 2024 9th International Symposium on Computer and Information Processing Technology (ISCIPT) 2024 May 24 (pp. 509-514).

[1020] Lv X, Jing Q, Liang C, et al. Quantification of crack in-pipe detection signals in steel pipelines based on differential eddy current detection technique with incremental permeability extraction. In Fourth International Conference on Testing Technology and Automation Engineering (TTAE 2024) 2024 Dec 12 (Vol. 13439, pp. 479-483).

>One method for one-dimensional timedomain signal inspection is the **Deep Residual Shrinkage Net** (**DRSN**), which offers noise immunity and has seen efficient improvements from ...

[1021] Liu G, Jiang Q, Sun Y, et al. A Double-Branch Improved **Residual Shrinkage Network** for Diagnosis of Induction Motor Broken Rotor Bar under Small Samples. IEEE Transactions on Instrumentation and Measurement. 2024 Nov 20.

>Aiming at the problems of limited data collection and the difficulty in estimating the severity of faults, a double-branch improved **residual shrinkage network** (DB-IRSN) for BRBs in IMs was proposed, where both transformed current and vibration signals are utilized.

[1022] Wu X, Peng H, Cui X, Guo T, Ni R, Zhang Y. Multi-Channel vibration signals fusion based on rolling bearings and MRST-Transformer fault diagnosis model. IEEE Sensors Journal. 2024 Apr 10.

>The MRST-Transformer comprises an enhanced **residual shrinkage building unit** with channel-wise (RSBU-CW) and a shallow cross-vision transformer (Cross Vit).

[1023] Zheng Y, Lyu W, Wang C, Guo Q, Zhou D, Xu W. Efficient Conflict-Filtered Network for Defect Detection. IEEE Transactions on Instrumentation and Measurement. 2023 Jul 10.

>Next, we introduce the noise reduction-**residual shrinkage building unit** with channelwise thresholds (NR-RSBU-CW) in the skip connection of the same layer to filter noise and …

[1024] Ji D, Fang W, Zhai C, Cao Z, Ma Y. TTNN: A Physically-Guided Deep Learning Model for Focal Depth and Epicenter Distance Estimation Base on Multistation Waveforms. IEEE Transactions on Geoscience and Remote Sensing. 2024 Sep 2.

>In this study, a physically guided deep learning model, referred to as the travel time neural network (TTNN), is proposed to estimate the focal depth and epicenter distance. TTNN is built upon a CNN, introducing **residual shrinkage modules** (RSMs) that leverage a soft thresholding attention mechanism to extract features more effectively from seismic records with high noise levels.

[1025] Yang M, Cai J, Yang Z, et al. Insect Recognition Method With Strong Anti-Interference Capability for Next-Generation Consumer Imaging Technology. IEEE Transactions on Consumer Electronics. 2024 Jun 17.

>Therefore, this paper proposes a novel multi-source visual data fusion insect recognition algorithm based on a **deep residual shrinkage network**.

[1026] 张火明, 黄敏, 陆萍蓝. 基于改进Resnet-LSTM模型的系泊缆仿真张力预测[J]. 计量学报, 1-8 [2024-12-19].

>本文利用LSTM算法的时序特性结合特征提取网络Resnet搭建改进型**残差收缩网络**(**residual shrinkage network**，Resnet-LSTM) 模型来优化网络同时提高风浪流联合作用下系泊力预测准确率。

[1027] Zhou G, Zhuang Y, Ding X, et al. A Simple Siamese Framework for Vibration Signal Representations. In IEEE International Conference on Image Processing (ICIP) 2022 Oct 16 (pp. 2456-2460).

>To improve the feature learning ability for TD data, a **deep residual shrinkage network** with channel-wise thresholds (**DRSN**-CW) [14] is utilized in this work.

[1028] 周璇, 闫学成. 一种基于一维DRSN的冷水机组故障诊断方法及系统[P]. 广东省: CN202310535170.9, 2023-09-15.

>构建一维**DRSN**故障诊断模型，包括输入层、一维卷积层、**残差收缩单元**、批量标准化层、整流线性函数、全局平均池化层、全连接层与输出层；在**残差收缩单元**中，嵌入注意力机制建立子通道阈值网络获取逐通道阈值...

[1029] 白智全, 马媛媛, 贺邦玮, 等. 一种基于EDRSN的电力通信系统声纹识别方法及系统[P]. 山东省: CN202310628366.2, 2023-08-11.

>声纹识别模型的输入层在获得输入特征后，依次进入声纹识别模型的三个改进**残差收缩块单元**...

[1030] 秦明华, 苗升伍. 一种基于图像识别算法的多机位同步音影录播系统[P]. 江苏省: CN202311008485.4, 2023-10-27.

>所述Google Net V3‑Unet+模型首先将Google Net V3中inception模块和**深度残差收缩模块**的组合模块移植到Unet网络的编码器...

[1031] X. Cui, C. Zhang, J. Li, et al. Channel estimation based on dual frequency domain Transformer in time-frequency doubly-selective fading underwater acoustic channels[J]. Physical Communication, 2024.

>Additionally, a high-frequency feature extraction (HFE) module based on **deep residual shrinkage** is implemented to mitigate the impact of noise and ICI on channel estimation.

[1032] 华锋. 模糊视觉环境下的密集水下目标检测算法研究[D]. 南昌航空大学, 2023.

>首先，在主干分支中，本章采用了**收缩残差块**来加强特征。相较于传统的残差块，**收缩残差块**具有更强的降噪能力，可以有效地减少噪声对特征提取的干扰。

[1033] 刘惠, 钟鹏程, 刘振宇, 等. 基于传感数据混合噪声抑制的装备零件故障诊断方法、装置及设备[P]. 浙江省: CN202411280901.0, 2024-12-17.

>可选地，所述深度学习模型为带有选择性核卷积模块与全局参数化ReLU的**深度残差收缩网络**。

[1034] Gong B, Zhang X, Chen X. Research on the Health Status Recognition Method of High Speed Train Bearings Based on **Deep Residual Shrinkage** Attention Block Network Model. In 2024 9th International Conference on Intelligent Computing and Signal Processing (ICSP) 2024 Apr 19 (pp. 977-982).

>This model fully utilizes the soft thresholding ability of **residual shrinkage networks** to suppress noise and the filtering ability of spatial channel attention to key feature information...

[1035] Yu S, Wei Y. Multi-focus image fusion method based on **deep residual shrinkage network**. In2024 7th International Conference on Computer Information Science and Application Technology (CISAT) 2024 Jul 12 (pp. 392-395).

[1036] Wang R, Fang Y, Qiang Y, et al. A Novel Method of Myocardial Infarction Diagnosis Based on **Residual Shrinkage Network**. In 2024 43rd Chinese Control Conference (CCC) 2024 Jul 28 (pp. 8864-8869).

[1037] Jiang W, Wu J, Zhu H, et al. Multi-Model Fusion Health Assessment for MultiState Industrial Robot via Fuzzy **Deep Residual Shrinkage Network** and Versatile Cluster. IEEE Transactions on Fuzzy Systems. 2024 Jun 7.

[1038] Huang S, Guo L, Fu X, et al. Open-Set Specific Emitter Identification Leveraging Enhanced Metric Denoising Auto-Encoders. IEEE Internet of Things Journal. 2024 May 22.

>This advanced framework incorporates a **deep residual shrinkage network**, significantly augmenting the denoising autoencoder’s capability, thereby bolstering its resilience against noisy environments.

[1039] Fan F, Zhang M, Yu D, et al. Lightweight Context Awareness and Feature Enhancement for Anchor-Free Remote Sensing Target Detection. IEEE Sensors Journal. 2024 Feb 12.

>Second, we proposed that ELAN-RSN uses an optimized **residual shrinkage network** (**RSN**) to eliminate background noise and conflicting information in the multiscale feature fusion.

[1040] Wang K, Gou Y, Chen Z, et al. Complex Fault Diagnosis of Rolling Bearings Based on Improved **Residual Shrinkage Networks**. In 2023 3rd International Conference on Robotics, Automation and Intelligent Control (ICRAIC) 2023 Nov 24 (pp. 344-349).

[1041] Wang Y, Cao C, Li Y, et al. Radiofrequency fingerprint feature extraction and recognition using a coordinate attention-guided **deep residual shrinkage network**. In 2023 International Conference on Networking and Network Applications (NaNA) 2023 Aug 18 (pp. 551-557).

[1042] Li J, Tan L, Zhou Y, et al. Voice-Face Cross-Modal Association Learning Based on **Deep Residual Shrinkage Network**. In 2023 IEEE International Conference on Image Processing and Computer Applications (ICIPCA) 2023 Aug 11 (pp. 140-145).

[1043] Luo M, Yang L, Sun Z, Yin M, Ma Y, Wu X, Cao W. Gait recognition based on sEMG and **Deep Residual Shrinkage Network**. In2023 IEEE International Conference on Real-time Computing and Robotics (RCAR) 2023 Jul 17 (pp. 122-127).

[1044] Feng Q, Han L, Zhao B, et al. Microseismic events recognition via joint deep clustering with **residual shrinkage** dense network. IEEE Transactions on Geoscience and Remote Sensing. 2023 Sep 11.

>To better suppress the noise in microseismic data, RSDB adds a densely connected hybrid dilated convolution and an improved threshold module to the **deep residual shrinkage network**.

[1045] 孟晶晶, 徐雅斌. 基于集成学习的乐声分离方法[J]. 北京信息科技大学学报(自然科学版), 2023, 38(03): 27-34.

>本文基于集成学习的方法，提出一种将卷积神经网络、注意力机制和**深度残差收缩网络**相结合的深度学习模型，能有效提升分离质量。

[1046] Zhu L, Sun Y, Zhang S. Multi-angle recognition of vehicles based on carrier-free UWB sensor and **deep residual shrinkage** learning. IEEE Microwave and Wireless Components Letters. 2022 Mar 11;32(7):927-30.

>This letter designs a **deep residual shrinkage network** to achieve the multiangle intelligent vehicle recognition.

[1047] Shen Q, Yang X, Zou L, et al. Multitask **residual shrinkage** convolutional neural network for sleep apnea detection based on wearable bracelet photoplethysmography. IEEE Internet of Things Journal. 2022 Aug 2;9(24):25207-22.

[1048] Roy A, Satija U. RS-2-BP: A Unified Deep Learning Framework for Deriving EIT-Based Breathing Patterns From Respiratory Sounds. IEEE Signal Processing Letters. 2024 Oct 8.

>The major contributions of the proposed framework are following: (a) investigation of mel spectrograms of RSs for predicting BPs, (b) proposed a novel light- hybrid-DL architecture for deriving BPs that utilizes cascaded standard convolution and **residual shrinkage blocks** followed by feature-refined transformer encoder, and LSTM module.

[1049] Zhang L, Yang X, Liu H, et al. Efficient **residual shrinkage** CNN denoiser design for intelligent signal processing: Modulation recognition, detection, and decoding. IEEE Journal on Selected Areas in Communications. 2021 Nov 8;40(1):97-111.

[1050] Xie W, Xiao J, Zhu P, Yu C. Multi-task learning-based channel estimation for RIS assisted multi-user communication systems. IEEE Communications Letters. 2021 Dec 23;26(3):577-81.

>Meanwhile, the **residual shrinkage blocks** are introduced into the multi-task network architecture to release the noise effect.

[1051] Qian Y, Yang X, Tang SK. Dual-space aggregation learning and random erasure for visible infrared person re-identification. IEEE Access. 2023 Jul 21.

>To address these issues, we explore a dual-space aggregation learning (DSAL) method that combines instance-batch normalization (IBN) and **residual shrinkage** (**RS**) into a baseline model for feature learning and compression at the channel-level.

[1052] 刘硕佳. 《第4章 基于**深度残差收缩网络**的低信噪比信号识别技术》基于深度学习的非授权频段无线信号识别[D]. 华侨大学, 2023.

>提出了一种基于**深度残差收缩网络**(**DRSN**)的低信噪比信号识别方法。

[1053] 曹雯琪. 基于二维卷积神经网络的轴承故障诊断方法研究[D]. 华侨大学, 2023.

>针对复杂工况下多源数据冗余与特征难以充分提取的问题，提出基于**深度残差收缩模块**的多传感器数据故障诊断方法，该方法具有一定的抗噪能力，可以实现在不同工况下的故障诊断。

[1054] 张稣艾. 《4.2.3  **残差收缩网络**》基于对抗训练的软测量关键技术研究[D]. 西北师范大学, 2024.

>在改进软测量建模预测能力方面，利用遮蔽卷积自注意力模块（MCT）对不同位置的特征进行提取，重构**残差收缩网络模块**获得RSN模块...

[1055] 吴清涛, 傅晓杰, 张晨, 等. 基于音频去干扰自学习神经网络的地下线缆定位系统研究[J]. 电气时代, 2024, (09): 93-98.

>**深度残差收缩网络**是一种面向振动信号的卷积神经网络，可以适用于数据含噪情况，其基本结构由输入层、卷积层、残差模块、注意力模块、全连接层和输出层组成。

[1056] 程帅洋. 基于视听觉多模态学习的视觉显著性分析[D]. 厦门大学, 2022.

>本文提出的声音注意力模块将**深度残差收缩网络**与注意力机制结合起来，用于声音信号的特征增强和噪声抑制...

[1057] 张旗. 噪声环境下基于深度学习的滚动轴承剩余寿命预测方法研究[D]. 大连交通大学, 2024.

>MSCNN-DRSNA 模型的核心思想是将Stacking集成学习的思想与**深度残差收缩网络**以及注意力机制结合，以实现对噪声环境下原始振动信号的多尺度建模和有效的信息提取。

[1058] 王安义, 李婼嫚, 李新宇, 等. 基于深度学习的导频设计和信道估计联合优化[J/OL]. 计算机科学, 1-13[2024-12-27].

>然后将优化后的导频位置输入**深度残差收缩网络**（**Deep Residual Shrinkage Network**， **DRSN**）获取更精确的CSI，进一步完成信道的精确估计。

[1059] M. Zhang, S. Huang, S. Chen, T. Ma. Research on ECG signal processing under complex noise based on machine learning algorithm[J]. IEEE 10th World Forum on Internet of Things (WF-IoT), 2024.

>and proposes a framework for ECG signal processing based on the **Deep Residual Shrinkage Network** combined with the Fully Convolutional Self-Coder and Decoder for ECG signals in a complex noise environment.

[1060] 邹腾枭. 基于CEEMD和自适应特征融合的滚动轴承故障诊断方法研究[D]. 三峡大学, 2024.
>该方法首先以CEEMD分解的有效IMF分量作为输入，在**深度残差收缩网络**的基础上，设计子域网络计算改进软阈值函数中的斜率因子和阈值参数...

[1061] 李明. 基于**深度残差收缩网络**的滚动轴承故障诊断方法研究[D]. 河北科技大学, 2024.

[1062] 王小敏, 熊旭洲, 杨勇, 等. 基于轨出电压暂态特征的轨道电路分路不良识别[J/OL]. 西南交通大学学报, 1-9[2025-01-05].
>最后，提出基于高效通道注意力机制的改进**深度残差收缩网络**，采集不同分路电阻对应的轨出暂态特征进行网络训练和分路电阻识别...

[1063] 郭素峡, 周建平, 刘华珠, 等. 基于**深度残差收缩网络**以及LSTM的ECG分类系统[P]. 广东省: CN202411113128.9, 2024-12-27.

[1064] 欧智坚, 肖吉, 孙磊, 等. 一种适用于高噪音环境的会议系统[P]. 江苏省: CN202311774198.4, 2024-12-27.

>将所述语音信号输入具备语音识别功能的**深度残差收缩网络**中，得到纯净语音文本。

[1065] 曹毅, 王彦雯, 曹光扬, 等. 一种基于分频段减小混响的声音事件分类方法[P]. 江苏省: CN202411274992.7, 2024-12-27.

>基于**深度残差收缩网络****DRSN**，构建频域**残差收缩网络**F-**DRSN**；所述频域**残差收缩网络**F-**DRSN**包括：依次连接的一个卷积层、**残差收缩单元**、全局平均池化和全连接层；其中，所述**残差收缩单元**的个数大于1；每个所述**残差收缩单元**中包括频域自校正算法；

[1066] 郭文龙, 罗庆全, 余涛, 等. 一种面向未知混叠场景的两阶段非侵入式负荷检测方法[P]. 广东省: CN202411199440.4, 2024-12-27.

>基于非局部**残差收缩模块**构建轻量化的鲁棒识别模型，用于提取降噪后目标电器波形的关键特征，从而进行鲁棒识别；

[1067] 史丽晨, 史炜椿, 王海涛, 等. 基于**DRSN**-Bi LSTM模型的刀具磨损预测方法研究[J/OL]. 机械工程学报, 2024, (24): 66-74[2025-01-07].

>针对以上问题，研究了一种基于深度学习的刀具磨损预测方法，将多通道筛选机制应用到预测模型中，提出基于**深度残差收缩**-双向长短期记忆网络模型的刀具磨损预测方法。

[1068] 刘小峰, 徐全桂, 金燕, 等. 噪声干扰环境下的深度强化学习故障诊断方法[J/OL]. 电子测量与仪器学报, 1-10[2025-01-09].

>该方法以高效通道注意力机制-**深度残差收缩网络**为Q网络基本模型，避免Q网络结构复杂导致的梯度消失现象。

[1069] 殷浩. 基于**深度残差收缩网络**的液压滑阀卡滞状态识别研究[D]. 哈尔滨工程大学, 2024.

[1070] 张宇, 李清波, 解晶莹, 等. 一种基于实际充电数据进行电池SOH估计的方法和系统[P]. 上海市: CN202411418104.4, 2024-12-31.

>构建**深度残差收缩网络**模型，将作为训练样本的所述电池充电数据作为输入，训练所述深度残差收缩网络模型；

[1071] 刘扬, 王悄, 陈俊杰, 等. 基于多模态时空特性的DNS数据泄露检测方法和系统[P]. 安徽省: CN202411501458.5, 2025-01-03.

>设计了基于**深度残差收缩网络**的深度特征提取模块，可以有效整合来自不同模态的补充信息，并利用**深度残差收缩网络**对噪声的鲁棒性，可以自动提取深度DNS数据泄密特征，提高实际检测中的鲁棒性。

[1072] 李鸿岐, 朱勇, 王怿, 等. 基于**DRSN**-LSTM的运动想象脑电信号分类方法[P]. 广东省: CN202410789953.4, 2024-09-10.

>将**深度残差收缩网络**和长短期记忆网络串行连接构成**DRSN**-LSTM特征融合网络，并进行训练；

[1073] 殷增斌, 陈邵阳, 袁军堂. 一种基于MDRSNet的切削刀具磨损预测方法[P]. 江苏省: CN202410271119.6, 2024-05-28.

>所述MDRSNet刀具磨损预测模型通过在**深度残差收缩网络****DRSN**中引入多分支结构构建，其中，所述**深度残差收缩网络****DRSN**包括若干层，不同层包含不同的**残差收缩单元**RSBU，所述**残差收缩单元**RSBU用于提取每层的信号特征...

[1074] 王少娜, 李响, 石嘉, 等. 基于显著融合差异图和深度学习的SAR图像变化检测方法[P]. 天津市:CN202311417809.X, 2024-01-26.

>最后，用训练样本训练**残差收缩**胶囊网络，并使用训练好的网络对测试样本进行分类，生成最终的变化结果图像。

[1075] 初宁, 李晓明, 嘉法理, 等. 基于半监督学习和残差神经网络的射流风机故障分类方法[P]. 浙江省:CN202211586747.0, 2023-12-29.

>本发明公开了一种半监督学习和**深度残差收缩网络**的地铁射流风机故障分类方法

[1076] 商少茹. 基于Wi-Fi信道状态信息的被动式室内人员态势感知技术研究[D]. 河南科技学院, 2024.

>该方法利用设备自动采集的CSI数据，将计算预处理后的数据滑动方差作为输入特征，对改进的**深度残差收缩网络**(**Deep Residual Shrinkage Network**，**DRSN**)进行训练，从而实现CSI数据到对应步态的映射。

[1077] 陈昊杰, 陈永毅, 倪洪杰, 等. 基于双维度注意力**残差收缩网络**的滚动轴承故障诊断[J]. 高技术通讯, 2024, 34(12): 1330-1340.

[1078] 李鑫. 基于地基云图的超短期光伏功率预测研究[D]. 天津大学, 2023.

>本文提出了基于一维**深度残差收缩网络**(One-Dimensional **Deep Residual Shrinkage Network**,1D-**DRSN**)的光伏功率预测方法。

[1079] Z. Jiang, J. Wu, H. Yu, et al. End-to-End Methane Concentration Measurement Model with **Deep Residual Shrinkage Network** for Direct Absorption Spectroscopy. IEEE Transactions on Instrumentation and Measurement, 2025.

[1080] Zhuang Q, Zhang J, Lin J, Liu W. A fault diagnosis method for partial discharge in distribution switchgear based on global Feature-enhanced **residual shrinkage network**. In Journal of Physics: Conference Series (Vol. 2935, No. 1, p. 012032), 2025. IOP Publishing.

[1081] Feng X, Guo Z, Kwong S.ID3RSNet: cross-subject driver drowsiness detection from raw single-channel EEG with an interpretable **residual shrinkage network**. Frontiers in Neuroscience, 2025, 18, 1508747.

[1082] C. Ma, S. Nan, Z. Kun, et al. A novel cross domain diagnosis method based on physical feature weighting and **deep residual shrinkage network**. Measurement Science and Technology 36, no. 1 (2024): 0161b6.

[1083] 赵建. 基于集成学习与**残差收缩网络**的IoT入侵检测方法[D]. 哈尔滨师范大学, 2024.

[1084] Cao H, Xu B, Wang C, et al. Automatic Seismic Event Detection in Low Signal-to-noise Ratio Seismic Signal Based on a **Deep Residual Shrinkage Network**. Computers & Geosciences, 2025, 105868.

[1085] 祝国铸, 叶瑞禄, 赵杏杏, 等. 基于组合模型的感潮河段潮位预报方法及系统[P]. 江苏省: CN202411517100.1, 2025-01-14.

>结合**深度残差收缩网络**、双向长短时记忆网络和注意力机制构建组合模型，挖掘时空特征。

[1086] 徐彬, 曹欢, 王琮煜, 等. 一种基于**深度残差收缩网络**的低信噪比地震检测模型[P]. 四川省: CN202411525410.8, 2025-01-21.

[1087] 罗静, 马黎文, 胡海军, 等. 一种铁路机房设备健康度预测模型的训练方法、装置、设备及介质[P]. 北京市: CN202411590479.9, 2025-01-21.

>将所述归一化后参数值时序数据输入至训练好的**深度残差收缩网络****DRSN**中进行注意力机制筛选，得到筛选后参数值时序数据并作为设备健康指标；

[1088] 郭海科, 赵小强, 梁浩鹏, 等. 一种小样本下基于MSDFM-ASTRSB的滚动轴承故障诊断方法[P]. 甘肃省: CN202411393951.X, 2025-01-21.

>基于非对称软阈值**残差收缩块**和位置交互自注意力机制，构建MSDFM-ASTRSB滚动轴承故障诊断模型

[1089] 王俊波, 周亚鹏, 高长江, 等. 一种改进CTC的摩斯信号快速译码方法[P]. 江苏省: CN202411205315.X, 2025-01-24.

>构建深度学习框架，包括**深度残差收缩模块**、全连接层和softmax结构；对**深度残差收缩模块**中间层经过全连接层和softmax结构输出...

[1090] 卢润坤, 吕戌杪, 陈金忠, 等. 一种端到端钢质油气管道裂纹的多通道检测方法[P]. 北京市: CN202411933639.5, 2025-01-28.

>将裂纹缺陷信号集输入**DRSN**2d模型训练，配合超参数，得到最佳优化模型。

[1091] 曾庆福, 陈志艺, 郑明艺, 等. 基于数字孪生的能耗预测及异常检测方法以及系统[P]. 福建省: CN202411832030.9, 2025-01-14.

>将物理参数和预测能耗进行融合，利用**深度残差收缩网络**进行回归训练，获得实时能耗、平均能耗、不同运行工况下的能耗，以评估整车能耗。

[1092] 谭超, 何长江, 谭文瑞, 等. 基于EEMD分解和NRBO优化的光伏户变关系预测方法[P]. 湖北省: CN202411256874.3, 2025-01-24.

>DRSN‑BIGRU‑ATTENTION网络模型包括：**深度残差收缩网络****DRSN**、双向门控循环单元BIGRU、注意力机制ATTENTION；

[1093] 罗嘉鹏, 陈晓兵, 陈尚, 等 . 一种基于物理信息约束的VMD-PIML轴承故障预测方法[P]. 江苏省: CN202411379809.X, 2025-01-21.

>对模型进行初始化权重，使用**深度残差收缩网络**构建PIML模型，使用改进的北方苍鹰算法FNGO对使用**残差收缩网络**构建PIML模型中超参数进行迭代寻优

[1094] 石争浩, 叶露露, 冯亚宁, 等. 基于自适应双向选择状态空间的生理信号片段分析方法[P]. 陕西省: CN202411422101.8, 2025-01-14.

>通过**深度残差收缩网络**进行自适应降噪；再通过多尺度高效聚合块来完成轻量级的多尺度语义信息建模；

[1095] 谷志茹, 毛麒云, 胡久松, 等. 基于注意力残差网络的毫米波信道估计算法[J/OL].无线电通信技术,1-9 [2025-03-11].

>该算法通过构建注意力引导模块和**残差收缩模块**，学习OFDM解调和传统信道估计方法的联合近似，从而在大规模MIMO-OFDM系统中有效提升信道估计的精度和鲁棒性。

[1096] 孙浩.基于数字孪生的加工平台轴承故障诊断系统研究[D].青岛理工大学,2024.

>使用**深度残差收缩网络**(**DRSN**)对图像融合方法进行验证，确定了两种图像的最佳融合比例。

[1097] 朱建国,申伟,邓朝恒,等.夹层金板纯度脉冲涡流检测系统的研制与应用[J].分析测试技术与仪器,2025,31(01):1-7.

>...包含线性电源和开关电源的混合供电模块研制，基于C++、Qt和Python的控制与数据分析软件开发，基于**残差收缩网络**的深度学习模型训练与验证等。

[1098] 冯郑雨.基于深度学习的滚动轴承复合故障智能诊断方法研究[D].成都理工大学,2023.

>提出了一种基于**深度残差收缩神经网络**和空洞卷积的复合故障特征提取方法。

[1099] 曹同洲.基于CNN及多注意力的跨站脚本检测研究[D].沈阳化工大学,2023.

>本章使用**残差收缩模块**提升模型对边缘信息的处理能力，该模块的结构示意图如图...

[1100] 雷宇.基于深度学习的便携式心电诊断系统研究[D].南京师范大学,2022.

>综上所述，特征提取部分采用**深度残差收缩网络**(**DRSN**)，激活函数采用Mish函数后，模型既强化了特征提取能力又具备了自动抗噪的功能。

[1101] 崔春霞.融入注意力机制的深度哈希图像检索方法研究[D].华中师范大学,2024.

>提出了基于**深度残差收缩**注意力网络和哈希中心的图像检索方法...

[1102] 武强,张帅,杜沅泽,赵颖旺,徐华.矿井突水识别方法、装置、电子设备及存储介质:202411403875.6[P].2025-03-04.

>并且该初始模型包括**残差收缩层**和卷积块注意力层,增强了对水流特征的关注和背景干扰的抑制,显著提升了在水流边缘检测和复杂背景分割中的性能。

[1103] 浙江大学.基于多源异构数据融合的谐波减速器故障诊断方法:202411640755.8[P].2025-03-04.

>三种信号的二维时频域特征图先分别通过**深度残差收缩网络**进行噪声抑制以及特征选择...

[1104] 扬州大学.一种带缝拱坝位移预测及其不确定性量化方法及系统:202411366416.5[P].2025-02-28.

>探究左**残差收缩**块组、右**残差收缩**块组以及收缩单元对DSRSN的带缝拱坝位移预测模型性能的影响；

[1105] 哈尔滨理工大学.基于数字孪生的不同工况下工业机器人谐波减速器故障诊断方法及系统:202411542983.1[P].2025-02-25.

>无监督域适应网络模型构建引入改进的半软阈值函数构建**深度残差收缩网络**，提取某工况已知标签源域和其他工况未知标签目标域数据特征，同时抑制噪声干扰；

[1106] 史灿.基于人工智能的美甲笔直流无刷驱动器运行速度调控方法:202411537102.7[P].2025-02-18.

>利用**深度残差收缩网络**中的**残差收缩单元**，通过软阈值函数自动筛选与优化特征数据；

[1107] 洛阳理工学院.基于**残差收缩**卷积和注意力机制的旋转机械故障诊断方法:202510027908.X[P].2025-02-18.

[1108] 华中师范大学.一种轮廓与纹理特征协同驱动的耕地地块遥感提取方法:202510061605.X[P].2025-02-18.

>首先在编码器中引入**深度残差收缩网络**模块对妨碍农田体块提取任务的冗余信息进行消除...

[1109] 梁立振,杨胜.一种基于数字孪生的VR故障诊断系统及方法:202411768606.X[P].2025-02-28.

>...数据故障诊断预测采用**深度残差收缩网络**处理三维时域信号...

[1110] 王玉芳,孙一鸣,翟刚毅,等.一种基于神经网络滤波的储层固有频率井下原位测量方法:202411631600.8[P].2025-02-28.

>基于**深度残差收缩神经网络**对自振振动噪声信号数据、背景噪声信号及脉冲放电时的反馈振动信号数据进行滤波降噪；

[1111] 何密,曹濒月,赵美云,等.一种基于毫米波雷达的非接触式心电特征点检测方法及系统:202411723548.9[P].2025-02-28.

>通过四组重复的**深度残差收缩网络**提取每一层特征数据中的感兴趣区域特征；

[1112] 孙鹏, 谢芮.权限滥用的检测方法、装置、电子设备及可读存储介质:202411591924.3[P].2025-02-18.

>该权限滥用模型中可以是包括卷积神经网络、深度残差网络、**深度残差收缩网络**、前向反馈网络、霍普菲尔网络、AlexNet网络、vgg网络、googlenet网络、resnet网络等用于对应用程序的权限滥用进行检测的一种或多种网络。

[1113] 王传娜,魏青,王振奎.标记定位方法和装置:202311075460.6[P].2025-02-25.

>通过在深度优先算法、广度优先算法、**残差收缩网络**、方向性FAST特征点检测和旋转BRIEF描述算法(ORB算法)等中选取与各个椎体相匹配的识别方法，从各个椎体中识别出目标对象的颈部位置的第一椎体以及第二椎体。

[1114] 李振国,苏春娜,张亮,等.一种基于大数据的微电网负荷预测方法及系统:202510059165.4[P].2025-02-18.

>利用**深度残差收缩网络**算法改进时间卷积网络的残差模块以增强模型的鲁棒性和泛化能力。**深度残差收缩网络**算法通过引入软阈值化和注意力机制来减少噪声干扰并突出重要特征。

[1115] 梁惠康.基于DRSN的分布式光纤传感周界安防系统信号识别研究[D].暨南大学,2023.

>本文的创新之处在于提出使用**深度残差收缩网络**（**DRSN**）开展分布式光纤传感信号识别研究，并提出改进的思路。

[1116] 李德望,周瑶.基于改进**DRSN**-CW的气体泄漏检测技术[J].中国高新科技,2024,(22):140-142.

>**深度残差收缩网络**是深度残差网络的改进版本，是深度残差网络、注意机制和软阈值函数的集成。

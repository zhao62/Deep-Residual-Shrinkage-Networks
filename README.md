# Deep-Residual-Shrinkage-Networks

The deep residual shrinkage network is a variant of deep residual networks (ResNets), and aims to improve the feature learning ability from highly noise signals or complex backgrounds. Although the method is originally developed for vibration-based fault diagnosis, it can be applied to image recognition and speech recognition as well. The major innovation is the integration of soft thresholding as nonlinear transformation layers into ResNets. Moreover, the thresholds are automatically determined by a specially designed sub-network, so that no professional expertise on threshold determination is required.

![The basic idea of deep residual shrinkage networks](https://github.com/zhao62/Deep-Residual-Shrinkage-Networks/blob/master/Basic-idea-of-DRSN.png)

The method is implemented using TensorFlow 1.0.1, TFLearn 0.3.2, and Keras 2.2.1, and applied for image classification. A small network with 3 residual shrinkage blocks is constructed in the code. More blocks and more training iterations can be used for a higher performance.

## Abstract:
This paper develops new deep learning methods, namely, deep residual shrinkage networks, to improve the feature learning ability from highly noised vibration signals and achieve a high fault diagnosing accuracy. Soft thresholding is inserted as nonlinear transformation layers into the deep architectures to eliminate unimportant features. Moreover, considering that it is generally challenging to set proper values for the thresholds, the developed deep residual shrinkage networks integrate a few specialized neural networks as trainable modules to automatically determine the thresholds, so that professional expertise on signal processing is not required. The efficacy of the developed methods is validated through experiments with various types of noise.

## Reference:

Minghang Zhao, Shisheng Zhong, Xuyun Fu, Baoping Tang, Michael Pecht, Deep residual shrinkage networks for fault diagnosis, 
IEEE Transactions on Industrial Informatics, 2020, 16(7): 4681-4690.

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

[1] 刘徐洲, 李孝忠. 基于**深度残差收缩网络**和迁移学习的变工况轴承故障诊断[J]. 天津科技大学学报, 2023, 38(04): 76-80.

[2] 龚玉晓, 高淑萍. 基于改进**深度残差收缩网络**的心电信号分类算法[J]. 应用数学和力学, 2023, 44(08): 977-988.

[3] 卞文彬, 邓艾东, 刘东川, 赵敏, 刘洋, 李晶. 基于改进**深度残差收缩网络**的风电机组滚动轴承故障诊断方法[J]. 机械工程学报, 2023, 59(12): 202-214.

[4] 李颖, 黄超, 孙成栋, 徐勇. 真实复杂场景下基于**残差收缩网络**的单幅图像超分辨率方法[J]. 计算机应用: 1-10.

[5] 麻建新, 袁春华, 李翔宇. 针对油井长时程基于**深度残差收缩网络**的模型故障诊断[J]. 科技资讯, 2023, 21(14): 116-119.

[6] 梁惠康, 谢浩燊, 黄红斌, 刘伟平. 基于改进**深度残差收缩网络**的DAS信号识别[J]. 激光与光电子学进展: 1-13.

[7] 林立媛. 基于**深度残差收缩网络**的水稻病害识别方法研究[D]. 黑龙江八一农垦大学, 2023.

[8] 高学金, 李虎, 韩华云, 齐咏生. 基于域自适应**残差收缩网络**的滚动轴承故障诊断[J]. 组合机床与自动化加工技术, 2023,(05): 164-168+173.

[9] 杨正理, 吴馥云, 陈海霞. **深度残差收缩网络**的多特征锅炉炉管声波信号故障识别[J]. 智能系统学报: 1-10.

[10] 刘汉举. 一种基于机器视觉和**深度残差收缩网络**的智能制造缺陷检测方法[J]. 中国科技论文, 2023, 18(04): 462-468.

[11] 陈姮, 陈志翔, 申高宁, 王舒琪. 基于**深度残差收缩网络**的恶意代码分类[J]. 闽南师范大学学报(自然科学版), 2023, 36(01): 50-58.

[12] 曹珂璐. 基于**深度残差收缩网络**的风力发电机齿轮箱故障诊断方法研究[D]. 陕西科技大学, 2023.

[13] 庄全胜. 基于**深度残差收缩网络**的自然情境下的多模态情感识别研究[D]. 哈尔滨理工大学, 2023.

[14] 高云鹏, 孟雪晴, 张其旺, 王庆凯, 杨佳伟, 董一隆. 基于深度宽卷积**残差收缩网络**的球磨机负荷状态诊断[J]. 湖南大学学报(自然科学版), 2023, 50(02): 102-111.

[15] 曹珂璐, 任工昌, 桓源, 张路平. 基于**深度残差收缩网络**的风力发电机齿轮箱故障诊断[J]. 机械与电子, 2023, 41(02): 66-70+75.

[16] 魏煦航, 曹少中, 杨彦红, 项璇. 基于**深度残差收缩网络**的滚动轴承健康因子构建方法[J]. 印刷与数字媒体技术研究, 2023,(01): 71-79.

[17] 王玉, 张燕红, 周昱洲, 林鸿斌. 基于**深度残差收缩网络**的校园垃圾图像分类[J]. 吉林大学学报(信息科学版), 2023, 41(01): 186-192.

[18] 翁敏超, 王海瑞, 朱贵富. 小波变换和**深度残差收缩网络**在齿轮箱故障诊断中的应用[J]. 机械科学与技术: 1-7.

[19] 吴萌, 高怡宁, 王佳. 结合特征聚类和**深度残差收缩网络**的壁画风格迁移[J]. 激光与光电子学进展: 1-17.

[20] 樊庆玲, 杨宏波, 郭涛, 张伟, 王威廉. FrFT-Bark域特征提取与CNN**残差收缩网络**心音分类算法[J]. 云南大学学报(自然科学版), 2023, 45(03): 564-574.

[21] 杨正理, 吴馥云, 陈海霞. 基于改进**深度残差收缩网络**的旋转机械故障诊断[J]. 机电工程, 2023, 40(03): 344-352.

[22] 戴江涛, 申静. 基于双流**残差收缩网络**的人体动作识别方法[J]. 信息技术与信息化, 2022, (10): 106-110.

[23] 田钦文, 冯辅周, 李鸣, 陈晓明, 朱俊臻, 胡浩, 宋超. 基于一维**深度残差收缩网络**的汇流行星排齿轮裂纹故障诊断[J]. 振动与冲击, 2022, 41(19): 198-206.

[24] 彭涛, 伦功仁, 赵峰. 基于**深度残差收缩网络**的船用补水泵滚动轴承故障诊断[J]. 风机技术, 2022, 64(S1): 37-42.

[25] 胡从强, 曲娜, 张帅, 冮震. 连续小波变换和具有注意力机制的**深度残差收缩网络**在低压串联电弧故障检测中的应用[J]. 电网技术, 2023, 47(05): 1897-1905.

[26] 赵莹莹, 何怡刚, 邢致恺, 杜博伦. 基于信息融合与**深度残差收缩网络**的DAB变换器开路故障诊断方法[J]. 电力自动化设备, 2023, 43(02): 112-118.

[27] 王彦博, 吴俊勇, 季佳伸, 李栌苏, 李宝琴. 基于**深度残差收缩网络**的电力系统暂态频率安全集成评估[J]. 电网技术, 2023, 47(02): 482-494.

[28] 吴爱华, 彭金喜. 基于**深度残差收缩网络**的信号调制类型识别[J]. 电子信息对抗技术, 2022, 37(04): 24-30.

[29] 梁日强, 胡燕林, 蒋占四. 基于改进的**残差收缩网络**的带钢表面缺陷识别[J]. 组合机床与自动化加工技术, 2022, (06): 82-85.

[30] 殷磊. 基于**残差收缩网络**的旋转机械故障诊断方法研究[D]. 哈尔滨工业大学, 2022.

[31] 黄莹. 基于**深度残差收缩网络**的心律失常分类算法研究[D]. 广西大学, 2022.

[32] 张晓东. 基于**深度残差收缩网络**滚动轴承故障识别研究[D]. 沈阳工业大学, 2022.

[33] 张晓锋. 基于多尺度特征融合与**残差收缩网络**的齿轮箱故障诊断研究[D]. 石家庄铁道大学, 2022.

[34] 梁日强. 基于**残差收缩网络**的带钢表面缺陷识别方法研究[D]. 桂林电子科技大学, 2022.

[35] 谈诚, 卢德龙, 张丹青. 基于双层**深度残差收缩网络**的台区窃电用户识别方法[J]. 电力大数据, 2022, 25(05): 1-9.

[36] 李雪松, 李劲华, 吕智涵. 基于改进**深度残差收缩网络**的轴承故障诊断[J]. 青岛大学学报(自然科学版), 2022, 35(02): 38-43+50.

[37] 李瑞航, 吴红兰, 孙有朝, 吴华聪. 基于**深度残差收缩网络**多特征融合语音情感识别[J]. 数据采集与处理, 2022, 37(03): 542-554.

[38] 唐震, 乔晓强, 张涛, 苏健, 杨小蒙. 基于**深度残差收缩网络**的辐射源个体识别方法[J]. 电子测量技术, 2022, 45(09): 168-174.

[39] 张翔, 孙宪坤, 胡峻, 尹京苑, 熊玉洁. 结合数据扩增与**残差收缩网络**的地震短临预测[J]. 地震, 2022, 42(02): 74-88.

[40] 李晓峰, 向辉, 杨青桦. 噪声干扰下基于二维特征图和**深度残差收缩网络**的齿轮箱故障诊断[J]. 机床与液压, 2022, 50(07): 187-191.

[41] 刘晓锋, 高丽梅. 基于改进空间**残差收缩网络**模型的农作物病虫害识别[J]. 山东农业大学学报(自然科学版), 2022, 53(02): 259-264.

[42] 袁思邈. 基于宽广**残差收缩网络**的图像分类研究[D]. 山东理工大学, 2022.

[43] 孙丰, 徐贺, 赵宇晗, 张渝东. 数据驱动的基于数学模型插补和改进**深度残差收缩网络**的调节阀状态监控（英文）[J]. Journal of Zhejiang University-Science A(Applied Physics & Engineering), 2022, 23(04): 303-314.

[44] 王之卓, 吕健鸿, 王中鹏. 基于**深度残差收缩网络**的LDPC译码算法[J]. 浙江科技学院学报, 2022, 34(01): 35-41.

[45] 车思韬, 郭荣佐, 李卓阳, 杨军. 注意力机制结合**残差收缩网络**对遥感图像分类[J]. 计算机应用研究, 2022, 39(08): 2532-2537.

[46] 陈玲玲, 毕晓君. 基于**残差收缩网络**的睡眠脑电分期[J]. 仪器仪表学报, 2022, 43(02): 148-155.

[47] 马鑫, 尚毅梓, 胡昊, 徐杨. 基于数据特征增强和**残差收缩网络**的变压器故障识别方法[J]. 电力系统自动化, 2022, 46(03): 175-183.

[48] 孟庆旭, 沈功田, 俞跃, 胡斌, 王宝轩, 李志农. **深度残差收缩网络**的含噪微泄漏超声识别方法[J]. 应用声学, 2022, 41(06): 964-972.

[49] 袁泉, 薛书鑫. 基于**残差收缩网络**的关系抽取算法[J]. 计算机应用, 2022, 42(10): 3040-3045.

[50] 许历隆, 翟江涛, 林鹏, 崔永富. 一种基于改进**深度残差收缩网络**的恶意应用检测方法[J]. 南京信息工程大学学报(自然科学版), 2022, 14(03): 368-378.

[51] 高晔, 郭松宜, 厍向阳. 基于**残差收缩网络**的遥感图像目标检测算法[J]. 计算机工程与应用, 2022, 58(17): 93-100.

[52] 柯翔, 包乾宗, 赵全波. 基于**深度残差收缩网络**的波阻抗反演建模[A]. 中国地球物理学会, 2021: 230-231.

[53] 张力, 常俊, 武浩, 黄彬, 刘欢. **深度残差收缩网络**下的定位与行为联合识别[J]. 计算机工程与应用, 2022, 58(21): 205-212.

[54] 李昊璇, 闫新艳. 基于**深度残差收缩网络**的商品图像识别[J]. 测试技术学报, 2021, 35(04): 294-299+322.

[55] 卢锦玲, 郭鲁豫. 基于改进**深度残差收缩网络**的电力系统暂态稳定评估[J]. 电工技术学报, 2021, 36(11): 2233-2244.

[56] 宋子豪, 程伟, 彭岑昕, 李晓柏. 基于CWD和**残差收缩网络**的调制方式识别方法[J]. 系统工程与电子技术, 2021, 43(11): 3371-3379.

[57] 何涛, 陈剑, 闻英友. 基于**深度残差收缩网络**的HEp-2图像识别[J]. 计算机与现代化, 2021, (01): 38-42.

[58] 杨偲乐. 基于混合域注意力机制的卷积网络和**残差收缩网络**的轴承故障诊断[D]. 北京邮电大学, 2020.

[59] 李天慧, 谢云澄, 车荣花, 梁迪昌, 王健. 基于**DRSN**-BiLSTM的电力信息网络入侵检测模型[J]. 电力信息与通信技术, 2023, 21(09): 30-37.

[60] 刘高辉, 宋博武. **DRSN**与集成融合的OFDM辐射源个体识别方法[J]. 信号处理: 1-14.

[61] 黄湛钧, 董鑫, 卢沐宇, 张瑞涛, 闫钊阳, 张安. 基于**DRSN**与电压幅值分析的航空HVDC系统中逆变器故障诊断[J]. 航空学报: 1-9.

[62] 王小聪, 郝正航, 陈卓. 基于**DRSN**-CW-LSTM网络的锂电池荷电状态预测[J]. 南方电网技术: 1-9.

[63] 赵光宏. 基于Conformer-**DRSN**的新冠肺炎CT图像检测系统的研究与实现[D].辽宁大学, 2023.

[64] 王磊, 孙志成, 王磊, 陈端兵, 蒋家玮. 基于**DRSN**-CW和LSTM的轴承故障诊断[J]. 电子科技大学学报, 2022, 51(06): 921-927.

[65] 文井辉, 伍荣森, 李帅永, 韩明秀. 基于**DRSN**和优化BiLSTM的轴承剩余寿命预测方法[J]. 计算机集成制造系统: 1-18.

[66] 吴卫堃, 宫士营, 郑耀华, 单超, 董传友. 基于**DRSN**的高噪声环境下XLPE电缆故障识别[J]. 电气传动, 2022, 52(16): 75-80.

[67] 毛浩英, 孙有朝, 李龙彪, 晏传奇. 基于改进**DRSN**的航空发动机故障风险预警模型[J]. 航空动力学报: 1-12.

[68] 胡昊, 马鑫, 徐杨, 任玉峰. 基于权重修正和**DRSN**-LSTM模型的向家坝下游水位多时间尺度预测[J]. 水利水电技术(中英文), 2022, 53(07): 46-57.

[69] 赵杰, 陈志刚, 赵志川, 张楠. 基于同步提取变换和**DRSN**的滚动轴承故障诊断研究[J]. 重庆理工大学学报(自然科学), 2021, 35(01): 138-144.

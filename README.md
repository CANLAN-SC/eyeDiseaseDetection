# eyeDiseaseDetection
Eye disease detection

# Dataset
数据集介绍
眼疾识别数据集iChallenge-整理版

眼疾识别数据集iChallenge-整理版，方便开发，重新整理，减少部分图像。
原始数据来源：https://aistudio.baidu.com/aistudio/datasetdetail/23828

眼底视网膜图片，训练和测试数据集各400张。
ichallenge-train-images.zip：包含训练集的图片
ichallenge-test-images.zip：包含测试集的图片
train-images-labels.txt：包含训练集的图片路径和分类标签
test-images-labels.txt：包含测试集的图片路径和分类标签
readme.txt：说明文件

train-images-labels.txt 和 test-images-labels.txt，数据格式：
空格分割，第一段图片路径，第二段分类标签
分类标签：1，病理性近视
分类标签：0，非病理性近视，包含正常眼睛和高度近似

iChallenge-PM中既有病理性近视患者的眼底图片，也有非病理性近视患者的图片，命名规则如下：
病理性近视（PM）：文件名以P开头
非病理性近视（non-PM）：
高度近似（high myopia）：文件名以H开头
正常眼睛（normal）：文件名以N开头

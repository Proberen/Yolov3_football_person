# Yolov3_football_person
## 一个基于Pytorch的Yolov3 足球和人物的目标检测模型（视频、图片）
### 🌲先看效果
### 处理前的视频

### 处理后的视频
### ❓如何使用
#### 1 存放数据集

1. **data/images**目录：存放png/jpg文件

2. **data/xml**目录：存放标签xml文件

#### 2 数据的预处理

1. **data/makeTxt.py**：运行后划分训练集、测试集、验证集（见data/Imagesets目录）

2. **data/voc_label.py**：将xml文件转换为txt文件，运行后生成data/txt目录（注意：修改classes，你需要训练几个类就填写哪几个类）

3. **模型的预处理**：cfg目录下，更改全连接层（**convolutional**）的filters和yolo（**yolo**）层的classes（注意：有四处需要更改，直接搜索即可）
- 公式：filters = （5+classes）*3 
- 举个🌰：需要分两类，那么classes=2，filters=21
4. **更改.data文件和.name文件**：这两个文件的内容大家自行修改，相信都能猜出来是干嘛的

#### 3 训练
那么下面就要开始训练啦！
1. **更改epoch等参数**：见**train.py**的main下的epoch参数，可以自行修改
2. **等待训练结束**
#### 4 测试
经过长时间的训练，大家会获得两个**pt文件**，在**weights目录**下（best.pt、last.pt）
1. 将你想要测试的图片、视频等放入**data/samples**目录下
2.等待训练结束后，结果出现在**output**目录下

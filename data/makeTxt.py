import os
import random
import shutil

if os.path.exists("./ImageSets/"):  # 如果文件存在
    shutil.rmtree("./ImageSets/")
    os.makedirs('./ImageSets/')
else:
    os.makedirs('./ImageSets/')

# 比例
test_percent = 0.1
train_percent = 0.8
val_percent = 0.1

xmlfilepath = './xml'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = list(range(num))

# 获取数量
num_val = int(num * val_percent)
num_test = int(num * test_percent)
num_train = int(num * train_percent)

# 随机采样
train_list = random.sample(list, num_train)
for i in train_list:
    list.remove(i)

test_list = random.sample(list, num_test)
for i in test_list:
    list.remove(i)

val_list = list


ftest = open('./ImageSets/test.txt', 'w')
ftrain = open('./ImageSets/train.txt', 'w')
fval = open('./ImageSets/val.txt', 'w')

for i in range(num):
    name = total_xml[i][:-4] + '\n'
    if i in train_list:
        ftrain.write(name)
    elif i in test_list:
        ftest.write(name)
    else:
        fval.write(name)


ftrain.close()
fval.close()
ftest.close()

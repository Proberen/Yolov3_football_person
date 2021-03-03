import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import shutil

if os.path.exists("./txt/"):  # 如果文件存在
    shutil.rmtree("./txt/")
    os.makedirs('./txt/')
else:
    os.makedirs('./txt/')


sets = ['train', 'test', 'val']

classes = ['football', 'person']


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('./xml/%s.xml' % (image_id))
    out_file = open('./txt/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = 1920
    h = 1080

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        # 类别
        cls = obj.find('name').text
        # 如果类别不在这个类里面或者difficult
        if cls not in classes or int(difficult) == 1:
            continue
        # 获取类别的index
        cls_id = classes.index(cls)
        # 得到xmlbox
        xmlbox = obj.find('bndbox')
        xmin = 0
        xmax = 0
        ymin = 0
        ymax = 0
        if float(xmlbox.find('xmin').text)>float(xmlbox.find('xmax').text):
            xmin = float(xmlbox.find('xmax').text)
            xmax = float(xmlbox.find('xmin').text)
        else:
            xmin = float(xmlbox.find('xmin').text)
            xmax = float(xmlbox.find('xmax').text)

        if float(xmlbox.find('ymin').text)>float(xmlbox.find('ymax').text):
            ymin = float(xmlbox.find('ymax').text)
            ymax = float(xmlbox.find('ymin').text)
        else:
            ymin = float(xmlbox.find('ymin').text)
            ymax = float(xmlbox.find('ymax').text)

        b = (xmin,xmax,ymin,ymax)
        # 归一化
        bb = convert((w, h), b)
        # 写成txt文件
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()
print(wd)
for image_set in sets:
    if not os.path.exists('./txt/'):
        os.makedirs('./txt/')
    image_ids = open('./ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('./%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('./data/images/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()
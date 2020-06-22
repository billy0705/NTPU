import os
import shutil

data_dir = './training'
class_num = 10

ori_data_dir = {}
data_list = {}

for i in range(class_num):
    ori_data_dir[i] = os.path.join(data_dir, str(i))
    data_list[i] = os.listdir(ori_data_dir[i])
    print(len(data_list[i]))

train_class_dir = {}
validation_class_dir = {}
base_dir = './dataset2'
if not os.path.isdir(base_dir):
  os.mkdir(base_dir)
train_dir = os.path.join(base_dir, "train")
if not os.path.isdir(train_dir):
  os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, "validation")
if not os.path.isdir(validation_dir):
  os.mkdir(validation_dir)

for i in range(class_num):
    if i % 2 == 0:
        train_class_dir[i] = os.path.join(train_dir, str(i))
        if not os.path.isdir(train_class_dir[i]):
            os.mkdir(train_class_dir[i])
        validation_class_dir[i] = os.path.join(validation_dir, str(i))
        if not os.path.isdir(validation_class_dir[i]):
            os.mkdir(validation_class_dir[i])
        fnames = data_list[i][:800]
        for fname in fnames:
            src = os.path.join(ori_data_dir[i], fname)
            dst = os.path.join(validation_class_dir[i], fname)
            shutil.copyfile(src, dst)
        fnames = data_list[i][800:]
        for fname in fnames:
            src = os.path.join(ori_data_dir[i], fname)
            dst = os.path.join(train_class_dir[i], fname)
            shutil.copyfile(src, dst)
        print("Finish ", str(i))
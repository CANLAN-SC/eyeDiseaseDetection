import os
import shutil
import random

# 定义源路径和目标路径
source_dir_train = "dataset/ichallenge-train-images"
target_dir_train = "eyeData/train"
target_dir_val = "eyeData/val"
label_file_train = "dataset/train-images-labels.txt"

source_dir_test = "dataset/ichallenge-test-images"
target_dir_test = "eyeData/test"
label_file_test = "dataset/test-images-labels.txt"

# 创建分类子目录
def create_dirs(base_dir):
    os.makedirs(os.path.join(base_dir, "PM"), exist_ok=True)  # 病理性近视 (1)
    os.makedirs(os.path.join(base_dir, "non-PM"), exist_ok=True)  # 非病理性近视 (0)

# 分类函数
def classify_images(label_file, source_dir, target_dir):
    with open(label_file, "r") as file:
        for line in file:
            image_path, label = line.strip().split()
            filename = os.path.basename(image_path)

            # 根据标签选择目标子目录
            if label == "1":
                target_subdir = os.path.join(target_dir, "PM")
            elif label == "0":
                target_subdir = os.path.join(target_dir, "non-PM")
            else:
                continue

            # 复制文件
            shutil.copy(os.path.join(source_dir, filename), target_subdir)

# 划分验证集
def create_val_set(train_dir, val_dir, val_ratio=0.2):
    # 创建验证集子目录
    create_dirs(val_dir)

    for category in ["PM", "non-PM"]:
        train_subdir = os.path.join(train_dir, category)
        val_subdir = os.path.join(val_dir, category)

        # 获取所有文件
        files = os.listdir(train_subdir)
        random.shuffle(files)

        # 抽取验证集比例
        val_count = int(len(files) * val_ratio)
        val_files = files[:val_count]

        # 移动文件到验证集目录
        for file in val_files:
            shutil.move(os.path.join(train_subdir, file), val_subdir)

# 创建训练集、测试集和验证集的目标目录
create_dirs(target_dir_train)
create_dirs(target_dir_test)
create_dirs(target_dir_val)

# 分类训练集
classify_images(label_file_train, source_dir_train, target_dir_train)

# 划分验证集
create_val_set(target_dir_train, target_dir_val)

# 分类测试集
classify_images(label_file_test, source_dir_test, target_dir_test)

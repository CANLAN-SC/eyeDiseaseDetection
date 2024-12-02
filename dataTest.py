from ultralytics import YOLO
import os

# 加载模型路径
model_path = os.path.join("runs", "classify", "train", "weights", "best.pt")
image_paths = [
    os.path.join("eyeData", "test", "non-PM", "V0001.jpg"),
    os.path.join("eyeData", "test", "PM", "V0002.jpg")
]

# 加载模型
model = YOLO(model_path)
results = model(image_paths)

# 结果保存目录
output_dir = "output_results"
os.makedirs(output_dir, exist_ok=True)

# 处理结果列表
for image_path, result in zip(image_paths, results):
    # 从路径中提取类别（PM 或 non-PM）
    category = os.path.basename(os.path.dirname(image_path))
    # 获取输入图片的文件名（不带路径）
    original_filename = os.path.basename(image_path)
    # 移除扩展名
    base_filename = os.path.splitext(original_filename)[0]
    
    # 构造文件名，包含类别标记
    result_filename = f"{category}-{base_filename}-result.jpg"
    # 构造保存路径
    output_file = os.path.join(output_dir, result_filename)
    
    # 显示结果
    result.show()  # 显示结果到屏幕
    # 保存结果到磁盘
    result.save(filename=output_file)
    print(f"结果已保存到 {output_file}")

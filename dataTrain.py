from ultralytics import YOLO

# 载入预训练模型
model = YOLO("yolo11x-cls.yaml")  
model = YOLO("yolo11x-cls.pt")  
model = YOLO("yolo11x-cls.yaml").load("yolo11x-cls.pt")  

# 训练模型
results = model.train(data="eyeData", epochs=100, imgsz=64, save = True, optimizer = 'auto', val = True, plots = True)

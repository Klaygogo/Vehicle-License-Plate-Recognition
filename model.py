#coding:utf-8
from ultralytics import YOLO

# 加载预训练模型
model = YOLO("runs/detect/train21/weights/best.pt")
# Use the model

def train():
    model.train(data='datasets/PlateData/data.yaml', epochs=10, batch=4)

def predict():
    model.predict(source='car2024/car2024', save=True, conf=0.5)


if __name__ == '__main__':
    train()
    predict()

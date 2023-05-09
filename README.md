# Grocery Detection and OCR

By [Abdullah Alshadadi](https://github.com/Srking501)

## Getting Started

```bash
git clone https://github.com/Srking501/grocery-detection-and-ocr --recurse-submodules
pip install -r yolov5/requirements.txt
```

**If you have not added the `--recurse-submodules`:**

```bash
git submodule init
git submodule update
```

## To Train the Model

```bash
python yolov5/train.py --img 640 --epochs 3 --data data/roboflow-grocery-detection-yolov5pytorch/data.yaml --weights models/yolov5s.pt
```

## Run under Camera:

```bash
python yolov5/detect.py --weights yolov5/runs/train/<exp<n>>/weights/best.pt --source 0
```

## 🚧 ATTEMPTING YOLOV5 PyTorch Hub IMPLEMENTATION 🚧

```bash
pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt
```

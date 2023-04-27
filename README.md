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

## To Run the Model

```bash
python yolov5/train.py --img 640 --epochs 3 --data data/roboflow-grocery-detection-yolov5pytorch/data.yaml --weights models/yolov5s.pt
```

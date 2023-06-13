# -*- coding: utf-8 -*-
"""yolo_pothole_objectdetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O77Zb6Pp-k6QAa2_M_smq1I9MpRiJnIV

Pothole object detection
"""

# Commented out IPython magic to ensure Python compatibility.
#clone YOLOv5 and 
!git clone https://github.com/ultralytics/yolov5  
# %cd yolov5
# %pip install -qr requirements.txt 
# %pip install -q roboflow

import torch
import os
from IPython.display import Image, clear_output  

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="BFyUi8mrlKYGU0xjiLzI")
project = rf.workspace("jj-gitvi").project("pothole-pnro9")
dataset = project.version(1).download("yolov5")

!python train.py --img 416 --batch 16 --epochs 60 --data /content/yolov5/pothole-1/data.yaml --weights yolov5s.pt --cache

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
# %tensorboard --logdir runs

!python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source /content/yolov5/pothole-1/test/images/vlcsnap-2020-04-08-23h23m13s588_jpg.rf.65b84c97b0524e684d6b7d1385981dc3.jpg

import glob
from IPython.display import Image, display

for imageName in glob.glob('/content/yolov5/runs/detect/exp2/img-319_jpg.rf.701460a276c8f17f72e07348c99f0b5e.jpg'): #assuming JPG
    display(Image(filename=imageName))
    print("\n")

from google.colab import files
files.download('./runs/train/exp/weights/best.pt')
# Object Detection with Yolov5

First install the requirements in new environment:

```pip install -r requirements.txt```


## The Data Config file:
Create new .yaml file inside src/data following the example:

```
train: ../dataset/images/train/ 
val:  ../dataset/images/val/
test: ../dataset/images/test/

# number of classes
nc: 4

# class names
names: ["head"]
```

The realted yolov5(network size).yaml needs to be adapted to the number os classes or any other chance in the architecture. The file is in the src/models.

To train: (-- device if GPU)
```bash
python train.py --img 640 --cfg yolov5s.yaml --hyp hyp.scratch.yaml --batch 16 --epochs 100 --data 'your_yaml'.yaml --weights yolov5s.pt --workers 4 --name 'your_proj' --device 0
```

For inference: ( Check the save_txt flag on inference )
```bash
python detect.py --source ../dataset/images/test/ --weights runs/train/'your_proj'/weights/best.pt --conf 0.50 --save-txt --save-conf --name 'your_proj'
```

For metrics on test set:
```bash
python test.py --weights runs/train/'your_proj'/weights/best.pt --data 'your_yaml'.yaml --task test --name 'your_proj'
```


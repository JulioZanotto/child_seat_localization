import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from glob import glob
from tqdm.notebook import tqdm
import os
import shutil
import random
import json
from sklearn.model_selection import train_test_split

from utils.general import get_coords, extract_from_txt, convert_to_yolov5, generate_json_coco
from utils.plots import plot_one_box, plot_image_cropped_new

# Get all image files
all_files = glob('../dataset/*.png')

# Generate a dataframe and shuffle
dataframe = pd.DataFrame(all_files, columns=['Images'])
dataframe = dataframe.sample(frac=1).reset_index(drop=True)

# Split 10% to validation
X_train, X_val = train_test_split(dataframe, test_size=0.1)

# Move the files accordingly
for i in X_train.index:
    name_file = X_train.loc[i, 'Images']
    new_name = name_file.replace('.png', '.txt').replace('dataset', 'dataset_gt')
    shutil.move(new_name, './dataset_gt/train/')

for i in X_val.index:
    name_file = X_val.loc[i, 'Images']
    new_name = name_file.replace('.png', '.txt').replace('dataset', 'dataset_gt')
    shutil.move(new_name, './dataset_gt/val/')
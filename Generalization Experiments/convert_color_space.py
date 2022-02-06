# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:59:47 2021

@author: Jeonghan
"""

import cv2
from tqdm import tqdm
import os
"""
# Adding Set
for i in range (2, 11):
    in_path = f"./Datafolder/Add/train(Add_" + str(i) +")/fake/"
    out_path = f"./Datafolder/Add/train(Add_" + str(i) + ")(HSV)/fake/"
    
    
    for img_name in tqdm(os.listdir(in_path)):
        img = cv2.imread(os.path.join(in_path, img_name))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imwrite(os.path.join(out_path, img_name), img)
"""

# Test Set
in_path = f"./Datafolder/FFHQ/test(StyleGAN2)/fake/"
out_path = f"./Datafolder/FFHQ/test(StyleGAN2)(HSV)/fake/"

for img_name in tqdm(os.listdir(in_path)):
    img = cv2.imread(os.path.join(in_path, img_name))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite(os.path.join(out_path, img_name), img)


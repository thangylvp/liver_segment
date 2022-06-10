import cv2
import pandas as pd 
import os 
import numpy as np


if __name__ == "__main__":
    df_study = pd.read_csv("image_info.csv")
    df_imgmask = pd.read_csv("image_mask.csv")
    
    list_study = df_study['StudyInstanceUID'].unique().tolist()
    list_sop = df_study['ImageUID'].values
    img_with_mask = df_imgmask['image'].values
    sop_with_mask = []
    for item in img_with_mask:
        sop = item.split('/')[-1][:-4]
        sop_with_mask.append(sop)
    
    print("Number of study", len(list_study))
    print("Total images", len(list_sop))
    print("Images with liver", len(sop_with_mask))
    print("Images without liver", len(list_sop) - len(sop_with_mask))
    print("Mean number of images per study", )




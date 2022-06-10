import cv2
import pandas as pd 
import os 
import numpy as np


if __name__ == "__main__":
    root_dir = "/media/thangnv/data_ssd/Github/liver-segmentaion"
    df = pd.read_csv("image_mask.csv")
    print(df.head(10))


    sample = df.iloc[10]
    image = sample['image']
    mask = sample['mask']
    
    img_raw = cv2.imread(os.path.join(root_dir, image))
    mask = cv2.imread(os.path.join(root_dir, mask),0)

    zero_mat = np.zeros(mask.shape)
    mask3 = np.stack([zero_mat, zero_mat, mask], 2).astype(np.uint8)
    
    viz = cv2.addWeighted(img_raw, 1.0, mask3, 0.1, 0.0)
    cv2.imshow('img', img_raw)
    cv2.imshow('mask', mask)
    cv2.imshow('viz',viz)
    cv2.waitKey()





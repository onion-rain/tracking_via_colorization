import glob
import re
import os
import cv2
import shutil
import json
from tqdm import tqdm

from src.config import Config
    

def check_and_clear(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        shutil.rmtree(dir)
        os.makedirs(dir)

def video_cut(video_cap, root, stride=24):
    i = 1
    imgs = []
    while True:
        success, img = video_cap.read()
        if success is False:
            # print('video cut done')
            video_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return imgs
            # break
        if i % stride == 0:
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgs.append(rgb_img)
            if root != "":
                name = root + "0000"[: 4-len(str(int(i/stride)))] + str(int(i/stride)) + '.jpg'
                cv2.imwrite(name, img)
        i += 1

BaseRoot = Config.KMeansData.DATA_ROOT
video_paths = glob.glob(os.path.join(BaseRoot, "*"))
for path in tqdm(video_paths):
    try:
        video_cap = cv2.VideoCapture(path)
        SaveRoot = BaseRoot+os.sep+"slices"+os.sep+path.split(os.sep)[-1].split(".")[0]+os.sep
        check_and_clear(SaveRoot)
        video_cut(video_cap, SaveRoot, 200)
        # video_cut(video_cap, "", 200)
    except Exception:
        print(path)


'./dataset/tracking/davis/training/abseiling/ZgDAZ61fhg0_000091_000101.mp4'
'./dataset/tracking/davis/training/abseiling/slices'
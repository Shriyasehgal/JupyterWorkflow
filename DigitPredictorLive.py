import cv2,os
import numpy as np
from sklearn.externals import joblib
import pyscreeze as ImageGrab
import time
import pickle
model = pickle.load(open("DigitRec/model/Model","rb"))
image_folder='DigitRec/orig_images/6/'
for i in range(0,1000):
    time.sleep(8)
    im=ImageGrab.screenshot(region=(530,250, 250, 250))
    im.save(image_folder+'test.png')
    input_image=cv2.imread(image_folder+'test.png')
    im_gray=cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)

    im_gray=cv2.GaussianBlur(im_gray,(15,15),0)
    roi = cv2.resize(im_gray,(24,24),interpolation=cv2.INTER_AREA)
    data=[]
    rows,cols=roi.shape
    for i in range(rows):
       for j in range(cols):
           k= roi[i,j]
           if k>200:
               k=0
           else:
               k=1

           data.append(k)

    predictions=model.predict([data])
    print("prediction: ",predictions[0])

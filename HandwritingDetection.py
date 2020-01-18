import cv2,os
import numpy as np
from sklearn.externals import joblib
import csv
import glob


label=0
for label in range(6):
    print (label)

    dirList = glob.glob("DigitRec/orig_images/"+str(label)+"/*.png")
    for img_path in dirList:
        file_name=img_path.split("/")[2]


        im= cv2.imread(img_path)

        im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        im_gray=cv2.GaussianBlur(im_gray,(15,15),0)
        roi = cv2.resize(im_gray,(24,24),interpolation=cv2.INTER_AREA)

        data=[]
        data.append(label)
        rows,cols=roi.shape

        for i in range(rows):
           for j in range(cols):
               k= roi[i,j]
               if k>100:
                   k=1
               else:
                   k=0

               data.append(k)


        with open('DigitRec/csv/newtraindataset.csv','ab') as f:
            writer=csv.writer(f)
            writer.writerow(data)
         

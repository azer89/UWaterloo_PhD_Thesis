# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:01:43 2020

@author: azer
"""

import cv2
import numpy as np

input1 = cv2.imread('rabbit1.jpg')
img1 = cv2.cvtColor(input1, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
big_contour = max(cnts, key=cv2.contourArea)

input2 = cv2.imread('rabbit2.jpg')
img2 = cv2.cvtColor(input2, cv2.COLOR_BGR2GRAY)

cnts2 = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts2 = cnts2[0] if len(cnts2) == 2 else cnts2[1]
big_contour2 = max(cnts2, key=cv2.contourArea)

#for x in range(500):
#    for y in range(500):

raw_dist1 = np.empty(img1.shape, dtype=np.float32)
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        #raw_dist1[i,j] =
        d = cv2.pointPolygonTest(big_contour, (j,i), True)
        if(d >= 0):
            d = 0
        d = -d
        raw_dist1[i,j] = d
        

raw_dist2 = np.empty(img2.shape, dtype=np.float32)
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        # raw_dist2[i,j]
        d = cv2.pointPolygonTest(big_contour2, (j,i), True)
        if(d >= 0): 
            d = 0
        d = -d
        raw_dist2[i,j] = d
        

dist_3_img = np.empty(img1.shape, dtype=np.float32)
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        dist_3_img[i,j] = raw_dist1[i,j]
        if(raw_dist2[i,j] < raw_dist1[i,j]):
            dist_3_img[i,j] = raw_dist2[i,j]


result2 = cv2.normalize(dist_3_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imwrite('_distance_normalized.png', result2)
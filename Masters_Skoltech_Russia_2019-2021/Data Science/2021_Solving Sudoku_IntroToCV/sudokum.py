#import joblib

import numpy as np
from numpy import logical_and as land
from numpy import logical_not as lnot
from skimage.feature import canny
from skimage.transform import rescale, ProjectiveTransform, warp
from skimage.morphology import dilation, disk
import cv2 as cv
#import tensorflow
import torch
from tensorflow import keras

import matplotlib.pyplot as plt
from skimage import io
from skimage.io import imread


SCALE = 0.33


def predict_image(image):
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(img, (7, 7), 3)

    thresh = cv.adaptiveThreshold(blurred, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 2)
    thresh = cv.bitwise_not(thresh)
    ext_contours = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]

    for n, contour in enumerate(ext_contours):
        contour = np.array(contour).squeeze() # we need to remove one dim, se below
        
    contour = max(ext_contours, key= lambda x : cv.contourArea(x))
    contour = contour.squeeze()
    image = np.zeros(img.shape)
    fill = cv.fillPoly(image, [contour], (255, 255, 255))

    mask = np.bool_(fill)

    # loading train image:
    train_img_4 = cv.imread('/autograder/source/train/train_4.jpg', 0)
    
    epsilon = 0.05 * cv.arcLength(contour, True)
    corners = cv.approxPolyDP(contour, epsilon, True).squeeze()
    

    points_current = corners
    size = 324
    if corners[3][1] > corners[2][1]:
        points_desired = np.array([[0, 0],[0, size], [size, size],[size, 0]])   
        print('first')
    else:
        points_desired = np.array([[size, 0],[0, 0],[0, size], [size, size]])
        print('second')
    tform = ProjectiveTransform()
    tform.estimate(points_desired, points_current)
    image_warped = warp(img, tform)[:size, :size]
    
    ret, bw_img = cv.threshold(image_warped*255,100,255,cv.THRESH_BINARY)
    bw_img = (255-bw_img)
    

    cell_size = int(image_warped.shape[0]/9)
    cells = []
    for i in range(9):
        for j in range(9):
            c = bw_img[cell_size*i+4:cell_size*(i+1)-4,cell_size*j+4:cell_size*(j+1)-4]
            #c_scaled = rescale(img, 0.3, multichannel=False)
            cells.append(c)
            
    cells = np.array(cells)
    #c = image_warped[cell*7:cell*8,0:cell]

    
    


    # loading model:  (you can use any other pickle-like format)
    #model = joblib.load('/autograder/submission/model.joblib')
    #model = joblib.load('model.joblib')
 
    model = keras.models.load_model("/autograder/submission/mod.h5")
    #model = keras.models.load_model('C:/Users/admin/Desktop/Skoltech/Intro to CV/HW2/mod.h5')
    
    res = []

    for digit in cells:
        prediction = model.predict(digit.reshape(1, 28, 28, 1)) 
        if (max(sum(prediction)))<0.5:
            res.append(-1)
        else:
            res.append(np.argmax(prediction))
    
        
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    l9 = []
    for i in range(81):
        if i//9==0:
            l1.append(res[i])
        if i//9==1:
            l2.append(res[i])
        if i//9==2:
            l3.append(res[i])
        if i//9==3:
            l4.append(res[i])
        if i//9==4:
            l5.append(res[i])
        if i//9==5:
            l6.append(res[i])
        if i//9==6:
            l7.append(res[i])
        if i//9==7:
            l8.append(res[i])
        if i//9==8:
            l9.append(res[i])
    
    cell_res = [l1, l2, l3, l4, l5, l6, l7, l8, l9]
    
    #sudoku_digits = [
    #    np.int16([[-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #              [-1, -1, -1,  8,  9,  4, -1, -1, -1],
    #              [-1, -1, -1,  6, -1,  1, -1, -1, -1],
    #              [-1,  6,  5,  1, -1,  9,  7,  8, -1],
    #              [-1,  1, -1, -1, -1, -1, -1,  3, -1],
    #              [-1,  3,  9,  4, -1,  5,  6,  1, -1],
    #              [-1, -1, -1,  8, -1,  2, -1, -1, -1],
    #              [-1, -1, -1,  9,  1,  3, -1, -1, -1],
    #              [-1, -1, -1, -1, -1, -1, -1, -1, -1]]),]        
    sudoku_digits = [np.int16(cell_res),]
    #cell_res
    
    return mask, sudoku_digits



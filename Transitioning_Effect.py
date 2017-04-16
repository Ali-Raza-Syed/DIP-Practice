import numpy as np
import cv2

def dissolve(img1, img2, a, dim):

    img1 = cv2.resize(img1, dim);
    img2 = cv2.resize(img2, dim);
    dissolved_img = np.zeros(dim, dtype = np.uint8);
    for i in range(dim[0]):
        for j in range(dim[1]):
            new_intensity = (1 - a) * img1[i][j] + a * img2[i][j];
            if new_intensity > 255:
                new_intensity = 255;
            dissolved_img[i][j] = new_intensity;
    cv2.imshow('img1', img1);
    cv2.imshow('img2', img2);
    cv2.imshow('dissolved_img', dissolved_img);

    return

img1 = cv2.imread('Fig01.tif', 0);
img2 = cv2.imread('Fig02.tif', 0);
dissolve(img1, img2, 0.70, (500, 500));
cv2.waitKey(0);

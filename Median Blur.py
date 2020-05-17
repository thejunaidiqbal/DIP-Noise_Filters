# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:34:59 2020

@author: thejunaidiqbal
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    
    imgpath =  "images/abc.png"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    noisy = np.zeros(img.shape, np.uint8)
    
    p = 0.2
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r = random.random()
            if r < p/2:
                noisy[i][j] = [0, 0, 0]
            elif r < p:
                noisy[i][j] = [255, 255, 255]
            else:
                noisy[i][j] = img[i][j]

    denoised = cv2.medianBlur(noisy, 5)

    output = [img, noisy, denoised ]
    
    titles = ['Original', 'Noisy', 'Denoised']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


main()

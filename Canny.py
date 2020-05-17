# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:37:54 2020

@author: thejunaidiqbal
"""


import cv2
import matplotlib.pyplot as plt


def main():
    
    imgpath = "images/abc.png"
    img = cv2.imread(imgpath, 0)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    L1 = cv2.Canny(img, 50, 300, L2gradient=False)
    
    L2 = cv2.Canny(img, 100, 150, L2gradient=True)

    
    titles = ['Original Image', 'L1 Norm', 'L2 Norm']

    outputs = [img, L1, L2]
    
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(outputs[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


main()
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:37:17 2020

@author: thejunaidiqbal
"""


import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath =  "images/abc.png"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edgesx = cv2.Scharr(img, -1, dx=1, dy=0, scale=1,
                       delta=0, borderType=cv2.BORDER_DEFAULT)
    
    edgesy = cv2.Scharr(img, -1, dx=0, dy=1, scale=1,
                       delta=0, borderType=cv2.BORDER_DEFAULT)
    
    edges = edgesx + edgesy

    output = [img, edgesx, edgesy, edges]
    titles = ['Original', 'dx=1 dy=0', 'dx=0 dy=1', 'Edges']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i], cmap = 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

main()
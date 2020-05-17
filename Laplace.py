# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:35:44 2020

@author: thejunaidiqbal
"""


import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath =  "images/abc.png"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edges = cv2.Laplacian(img, -1, ksize=29, scale=1, delta=0, 
                          borderType=cv2.BORDER_DEFAULT)

    output = [img, edges]
    titles = ['Original', 'Edges']
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(output[i], cmap = 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


main()
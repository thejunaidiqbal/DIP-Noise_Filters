# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:29:21 2020

@author: thejunaidiqbal
"""


import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath = "images/abc.png"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    

  
    plt.imshow(img)
    plt.title('Image with Salt and Pepper Noise')
    plt.show()


main()
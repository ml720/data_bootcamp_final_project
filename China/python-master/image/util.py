import numpy as np

h = 660
w = 1000
imgWin = np.zeros((h,w,3), np.uint8)
background = (0,0,255)
fontColor = (255,255,255)
imgWin[0:h,0:w] = background

def getImg():
    return imgWin

def addImg(img, startH, startW):

    global imgWin
    imgH = img.shape[0]
    imgW = img.shape[1] 
    imgWin[startH:startH+imgH, startW:startW+imgW] = img

def getBackground() :
    return background

def getFontColor() :
    return fontColor
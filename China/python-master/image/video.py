import chinese
import cv2
import english
import util
import factory
import numpy as np

#imgWin = np.zeros((fontSize,width,3),np.uint8)
chinese.setFontSize(82)
img = chinese.createChineseText("中国")
factory.addImages(img)

img = chinese.createChineseText("江西")
factory.addImages(img)

img = chinese.createChineseText("萍乡")
factory.addImages(img)

cImg = chinese.createChineseText("1929年")
eImg = english.createEnglishText(". . . . . .")
cH = cImg.shape[0]
cW = cImg.shape[1]
eH = eImg.shape[0]
eW = eImg.shape[1]
img = np.zeros((cH,cW,3))
img[0:cH,0:cW] = cImg
s = cW-eW-40
img[0:cH,s:s+eW] = eImg

#img[0:cH,cW-150:cW+eW-150] = eImg

factory.addImages(img)

factory.createWindow()
winImg = util.getImg()

#winImg = english.createEnglishText("asdf")
cv2.imshow("win", winImg)
cv2.waitKey()
#cv2.imshow("res", img)
#cv2.waitKey()
cv2.destroyAllWindows

cv2.imwrite("firstpage.jpg",util.getImg())

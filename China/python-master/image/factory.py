import util
import cv2

images = []
count = 0
height = 0
width = 0
xOverlay = 40
ySkip = 20

def addImages(image):
    global images
    global height
    global width
    global count
    images += [image]
    count += 1
    height += image.shape[0]
    print(height)
    width += image.shape[1]
    
    
    
def createWindow():
    startX = (util.w-width+count*xOverlay)/2
    startY = (util.h-height-count*ySkip)/2
    h = 0
    w = 0
    cnt = 0
    for img in images:
#        cv2.waitKey()
        util.addImg(img, startY+h+cnt*ySkip, startX+w-cnt*xOverlay)
        h += img.shape[0]
        w += img.shape[1]
        cnt += 1
#        cv2.imshow("win1", util.getImg())
   
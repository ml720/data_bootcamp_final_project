import numpy as np
import util
import cv2
from PIL import ImageFont, ImageDraw, Image

fontSize = 36


def createEnglishText(txt):
    txtLen = len(txt)
    width = txtLen*10
    print(width)
    img = np.zeros((fontSize,width,3),np.uint8)
    ## Use simsum.ttc to write Chinese.
    fontpath = "arial" 
    font = ImageFont.truetype(fontpath, fontSize)

    img_pil = Image.fromarray(img)
    img_pil = Image.new("RGB",(width, 82),util.getBackground())

    draw = ImageDraw.Draw(img_pil)
    draw.text( (0,50), txt, font=font, fill=util.getFontColor())
    img = np.array(img_pil)
    return img

def setFontSize(size):
    global fontSize
    fontSize = size;


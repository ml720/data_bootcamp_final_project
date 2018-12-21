import numpy as np
from PIL import ImageFont, ImageDraw, Image
import util

fontSize = 160


def createChineseText(txt):
    txtUtf8 = txt.decode('utf8')
    txtLen = len(txtUtf8)
    width = txtLen*fontSize
    img = np.zeros((fontSize,width,3),np.uint8)
    
    ## Use simsum.ttc to write Chinese.
    fontpath = "simsun.ttc" 
    font = ImageFont.truetype(fontpath, fontSize)

    img_pil = Image.fromarray(img)
    img_pil = Image.new("RGB",(width, fontSize),util.getBackground())

    draw = ImageDraw.Draw(img_pil)
    draw.text( (0,0), unicode(txt,'UTF-8'), font=font, fill=util.getFontColor())
    img = np.array(img_pil)
    return img

def setFontSize(size):
    global fontSize
    fontSize = size;

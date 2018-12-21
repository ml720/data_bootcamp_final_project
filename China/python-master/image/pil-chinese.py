import numpy as np
from PIL import ImageFont, ImageDraw, Image

## Use simsum.ttc to write Chinese.
fontpath = "simsun.ttc" # <== 这里是宋体路径 
font = ImageFont.truetype(fontpath, 72)

img_pil = Image.new("RGB",(500,100),(0,0,0))
txt =  "这里是宋体路径"
draw = ImageDraw.Draw(img_pil)
draw.text( (0,0), unicode(txt,'UTF-8'), font=font)
#cv2.putText(img, "---", (200,150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (b,g,r),1)

#from __future__ import print_function
print(img_pil.format, img_pil.size, img_pil.mode)
img_pil.show()

f = open("pil-chinese.bmp", "w")
img_rgb = img_pil.convert("RGB")
img_rgb.save(f)

f.flush()
f.close()
#cv2.putText(img,  "--- by Silencer", (200,150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (b,g,r), 1, cv2.LINE_AA)


## Display 
#cv2.imshow("res", img);cv2.waitKey();cv2.destroyAllWindows()
#cv2.imwrite("res.png", img)


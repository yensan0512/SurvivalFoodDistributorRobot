#import urllib
import urllib.request
import cv2
import numpy as np



url='http://10.73.39.186:8080//photoaf.jpg'

while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # all the opencv processing is done here
    cv2.imwrite("opencv123.jpg", img)
    #cv2.imwrite('test123',img)
    exit(0)
'''
Get and save images from camera
@author Kan Mayoshi <k_mayoshi@ac.jaxa.jp>
Usage: $ python camera.py
'''

import os
import cv2
from skimage import io

if os.path.exists("./image") == False:
    os.mkdir('./image')

count = 0   
uri = 'http://192.168.201.61/axis-cgi/jpg/image.cgi?resolution=640x480'

while(True):
    # img = cv2.imread(uri) ?
    img = io.imread(uri)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    cv2.imshow('camera image',img)
    cv2.imwrite('./image/image%05d.png'%count,img)

    print 'FRAME =',count
    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print 'quit'
        break

cv2.destroyAllWindows()

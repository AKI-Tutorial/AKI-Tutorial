import cv2
import numpy as np
#import urllib2

#cap = cv2.VideoCapture("rtsp://192.168.201.15/mpeg4?overlay=off")
#cap = cv2.VideoCapture("rtsp://192.168.201.15/mjpg?overlay=off")
cap = cv2.VideoCapture("rtsp://192.168.201.15/avc?overlay=off")

count = 1

while(True):  # while(cap.isOpened())
    # Capture frame-by-frame
    ret, img = cap.read()

    # Display the thermal image
    cv2.imshow("Thermal image",img)

    # Save the image
    cv2.imwrite("thermal%d.png" %count,img)

    ##### Visual mode #####
    # vis_url = "http://192.168.201.15/home/setviewmode/VISUAL"
    # urllib2.urlopen(vis_url)
    # cv2.waitKey(500)
    # ret, vis = cap.read()
    # cv2.imwrite("visual%d.png" %count,vis)

    ##### Fusion(IR + Visual) mode #####
    # fus_url = "http://192.168.201.15/home/setviewmode/FUSION"
    # urllib2.urlopen(fus_url)
    # cv2.waitKey(500)
    # ret, fus = cap.read()
    # cv2.imwrite("fusion%d.png" %count,fus)

    # back to ir mode
    # ir_url = "http://192.168.201.15/home/setviewmode/IR"
    # urllib2.urlopen(ir_url)

    count = count + 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

cv2.waitKey(0)

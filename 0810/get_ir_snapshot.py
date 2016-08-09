'''
Get and save image from IR camera
@author Satoshi Watanabe
@author Kyohei Otsu <kyon@ac.jaxa.jp>
Usage: $ python get_ir_snapshot.py
'''

import cv2
import numpy as np
#import urllib2


def main():
    ### URI setting ###
    ipaddr = '192.168.201.15'
    uri = 'rtsp://{}/avc?overlay=off'.format(ipaddr)

    ### Camera option ###
    # viewmode_uri = 'http://{}/home/setviewmode/IR'    .format(ipaddr)  # IR
    # viewmode_uri = 'http://{}/home/setviewmode/VISUAL'.format(ipaddr)  # RGB 
    # viewmode_uri = 'http://{}/home/setviewmode/FUSION'.format(ipaddr)  # IR + RGB
    # urllib2.urlopen(viewmode_uri)
    # cv2.waitKey(500)

    ### get a single image from camera ###
    cap = cv2.VideoCapture(uri)
    ret, img = cap.read()
    if img is None: return

    ### show image ###
    cv2.imshow('Thermal image', img)
    cv2.waitKey(1)

    ### save as file ###
    write_enable = False
    if write_enable:
        cv2.imwrite('./ir_image.png', img)

    ### fianlizing ###
    cap.release()


if __name__ == '__main__':
    main()

    print 'Press enter to exit...'
    raw_input()


'''
Get and save images from camera
@author Kan Mayoshi <k_mayoshi@ac.jaxa.jp>
@author Kyohei Otsu <kyon@ac.jaxa.jp>
Usage: $ python get_camera_snapshot.py
'''

import os
import cv2
from skimage import io


def get_snapshot(uri):
    ''' Get snapshot from camera using HTTP request
        Returns:
            A single BGR image
            (*) OpenCV uses BGR as the default color space (not RGB)
    '''
    img = io.imread(uri)  # get image
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # convert color space (RGB --> BGR)
    return img


def main():
    ### URI setting ###
    uri = 'http://49.212.135.60/p/79/75279/20973301.jpg'  # DUMMY

    ### get a single image from camera ###
    print 'Sending image request to', uri
    img = get_snapshot(uri)

    ### show image ###
    cv2.imshow('camera image', img)
    cv2.waitKey(1)

    ### save as file ###
    write_enable = False
    if write_enable:
        cv2.imwrite('./image.png', img)
    

if __name__ == '__main__':
    main()

    print 'Press enter to exit...'
    raw_input()


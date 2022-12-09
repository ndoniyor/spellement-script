import sys
import time

import cv2
import numpy as np
import pyautogui
import pytesseract
from mss import mss
from PIL import Image


def pre_processing(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(processed_image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18,18))
    
    dilation = cv2.dilate(thresh, rect_kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    #copy_proc_img = image.copy()
    #processed_image = cv2.Canny(processed_image, threshold1=1000,threshold2=500)
    return [processed_image,contours]

def main():
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
    health_box = {'top': 40, 'left': 87, 'width': 100, 'height': 50}
    frame_rate = 0
    sct = mss()
    prev_frame = time.time()
    while True:
        #frame_rate = (time.time()-prev_frame)**-1
        #sys.stdout.write("\rFrame rate: {} Hz".format(int(frame_rate)))
        #sys.stdout.flush()
        #prev_frame = time.time()
        
        pre_process= np.array(sct.grab(health_box))
        post_process, contours = pre_processing(pre_process)
        cv2.imshow('screen', post_process)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            rect = cv2.rectangle(pre_process,(x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped = pre_process[y:y + h, x:x + w]
            text = pytesseract.image_to_string(cropped)
            #sys.stdout.write(text)
            print(text)

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
if __name__ == "__main__":
    main()

import cv2
import numpy as np

sumber = cv2.VideoCapture(0)

while(True):
    _, tampil = sumber.read()
    gambarHSV = cv2.cvtColor(tampil, cv2.COLOR_BGR2HSV)
    warna_bawah = np.array([18, 40, 90], np.uint8)
    warna_atas = np.array([27, 255, 255], np.uint8)
    warna_mask = cv2.inRange(gambarHSV, warna_bawah, warna_atas)
    kernal = np.ones((5,5), "uint8")
    warna_mask = cv2.dilate(warna_mask, kernal)
    res_warna = cv2.bitwise_and(tampil, tampil,mask = warna_mask)
    contours, hierarchy = cv2.findContours(warna_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 100):
            x, y, w, h = cv2.boundingRect(contour)
            tampil = cv2.rectangle(tampil, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(tampil, "Bola", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))
    cv2.imshow('kamera', tampil)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
sumber.release()
cv2.destroyAllWindows()
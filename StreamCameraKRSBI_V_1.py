import cv2

sumber = cv2.VideoCapture(0)

while(True):
    ret, tampil = sumber.read()
    cv2.imshow('kamera', tampil)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
sumber.release()
cv2.destroyAllWindows()
import streamlink
import cv2
import time

url = 'https://www.youtube.com/watch?v=PbzrnUW70gU'

streams = streamlink.streams(url)
cap = cv2.VideoCapture(streams["best"].url)
i=0
while True:
    time.sleep(1)
    ret, frame = cap.read()

    cv2.imwrite("frame%d.jpg" % i,frame)
    i=i+1

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
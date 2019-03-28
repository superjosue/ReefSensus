import streamlink
import cv2
import time
url2= "https://www.youtube.com/watch?v=ifqYuTn_6MI"  #explorer North Carolina
url1 = 'https://www.youtube.com/watch?v=PbzrnUW70gU' #deerfield

streams = streamlink.streams(url2)
cap = cv2.VideoCapture(streams["best"].url)
i=0
while True:
    time.sleep(1)
    ret, frame = cap.read()

    cv2.imwrite("frame%d.jpg" % i,frame)
    i=i+1



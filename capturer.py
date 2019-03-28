import streamlink
import cv2
import time
import datetime as dt
test ="https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8"
url2= "https://www.youtube.com/watch?v=ifqYuTn_6MI"  #explorer North Carolina
url1 = 'https://www.youtube.com/watch?v=PbzrnUW70gU' #deerfield
timeSpam=dt.datetime.now()
streams = streamlink.streams(test)
cap = cv2.VideoCapture(streams["best"].url)
i=0
while True:
    time.sleep(1)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("Photo%d.jpg" % i,frame)
        print("saving Photo%d.jpg" % i )
        i=i+1
    print("nothing to Save")


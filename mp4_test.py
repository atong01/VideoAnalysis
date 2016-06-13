import cv2
import cv2.cv as cv
#c= cv2.VideoCapture("Tack1.mp4")
#print c.grab() # returns false. however returns true if use avi file.

cap = cv.CaptureFromFile("Tack1.Mp4")

nframes=int(cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_FRAME_COUNT))
fps= int(cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_FPS))
print "total frame",cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_FRAME_COUNT)
print "fps" ,fps
print " currpos of videofile",cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_POS_MSEC)
waitpermillisecond=int(1*1000/fps)
print "waitpermillisecond",waitpermillisecond
print cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_FOURCC)

for f in xrange(nframes):
    frameimg=cv.QueryFrame(cap)
    print " currpos of videofile",cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_POS_MSEC)
    print " index of frame",cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_POS_FRAMES)
    cv.ShowImage("hcq",frameimg)
    cv.WaitKey(1)

cv.DestroyAllWindows("hcq")

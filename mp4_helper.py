import cv2
import cv2.cv as cv

from argparse import ArgumentParser

def view(cap, frame = 0, length = -1):
    for f in xrange(frame, frame + length):
        img = cv.QueryFrame(cap)
        cv.ShowImage('img', img)
        cv.WaitKey(1)
def parseVideo():
    ap = ArgumentParser()
    ap.add_argument('-f', '--file', default = 'default.mp4', help='video file to load')
    r = ap.parse_args()
    return r.file

if __name__ == "__main__":
    video = parseVideo()
    cap   = cv.CaptureFromFile(video)
    view(cap, length = 10)

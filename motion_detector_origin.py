# USAGE
# python motion_detector.py
# python motion_detector.py --video videos/example_01.mp4

import argparse
import datetime
import imutils
import time
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

if args.get("video", None) is None:
	camera = cv2.VideoCapture(0)
	time.sleep(0.25)

else:
	camera = cv2.VideoCapture(args["video"])

firstFrame = None
j=0
while True:
	(grabbed, frame) = camera.read()

	if not grabbed:
		break

	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray_temp = gray
	gray = cv2.GaussianBlur(gray, (21, 21), 0)


	if firstFrame is None:
		firstFrame = gray
		continue

	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

	thresh = cv2.dilate(thresh, None, iterations=17)
	thresh = cv2.erode(thresh,None,iterations = 17)
	image, cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

	for c in cnts:
		if cv2.contourArea(c) < args["min_area"]:
			continue
	cv2.imwrite("selfie_mask/image" + str(j) + ".png", thresh)
	cv2.imwrite("selfie_input/image" + str(j) + ".png", frame)
	cv2.imshow("Security Feed", frame)
	temp_mask1=cv2.imread("selfie_mask/image"+str(j)+".png")
  	frame1=cv2.imread("selfie_input/image"+str(j)+".png")
  	max_value= np.max(temp_mask1)
  	temp_mask1/=max_value
  	res1 = frame1*temp_mask1
  	cv2.imwrite("selfie_result/image" + str(j) + ".png", res1)
	j=j+1
	if cv2.waitKey(10) == 27:
		break
    	#key = cv2.waitKey(1) & 0xFF
	#if key == ord("q"):
	#	break
camera.release()
cv2.destroyAllWindows()
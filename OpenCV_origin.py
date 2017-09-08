import numpy as np
import cv2
import skimage.io as io
 
cap = cv2.VideoCapture('video2_1_400.mp4')
fourcc = cv2.VideoWriter_fourcc(*'H264')
fgmask = []
temp_mask=cv2.imread("selfie_res/image"+str(1)+".png")
for i in xrange(1,271):
  fgmask.append(cv2.imread("selfie_res/image"+str(i)+".png"))
j=0
#fgbg = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold = 25,detectShadows=False)
#out = cv2.VideoWriter('video4_result.mp4',fourcc, 24.0, (temp_mask.shape[0],temp_mask.shape[1]),True)
while(j<270):
  temp_mask=cv2.imread("selfie_mask/image"+str(j)+".png")
  frame=cv2.imread("selfie_input/image"+str(j)+".png")
  #fps = cap.get(cv2.CAP_PROP_POS_MSEC)
  max_value= np.max(temp_mask)
  temp_mask/=max_value
  res = frame*temp_mask
  cv2.imwrite("selfie_result/image" + str(j) + ".png", res)
  #cv2.imshow('frame',res)
  #io.imsave('selfie_res/image'+str(j)+'.png', res)
  #out.write(res)
  j=j+1
  k = cv2.waitKey(30) & 0xff
  if k == 27:
    break
cap.release()
#out.release()
cv2.destroyAllWindows()
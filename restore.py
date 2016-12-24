import sys
import cv2
import numpy as np

inFile = sys.argv[1]
outFile = sys.argv[2]
threshold = int(sys.argv[3])

img = cv2.imread(inFile)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
mask = np.zeros(im.shape[:-1], np.uint8)
for i in range(gray.shape[0]):
  if np.cov(gray[i, :]) < threshold:
    mask[i, :] = 1
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
cv2.imwrite(outFile, dst)

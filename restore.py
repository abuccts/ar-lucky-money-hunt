#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np


def inpaint(inFile, outFile, threshold):
  img = cv2.imread(inFile)
  gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  mask = np.zeros(im.shape[:-1], np.uint8)
  for i in range(gray.shape[0]):
    if np.cov(gray[i, :]) < threshold:
      mask[i, :] = 1
  dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
  cv2.imwrite(outFile, dst)

  
if __name__ == "__main__":
  inFile, outFile = sys.argv[1], sys.argv[2]
  threshold = int(sys.argv[3]) if len(sys.argv) > 3 else 300
  inpaint(inFile, outFile, threshold)

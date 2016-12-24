#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ar-lucky-money-hunt: image restoration for alipay ar lucky money based on
inpainting algorithms
Please refer to README for more details.

Copyright (C) 2016 Yifan Xiong
https://github.com/abuccts/ar-lucky-money-hunt

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""


import sys
import cv2
import numpy as np


def inpaint(inFile, outFile, threshold):
  img = cv2.imread(inFile)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  mask = np.zeros(img.shape[:-1], np.uint8)
  for i in range(gray.shape[0]):
    if np.cov(gray[i, :]) < threshold:
      mask[i, :] = 1
  dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
  cv2.imwrite(outFile, dst)

  
if __name__ == "__main__":
  inFile, outFile = sys.argv[1], sys.argv[2]
  threshold = int(sys.argv[3]) if len(sys.argv) > 3 else 300
  inpaint(inFile, outFile, threshold)

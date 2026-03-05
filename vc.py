import cv2
import numpy as np
import random

img = cv2.imread("input/sample.png", 0)

_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

h, w = binary.shape

share1 = np.zeros((h, w*2), dtype=np.uint8)
share2 = np.zeros((h, w*2), dtype=np.uint8)

for i in range(h):
    for j in range(w):
        pixel = binary[i][j]
        r = random.choice([0,1])

        if pixel == 255:
            pattern = [[255,0],[0,255]][r]
            share1[i,2*j:2*j+2] = pattern
            share2[i,2*j:2*j+2] = pattern
        else:
            pattern1 = [[255,0],[0,255]][r]
            pattern2 = pattern1[::-1]
            share1[i,2*j:2*j+2] = pattern1
            share2[i,2*j:2*j+2] = pattern2

cv2.imwrite("output/share1.png", share1)
cv2.imwrite("output/share2.png", share2)

reconstructed = cv2.bitwise_or(share1, share2)
cv2.imwrite("output/reconstructed.png", reconstructed)

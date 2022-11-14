import cv2
import numpy as np
import matplotlib.pyplot as plt

src_points = np.array([[518,781],[532,827],[668,771],[863,775],[864,820 ]])
dest_points = np.array([[1172,584],[1174,620],[1284,570],[1460,590],[1442,633]])


h, status = cv2.findHomography(src_points, dest_points)
print(h)
im_src = cv2.imread('image1.png')
im_dst = cv2.imread('image2.png')

im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

cv2.imshow("Warped_Source_Image", im_out)
plt.imshow(im_out)
plt.show()

#Coordinates for image1
# 139   730
# 123   318
# 775   734
# 148   75
# 783   323




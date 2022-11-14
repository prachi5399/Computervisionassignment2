import numpy as np
import cv2

imgPath=["Test1/pic1.jpg","Test1/pic2.jpg","Test1/pic3.jpg"]

imgPath2=["Test2/store1.jpg","Test2/store2.jpg","Test2/store3.jpg"]

imgPath3=["Test3/store5.jpg","Test3/store6.jpg","Test3/store7.jpg"]

imgPath4=["Test4/pc1.jpg","Test4/pc2.jpg","Test4/pc3.jpg"]

imgPath5=["Test5/pp1.jpg","Test5/pp2.jpg","Test5/pp3.jpg"]

images = []

for path in imgPath5:
	image = cv2.imread(path)
	images.append(image)

print(len(images))
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
	print("Image Stitching Successful")
	cv2.imshow("Stitched Image", stitched)
	cv2.imwrite("imgstitched5.png",stitched)
	cv2.waitKey(0)
else:
	print("[INFO] Failed Image Stitching ({})"/format(status))

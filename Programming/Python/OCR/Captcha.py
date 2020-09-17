import cv2
import numpy as np
import argparse
import os
import pytesseract
from PIL import Image 

def rotate_image(mat, angle):
    height, width = mat.shape[:2] 
    image_center = (width/2, height/2) 

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)
    
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

colorized = cv2.imread(args["image"])
image = cv2.cvtColor(colorized, cv2.COLOR_BGR2GRAY)

if args["preprocess"] == "thresh":
	image = cv2.threshold(image, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif args["preprocess"] == "blur":
	image = cv2.medianBlur(image, 3)

s = 0
for angle in np.arange(0,360,15):
	rotated = rotate_image(image,angle)
	cv2.imshow("Hatdog",rotated)
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, image)
	text = pytesseract.image_to_string(Image.open(filename))
	print(text)
	os.remove(filename)
	print(angle)
	cv2.waitKey(0)
	if text != "":
		print("This angle is successful:", angle)
		s = 1

if s == 0:
	print("No angle was succesful")

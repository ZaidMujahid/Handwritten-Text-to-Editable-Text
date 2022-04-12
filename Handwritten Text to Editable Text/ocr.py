from PIL import Image
import pytesseract
import argparse
import cv2
import os

def ocr(imgPath):

	image = cv2.imread(imgPath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	options = "-l {}".format("hin")
	text = pytesseract.image_to_string(Image.open(filename), config=options)
	os.remove(filename)

	return text
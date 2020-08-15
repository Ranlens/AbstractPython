import cv2
import sys

imgen = cv2.imread("foto_eu.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayImageInv = 255 - grayImage
grayImageInv = cv2.GaussinanBlur(grayImageInv, (21, 21), 0)
output = cv2.divde(grayImage, 255-grayImageInv, scale=256.0)
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)
cv2.imshow("image", image)
cv2.imshow("pencelsketch", output)
cv2.waitKey(0)
cv2.destroyAllwimdows()
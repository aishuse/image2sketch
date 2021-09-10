import cv2

image=cv2.imread("baby.jpg")   # read the image
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)   # convert the colored image into grayscale
cv2.imwrite("gray.png",gray_image)  # save the gray scale image

# apply inverted filter..

inverted_image=255-gray_image
cv2.imwrite("inv.png",inverted_image)

# apply gaussian blur to get blur image

blur=cv2.GaussianBlur(inverted_image,(21,21),0)
cv2.imwrite("blur.png",blur)

#convert blur image to inverted

inv_blur=255-blur
cv2.imwrite("inv_blur.png",inv_blur)

#convert it into sketch image..The sketch can be obtained by performing bit-wise division between the grayscale image and the inverted-blurred image.

sketch=cv2.divide(gray_image,inv_blur,scale=256.0)
cv2.imwrite("sktch.png",sketch)

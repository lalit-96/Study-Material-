import cv2

img=cv2.imread("galaxy.jpg",0)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img=cv2.resize(img,(1600,900))
cv2.imshow("Small",resized_img)
cv2.imwrite("galaxy_new.jpg",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

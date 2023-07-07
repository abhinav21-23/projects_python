import cv2

scale_percent = 50
source = "hero-3.jpg"
destination = "new_image.png"

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv2.resize(image, dsize)
cv2.imwrite(destination, output)
# cv2.waitKey(0)

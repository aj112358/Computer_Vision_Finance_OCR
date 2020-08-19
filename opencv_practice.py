import cv2

my_image = cv2.imread('sample_student.jpg', cv2.IMREAD_COLOR)

cv2.imshow("Look, it's Pikachu!", my_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
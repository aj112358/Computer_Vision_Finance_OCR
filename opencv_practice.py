import cv2

my_image = cv2.imread('Handwriting_Tests/handwriting_test_ADF.jpg', cv2.IMREAD_COLOR)
# my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)

image_height, image_width, _ = my_image.shape
SCALE_FACTOR = 0.35
WIDTH = int(image_width*SCALE_FACTOR)
HEIGHT = int(image_height*SCALE_FACTOR)
# my_image = cv2.resize(my_image, (WIDTH, HEIGHT)) 

R = 255
G = 0
B = 0
thickness = 1
pixel_to_mm = 0.2645833333 # 1pixel = 0.2645833333mm BUT NOT ALWAYS THE SAME SIZE!!

(x,y) = (178,182)
w = 72
h = 70
(X,Y) = (x+w,y+h)

cropped = my_image[y:Y+1, x:X+1]

# cv2.imshow("The cropped image", cropped)
cv2.imwrite("test_big_letter.jpg", cropped)
# cv2.rectangle(my_image, (x,y), (X,Y), (B,G,R), thickness)







# Testing all box placements
# dx = w
# dy = h
offset = -2
for i in range(0,26):
    offset += 1
    cv2.rectangle(my_image, (x+(w+6)*i+offset,y), (X+(w+6)*i+offset,Y), (B,G,R), thickness)




# cv2.namedWindow("Look, it's Pikachu!", cv2.WINDOW_NORMAL)
cv2.imshow("Look, it's Pikachu!", my_image)
cv2.waitKey(0)
cv2.destroyAllWindows()





###### OLD CODES



# (x,y) = (62,64)
# w = 25
# h = 24
# (X,Y) = (x+w,y+h)

# cv2.rectangle(my_image, (x,y), (X,Y), (B,255,R), thickness)


# cv2.rectangle(my_image, (x,y), (X,Y), (B,255,R), thickness)
# cropped = my_image[y:Y+1, x:X+1]
# cv2.imshow("The cropped image", cropped)
# cv2.imwrite("test_letter.jpg", cropped)


# cv2.rectangle(my_image, (x+w+1+1,y), (X+w+1+1,Y), (B,G,R), thickness)
# cropped2 = my_image[y:Y+1, x+w+3:X+w+3]
# cv2.imshow("The cropped image", cropped2)
# cv2.imwrite("test_letter2.jpg", cropped2)

# cropped3 = my_image[y:Y+1, x+2*w+6:X+2*w+6]
# cv2.imshow("The cropped image", cropped3)
# cv2.imwrite("test_letter3.jpg", cropped3)


# cropped4 = my_image[y:Y+1, x+3*w+8:X+3*w+8]
# cv2.imshow("The cropped image", cropped3)
# cv2.imwrite("test_letter4.jpg", cropped4)



# cropped5 = my_image[y:Y+1, x+4*w+11:X+4*w+11]
# cv2.imshow("The cropped image", cropped3)
# cv2.imwrite("test_letter5.jpg", cropped5)



# cropped6 = my_image[y:Y+1, x+5*w+13:X+5*w+13]
# cv2.imshow("The cropped image", cropped3)
# cv2.imwrite("test_letter6.jpg", cropped6)
import cv2

# my_image = cv2.imread('Handwriting_Tests/handwriting_ADF_dotted.jpg', cv2.IMREAD_COLOR) # Works with the rows
# my_image = cv2.imread('Handwriting_Tests/handwriting_ScanBed_dottedPaper.jpg', cv2.IMREAD_COLOR) # Doesnt work with rows
# my_image = cv2.imread('Handwriting_Tests/handwriting_ADF_dotted(BEST).jpg', cv2.IMREAD_COLOR) # Seems to work with rows

# my_image = cv2.imread('Handwriting_Tests/bed1.jpg', cv2.IMREAD_COLOR)
# my_image = cv2.imread('Handwriting_Tests/bed2.jpg', cv2.IMREAD_COLOR)


my_image = cv2.imread('Handwriting_Samples/uppercase.jpg', cv2.IMREAD_COLOR)


# my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)

# cv2.rectangle(my_image, (185,210), (205,230), (255,255,0), 2)

##############
temp = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
current_max = 255
# (i_max, j_max) = (0,0)
i_max = 0
j_max = 0
count = 0
for i in range(185,205+1):
    for j in range(210,230+1):
        
        if temp[j,i] < current_max:
            # print(temp[j,i])
            current_max = temp[j,i]
            i_max = i
            j_max = j
            # (i_max, j_max) = (i,j)
            count += 1

print(current_max)
print(count)
print(f"({i_max},{j_max})")

my_image[j_max,i_max] = [0,255,255]
##############


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

(x,y) = (i_max,j_max) # Both used to be 178
w = 72
h = 72
(X,Y) = (x+w,y+h)

cropped = my_image[y:Y+1, x:X+1]

# cv2.imshow("The cropped image", cropped)
cv2.imwrite("test_big_letter.jpg", cropped)
# cv2.rectangle(my_image, (x,y), (X,Y), (B,G,R), thickness)




LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
SMALL_LETTERS = [x.lower() for x in LETTERS]
# print(SMALL_LETTERS, end=" ")

# Testing all box placements
# dx = w
# dy = h

y_offset = 0 # Was -39
for j in range(0,35):
    # y_offset += 1

    if j in range(0,3): # A-C
        y_offset += 3 
    elif j in range(3,6): # D-F
        y_offset += 3
    elif j in range(6,9): # G-I
        y_offset += 6
    elif j in range(9,12): # J-L
        y_offset += 3
    elif j in range(12,15): # M-O
        y_offset += 9
    elif j in range(15,18): # P-R
        y_offset += 3
    elif j in range(18,21): # S-U
        y_offset += 6
    elif j in range(21,24): # V-X
        y_offset += 6
    elif j in range(24,27): # Y,Z,1
        y_offset += 3
    elif j in range(27,30): # 2-4
        y_offset += 6
    elif j in range(30,33): # 5-7
        y_offset += 3
    else:                   # 8,9
        y_offset += 9   
    
    
    
    x_offset = 2 # Was 15
    for i in range(0,26):

        if i in range(0,5):
            x_offset += 1 # A-E
        elif i in range(5,10): # F-J
            x_offset += 0
        elif i in range(10,15): # K-O
            x_offset += 1
        elif i in range(15,20): # P-T
            x_offset += 1
        elif i in range(20,23): # U-W
            x_offset += 1
        else:
            x_offset += 0 # X-Z

        # cv2.rectangle(my_image, (x+(w+6)*i+x_offset,y+(h+1)*j+y_offset), (X+(w+6)*i+x_offset,Y+(h+1)*j+y_offset), (B,G,R), thickness)
            
        cropped = my_image[y+(h+1)*j+y_offset:Y+(h+1)*j+y_offset, x+(w+6)*i+x_offset:X+(w+6)*i+x_offset+1]
        
        cv2.imwrite(f"Uppercase/{LETTERS[i]}_{j+1}.jpg", cropped)



# x_offset = 15 # was -2 for the solid line test sheet
# y_offset2 = -5
# for i in range(0,26):
#     x_offset += 1
#     cv2.rectangle(my_image, (x+(w+6)*i+x_offset,y+5*h+y_ offset2), (X+(w+6)*i+x_offset,Y+5*h+y_offset2), (B,G,R), thickness)
    
    # cropped = my_image[y+5*h+y_offset2:Y+5*h+y_offset2+1, x+(w+6)*i+x_offset:X+(w+6)*i+x_offset+1]
    # cv2.imwrite(f"test_big_letter_{LETTERS[i]}.jpg", cropped)





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
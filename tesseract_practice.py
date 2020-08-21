print("Hello world")

# from PIL import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

my_image = cv2.imread("sample_student.jpg")
my_image2 = cv2.imread("sample_student_no_back_sheet.jpg")
# my_image3 = cv2.imread("handwriting_test_ADF.jpg")
# my_image3 = cv2.imread("handwriting_ScanBed_dottedSolid.jpg")
# my_image3 = cv2.imread("handwriting_ScanBed_thinSolid.jpg")
my_image3 = cv2.imread("handwriting_ScanBed_dottedPaper.jpg")

my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
my_image3 = cv2.cvtColor(my_image3, cv2.COLOR_BGR2GRAY)


image_height, image_width, _ = my_image.shape
image_height2, image_width2, _ = my_image2.shape
image_height3, image_width3 = my_image3.shape

print(image_height3) # 3229
print(image_width3) # 2479


WIDTH = int(1366*0.7)
HEIGHT = int(768*0.7)


SCALE_FACTOR = 0.35
WIDTH3 = int(image_width3*SCALE_FACTOR)
HEIGHT3 = int(image_height3*SCALE_FACTOR)

my_image = cv2.resize(my_image, (WIDTH, HEIGHT)) 
my_image2 = cv2.resize(my_image2, (WIDTH, HEIGHT))
my_image3 = cv2.resize(my_image3, (WIDTH3, HEIGHT3))
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)


# x = pytesseract.image_to_string(my_image, lang="eng")
# x2 = pytesseract.image_to_string(my_image2, lang="eng")
# x3 = pytesseract.image_to_string(my_image3, lang="eng")
# print(x)
# print(x2)

# y = pytesseract.image_to_boxes(my_image, lang="eng")
# y2 = pytesseract.image_to_boxes(my_image2, lang="eng")
y3 = pytesseract.image_to_boxes(my_image3, lang="eng")
# print(y)
# print(y2)

# z = pytesseract.image_to_data(my_image, lang="eng")
# z2 = pytesseract.image_to_data(my_image2, lang="eng")
z3 = pytesseract.image_to_data(my_image3, lang="eng")
# print(z2[0])



# for box in y.splitlines():
#     box = box.split()
#     x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(my_image, (x,image_height-y), (w,image_height-h), (0,0,255), 1)


# for box in y2.splitlines():
#     box = box.split()
#     x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(my_image2, (x,image_height2-y), (w,image_height2-h), (0,0,255), 1)
    # cv2.putText(my_image2, box[0], (x,image_height2-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)


# for count,box in enumerate(z2.splitlines()):
#     if count == 0 :
#         continue
    
#     box = box.split()

#     if len(box) == 12:
#         x,y,w,h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
#         cv2.rectangle(my_image2, (x,y), (x+w,y+h), (0,0,255), 1)
#         # cv2.putText(my_image2, box[11], (x,y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255))

#         # Printing the words that are detected
#         if box[11] != "":
#             print(box[11])

# print(y3)

boxes = [box.split() for box in y3.splitlines()]
# print(boxes)

# print(y3.splitlines().split())
boxes.sort(key=lambda elem: elem[0])

for box in boxes:
    print(box)


# print(boxes, end="\n")
for box in y3.splitlines():
    box = box.split()
    # print(box)
    x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(my_image3, (x,HEIGHT3-y), (w,HEIGHT3-h), (0,0,255), 1)

    # cv2.rectangle(my_image3, (x,image_height3-y), (w,image_height3-h), (0,0,255), 1)
    # cv2.rectangle(my_image3, (image_height3-y,x), (image_height3-h,w), (0,0,255), 1)
    # cv2.rectangle(my_image3, (L,HEIGHT3-T), (R,HEIGHT3-B), (0,0,255), 3)
    # cv2.rectangle(my_image3, (x,y), (w,h), (0,0,255), 1)
    # cv2.putText(my_image3, box[0], (x,image_height3-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)

cv2.rectangle(my_image3, (50,50), (100,100), (255,0,0), 3)
# cv2.rectangle(my_image3, (0,HEIGHT3-105), (50,HEIGHT3-119), (0,255,0), 3)

# for count,box in enumerate(z3.splitlines()):
#     if count == 0 :
#         continue
    
#     box = box.split()

#     if len(box) == 12:
#         x,y,w,h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
#         cv2.rectangle(my_image3, (x,y), (x+w,y+h), (0,0,255), 1)
#         # cv2.putText(my_image2, box[11], (x,y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255))

#         # Printing the words that are detected
#         if box[11] != "":
#             print(box[11])




# cv2.imshow("output", my_image)
# cv2.imshow("output2", my_image2)
cv2.imshow("output3", my_image3)
cv2.waitKey(0)





# extracted_text = pytesseract.image_to_string(my_image, lang="eng")

# with open("boom2.txt", mode='a') as newfile:
#     newfile.write(extracted_text)

print("Goodnight world")
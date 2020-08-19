print("Hello world")

# from PIL import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

my_image = cv2.imread("sample_student.jpg")
my_image2 = cv2.imread("sample_student_no_back_sheet.jpg")

my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)



WIDTH = int(1366*0.7)
HEIGHT = int(768*0.7)
my_image = cv2.resize(my_image, (WIDTH, HEIGHT)) 
my_image2 = cv2.resize(my_image2, (WIDTH, HEIGHT))
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)


# x = pytesseract.image_to_string(my_image, lang="eng")
# x2 = pytesseract.image_to_string(my_image2, lang="eng")
# print(x)
# print(x2)

# y = pytesseract.image_to_boxes(my_image, lang="eng")
# y2 = pytesseract.image_to_boxes(my_image2, lang="eng")
# print(y)
# print(y2)

# z = pytesseract.image_to_data(my_image, lang="eng")
z2 = pytesseract.image_to_data(my_image2, lang="eng")
# print(z2[0])

image_height, image_width, _ = my_image.shape
image_height2, image_width2, _ = my_image2.shape

# for box in y.splitlines():
#     box = box.split()
#     x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(my_image, (x,image_height-y), (w,image_height-h), (0,0,255), 1)


# for box in y2.splitlines():
#     box = box.split()
#     x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(my_image2, (x,image_height2-y), (w,image_height2-h), (0,0,255), 1)
#     cv2.putText(my_image2, box[0], (x,image_height2-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)


for count,box in enumerate(z2.splitlines()):
    if count == 0 :
        continue
    
    box = box.split()

    if len(box) == 12:
        x,y,w,h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
        cv2.rectangle(my_image2, (x,y), (x+w,y+h), (0,0,255), 1)
        # cv2.putText(my_image2, box[11], (x,y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255))

        # Printing the words that are detected
        if box[11] != "":
            print(box[11])




# cv2.imshow("output", my_image)
cv2.imshow("output2", my_image2)
cv2.waitKey(0)





# extracted_text = pytesseract.image_to_string(my_image, lang="eng")

# with open("boom2.txt", mode='a') as newfile:
#     newfile.write(extracted_text)

# print("Goodnight world")
from sklearn.model_selection import train_test_split, GridSearchCV
import os
import numpy as np
import cv2

LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
SMALL_LETTERS = [x.lower() for x in LETTERS]
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']
SYMBOLS = ['@','$','&',',','period','-']


for letter in LETTERS:

    with open(fr".\Uppercase\{letter}\{letter}.txt", "w") as newfile:

        for i in range(1,36):
            my_image = cv2.imread(fr"C:\Users\AJ\Desktop\Computer_Vision_Finance_OCR\Uppercase\{letter}\{letter}_{i}.jpg")

            # gray_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)

            # print(my_image.dtype) # uint8
            # print(my_image.shape) # (73, 73, 3)

            # cv2.imshow("original", my_image)
            # cv2.imshow("grayscale", gray_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()


            data = np.array(my_image)
            data_list = data.tolist()
            # print(data_list[0])
            # print(data[0][0:3])
            # print(data[0].shape) # 73x3 (Obviously! )
            # print(data.shape) # (73, 73, 3)

            newfile.write(f"{letter}::"+str(data_list)+"\n")



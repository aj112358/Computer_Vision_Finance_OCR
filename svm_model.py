# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.svm import SVC
# from sklearn.metrics import classification_report, confusion_matrix
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import image

# Import character data (and clean???)


my_image = cv2.imread(r"C:\Users\AJ\Desktop\Computer_Vision_Finance_OCR\Uppercase\A\A_1.jpg")

gray_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)

# print(my_image.dtype) # uint8
# print(my_image.shape) # (73, 73, 3)

# cv2.imshow("original", my_image)
# cv2.imshow("grayscale", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(my_image)
# plt.show()


data = np.asarray(gray_image)
print(data)
# print(data[0][0:3])
# print(data[0].shape) # 73x3 (Obviously! )
# print(data.shape) # (73, 73, 3)

# np.savetxt("img_to_array_test2.txt", X=data)
# np.save("img_to_array_test2.txt", arr=data)

with open("img_to_array_test.txt", "w") as newfile:
    newfile.write("A::"+str(data))
    # for row in range(73):
    #     newfile.writelines(str(data[row])+",")




# CWD = os.getcwd()
# print(CWD)
# PATH = r"Uppercase/A"
# raw_data = f"{PATH}/A_1.jpg"



# print("Path at terminal when executing this file")
# print(os.getcwd() + "\n")

# print("This file path, relative to os.getcwd()")
# print(__file__ + "\n")

# print("This file full path (following symlinks)")
# full_path = os.path.realpath(__file__)
# print(full_path + "\n")

# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")

# print("This file directory only")
# print(os.path.dirname(full_path))


# convert_to_numerical


# Split the data
# X
# y


# Create & fit the model 



# Evaluate the model (with training data)




# Create "validation data" to do final tests




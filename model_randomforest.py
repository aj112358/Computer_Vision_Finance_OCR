#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import cv2
import ast


# In[2]:


from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix


# In[3]:


from sklearn.tree import DecisionTreeClassifier


# In[4]:


LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
SMALL_LETTERS = [x.lower() for x in LETTERS]
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']
SYMBOLS = ['@','$','&',',','period','-']


# In[47]:


# Import the data
#### This cell takes ~90s to execute (for color data)
#### This cell takes ~20s to execute (for gray data)

X = []
y = []

for letter in LETTERS:

    with open(fr".\Uppercase\{letter}\{letter}.txt", "r") as newfile:
        
        for i in range(70):
            target, data = newfile.readline().split("::")
            data = ast.literal_eval(data)
            y.append(target)
            X.append(data)


# In[53]:


# print(y[0]) # A
# print(np.array(y).shape) # (910,)
# print(np.array(y).ndim) # 1
print(np.array(X).shape) # (910, 73, 73, 3)
# print(np.array(X).ndim) # 4
# print(type(X[0])) $ <class 'list'>
# # print(X[0])


# In[56]:


# Trying to reshape the X-input data
X = np.array(X)
y = np.array(y)

X = X.reshape((1820,-1))


# In[57]:


# Split the data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[9]:


# print(y_test)
print(X_train.shape)
print(X_test[0])


# In[10]:


# Instantiate model object

decision_tree_model = DecisionTreeClassifier()


# In[58]:


# Fit the model with training data

decision_tree_model.fit(X_train, y_train)


# In[12]:


# Evaluate the model (with testing data)

predictions = decision_tree_model.predict(X_test)


# In[13]:


# Evaluate the model
#### Need to assess predictions vs. y_test

classification_report(y_test, predictions)


# In[14]:


confusion_matrix(y_test, predictions)


# In[15]:


# Not sure how to interpret the above two reports...so we will instead use plots!

import matplotlib.pyplot as plt
import seaborn as sns
# get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams["figure.dpi"] = 150


# In[16]:


sns.heatmap(confusion_matrix(y_test,predictions))


# In[17]:


fig, axes = plt.subplots(1,1)

# axes.plot(y_test, predictions)

#### NOTE: The lines below only change the tick LABELS!!! They don't affect the data points!
# axes.set_xticklabels(LETTERS)
# axes.set_yticklabels(LETTERS)

ax = sns.scatterplot(x = y_test,
                y = predictions)
# ax.set_xlim(LETTERS)


# In[18]:


# y_test


# In[19]:


# predictions


# In[20]:


# Manually determine percent accuracy
count=0
for i in range(len(y_test)):
    if y_test[i] == predictions[i]:
        count+=1

percent = count/len(y_test) * 100
print("Number of predictions made: ", len(y_test))
print("Number correct: ", count)
print("Percentage correct: ", round(percent, 2), "%")


# Wow, terrible results! We can try to use a random forest model:

# In[21]:


from sklearn.ensemble import RandomForestClassifier


# In[40]:


num_trees=5000 # Default is 100
random_forest_model = RandomForestClassifier(n_estimators=num_trees)


# In[41]:


random_forest_model.fit(X_train,y_train)


# In[42]:


predictions2 = random_forest_model.predict(X_test)


# In[43]:


sns.heatmap(confusion_matrix(y_test,predictions2))


# In[44]:


fig, axes = plt.subplots(1,1)

# axes.plot(y_test, predictions)

#### NOTE: The lines below only change the tick LABELS!!! They don't affect the data points!
# axes.set_xticklabels(LETTERS)
# axes.set_yticklabels(LETTERS)

ax = sns.scatterplot(x = y_test,
                y = predictions2)
# ax.set_xlim(LETTERS)


# In[45]:


# Manually determine percent accuracy
count=0
for i in range(len(y_test)):
    if y_test[i] == predictions2[i]:
        count+=1

percent = count/len(y_test) * 100
print("Number of predictions made: ", len(y_test))
print("Number correct: ", count)
print("Percentage correct: ", round(percent, 2), "%")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install sklearn


# In[3]:


pip install yellowbrick


# In[78]:


from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.datasets.samples_generator import make_blobs

X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

# TODO determine the best k for k-means
model = KMeans()
visualizer = KElbowVisualizer(model, k=(2,12))

visualizer.fit(X)
visualizer.show()

    #The best k determined by the elbow method is 4 based on a range of k from 2 to 12 

# TODO calculate accuracy for best K

model = KMeans(n_clusters=4)
model.fit(X)
ymeans = model.predict(X)

print("Accuracy:")
print(accuracy_score(y_true, ymeans))
print() #Formatting

    #The accuracy fluctuates between ~0% and ~50% 
    #Averaging ~17%-25% on 100 trials

# TODO draw a confusion matrix

print("Confusion Matrix")
print(confusion_matrix(y_true, ymeans))


# In[ ]:





# In[ ]:





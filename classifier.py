# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import support vector classifier
from sklearn.svm import SVC 
import cv2
# import warnings to remove any type of future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# reading csv file and extracting class column to y.
dataf = pd.read_csv("Datasetinfectedhealthy.csv")

# extracting two features
X = dataf.drop(['imgid','fortnum','feature3'], axis=1)
y = X['label']
X = X.drop('label', axis=1)

print "\nTraining dataset:-\n" 
print X


log = pd.read_csv("datasetlog/Datasetunlabelled.csv")

log = log.tail(1)
X_ul = log.drop(['imgid','fortnum','feature3'], axis=1)

print "\nTest dataset:-\n"
print X_ul


X.plot(kind='scatter',x='feature1',y='feature2')
plt.show()

Sum = 0
from sklearn.model_selection import train_test_split  
for n in xrange(4):
	x_train, Xi_test, y_train, yi_test = train_test_split(X, y, test_size=0.52, random_state=60)  
	     
	svclassifier = SVC(kernel='linear')  
	svclassifier.fit(x_train, y_train)  
	pred = svclassifier.predict(X_ul)
	Sum = Sum + pred
	print pred

print "\nprediction:",Sum 

if(Sum < 2):
	print "The leaf is sufficiently healthy!"
else:
	print "The leaf is infected!"

print "\nKeypress on any image window to terminate"

#from sklearn.metrics import classification_report, confusion_matrix  

#print(classification_report(yi_test,y_pred))
#print "\n Average precision percentage: %.2f"  %avg_pred + "%"
cv2.waitKey(0)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# KNN FUNCTIONS
def l2distance(X,Z):
    # BODY REMOVED FOR ACADEMIC INTEGRITY PURPOSES

def findknn(xTr,xTe,k, inp):
    # BODY REMOVED FOR ACADEMIC INTEGRITY PURPOSES
    

def knnclassifier(xTr,yTr,xTe,k, inp):
    # BODY REMOVED FOR ACADEMIC INTEGRITY PURPOSES


# Function to be called
def classify(use):

  # Test point processing
  if use == "user":
    print("Welcome to the Cornell Admissions Simulator! \n\n")
    print("This simulator uses a k-nearest neighbors binary classification machine learning algorithm\n")
    print("\nNow, time to fill out your application!")
    inp = [''] * 6
    inp[0] = input("\nSAT: ")
    inp[1] = input("\nUnweighted GPA (max 4.0): ")
    print("\nFor the following questions, 1 = yes, 0 = no")
    inp[2] = input("\nDo you play a sport: ")
    inp[3] = input("\nDo you volunteer on a monthy basis: ")
    inp[4] = input("\nAre you the head of any clubs or organizations: ")
    inp[5] = input("\nDo you have a unique trait that very few applicants have?: ")
    xTe = [0.0] * 6
    for i in range(len(xTe)):
      xTe[i] = 500.0 * float(inp[i])
      if i == 0:
        xTe[i] /= 500.0
    xTe = np.array(xTe)
    xTe = xTe.reshape((1,6))

  if use == "test":
    test_data = pd.read_csv('test_data.csv')
    xTe = test_data[['SAT', 'GPA', 'Sports', 'Volunteering', 'Leadership', 'Unique_Trait']]
    xTe['GPA'] = xTe['GPA'] * 500.0
    xTe['Sports'] = xTe['Sports'] * 500.0
    xTe['Volunteering'] = xTe['Volunteering'] * 500.0
    xTe['Leadership'] = xTe['Leadership'] * 500.0
    xTe['Unique_Trait'] = xTe['Unique_Trait'] * 500.0
    xTe = xTe.values
    yTe = test_data['Accepted'].values


  # Training data processing
  df = pd.read_csv("training_data.csv")
  xTr = df[['SAT', 'GPA', 'Sports', 'Volunteering', 'Leadership', 'Unique_Trait']].values
  yTr = df['Accepted'].values

  for i in range(len(xTr)):
    for j in range(len(xTr[0])):
      xTr[i][j] = 500.0 * float(xTr[i][j])
      if j == 0:
        xTr[i][j] /= 500.0


  # Run KNN
  preds = knnclassifier(xTr,yTr,xTe,5,inp)


  # Descision
  if use == "user":
    if preds[0] == 1:
        print("\n\nCongratulations!!! Your application resembles many accepted Cornell students\n")
        print("The KNN classifier predicts your application will be: Accepted\n\n\n")
    else:
        print("\n\nUnfortunately, your application matches that of rejected applicants :(\n")
        print("The KNN classifier predicts your application will be: Rejected\n\n\n")
  if use == "test":
    classified = 0
    for i in range(len(preds)):
      if preds[i] == yTe[i]:
        classified += 1

    print("The KNN algorithm has: " + str(100.0 * classified / len(preds)) + "% accuracy on the test data\n\n")

#classify("test")
#classify("user")
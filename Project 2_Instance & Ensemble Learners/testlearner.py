"""
Test a learner.  (c) 2015 Tucker Balch
"""

import LinRegLearner as lrl
import KNNLearner as knn
import BagLearner as bl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

if __name__=="__main__":
    #_______________________________Data Import________________________________
    data = pd.read_csv('Data/simple.csv', header = None)

    # compute how much of the data is training and testing
    train_rows = math.floor(0.6* data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    trainX = data.iloc[:train_rows,0:-1]
    trainY = data.iloc[:train_rows,-1]
    testX = data.iloc[train_rows:,0:-1]
    testY = data.iloc[train_rows:,-1]

    #____________________________Linear Regression_____________________________
    print("\nLinear Regression:")
    # create a learner and train it
    learner = lrl.LinRegLearner() # create a LinRegLearner
    learner.addEvidence(trainX, trainY) # training step

    # evaluate in sample
    predY = learner.query(trainX)       # get the predictions
    rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
    print ("In sample results")
    print ("RMSE: ", rmse)
    c = np.corrcoef(predY, y=trainY)
    print ("corr: ", c[0,1])

    # evaluate out of sample
    predY = learner.query(testX) # get the predictions
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
    print ("Out of sample results")
    print ("RMSE: ", rmse)
    c = np.corrcoef(predY, y=testY)
    print ("corr: ", c[0,1])
    
    #___________________________K-Nearest Neighbors____________________________
    print("\nK-Nearest Neighbors:")
    # create a learner and train it
    learner = knn.KNNLearner(k = 3)
    learner.addEvidence(trainX, trainY) # training step
    
    # evaluate in sample
    predY = learner.query(trainX)       # get the predictions
    rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
    print ("In sample results")
    print ("RMSE: ", rmse)
    c = np.corrcoef(predY, y=trainY)
    print ("corr: ", c[0,1])
    
    # evaluate out of sample
    predY = learner.query(testX) # get the predictions
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
    print ("Out of sample results")
    print ("RMSE: ", rmse)
    c = np.corrcoef(predY, y=testY)
    print ("corr: ", c[0,1])
    
    #_________________________________Bagging__________________________________
    print("\nBagging:")
    # create a learner and train it
    learner = bl.BagLearner(learner = 'KNNLearner', kwargs = {"k":3}, bags = 20, boost = False)
    learner.addEvidence(trainX, trainY) # training step
    
    # evaluate in sample
    predY = learner.query(trainX)       # get the predictions
    rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
    print ("In sample results")
    print ("RMSE: ", rmse)
    c = np.corrcoef(predY, y=trainY)
    print ("corr: ", c[0,1])
    
    # evaluate out of sample
    predY = learner.query(testX) # get the predictions
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
    print ("Out of sample results")
    print ("RMSE: ", rmse)
    c = np.corrcoef(predY, y=testY)
    print ("corr: ", c[0,1])
    
    #learners = []
    #for i in range(0,10):
        #kwargs = {"k":i}
        #learners.append(lrl.LinRegLearner(**kwargs))

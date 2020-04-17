import numpy as np
import pandas as pd

class KNNLearner(object):
    
    def __init__(self, k = 3):
        self.k = k
    
    def addEvidence(self, dataX, dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        self.data = np.ones([dataX.shape[0],dataX.shape[1]+1])
        self.data[:,:-1] = dataX
        self.data[:,-1] = dataY
    
    def getKNeighbors(self, testRow):
        distances = list()
        for trainRow in self.data[:,:-1]:
#            print(trainRow, testRow)
            dist = (((testRow - trainRow) ** 2).sum()) ** 0.5
            distances.append((trainRow, dist))
        distances.sort(key = lambda tup: tup[1])
#        print(distances)
        neighbors = list()
        for i in range(self.k):
            neighbors.append(distances[i][0])
#            print(distances[i][0])
#        print(neighbors)
        return np.array(neighbors)
        
    def query(self, dataX):
        """
        @summary: Estimate a set of test points given the model we built.
        @param dataX: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        predY = []
        for index, testRow in dataX.iterrows():
            neighbors = self.getKNeighbors(testRow)
            neighborValues = neighbors[-1]
            predRow = neighborValues.mean()
            predY.append(predRow)
        return np.array(predY)

if __name__=="__main__":
    print ("the secret clue is 'zzyzx'")
            
        
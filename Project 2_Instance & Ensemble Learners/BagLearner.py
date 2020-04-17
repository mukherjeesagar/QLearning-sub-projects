import math
import numpy as np
import pandas as pd
from importlib.machinery import SourceFileLoader
from random import randrange

class BagLearner(object):
    
    def __init__(self, learner, kwargs, bags = 20, boost = False):
        self.learner = learner
        self.bags = bags
        self.kwargs = kwargs
        self.foo = SourceFileLoader(self.learner,self.learner+'.py').load_module()
        exec("self.learnerObj = self.foo."+self.learner+"(**self.kwargs)")
    
    def addEvidence(self, dataX, dataY):
        self.data = np.ones([dataX.shape[0],dataX.shape[1]+1])
        self.data[:,:-1] = dataX
        self.data[:,-1] = dataY
        self.learnerObj.addEvidence(dataX, dataY)
    
    def subSample(self, data):
#        return data[:,:-1], data[:,-1]
        pdData = pd.DataFrame(self.data)
        sample = pd.DataFrame.sample(pdData, n = int(0.6*len(self.data)), replace=True)
        return sample.iloc[:,:-1], sample.iloc[:,-1]
        
    def query(self, dataX):
        predList = []
        for i in range(self.bags):
            foo = SourceFileLoader(self.learner,self.learner+'.py').load_module()
            exec("self.learnerObj = foo."+self.learner+"(**self.kwargs)")
            sample = self.subSample(self.data)
            self.learnerObj.addEvidence(sample[0], sample[1])
            predY = self.learnerObj.query(dataX)
            predList.append(predY)
        return np.mean(np.array(predList), axis=0)
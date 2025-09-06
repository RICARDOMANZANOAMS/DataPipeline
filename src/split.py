from abc import ABC,abstractmethod
from sklearn.model_selection import train_test_split,KFold, LeaveOneOut
class splitStrategy(ABC):
    '''
    Class strategy for split datasets
    '''
    @abstractmethod
    def splitDataset(self,df):
        pass
    
class dataSplitStrategy(splitStrategy):
    '''
    Child class that implements split strategy only in two subdatasets
    '''
    def splitDataset(self,df,testSize=0.2):
        train,test=train_test_split(df,test_size=testSize) 
        return [train, test]
    
class kFoldStrategy(splitStrategy):
    '''
    Child class that implements k fold. 
    To illustrate, if k=4, it will divide the dataset in 4, it will train with 3 parts and test with one
    '''
    def splitDataset(self,df,kFolds):
        kf = KFold(n_splits=kFolds)
        arraySplits=kf.split(df)
        return list(arraySplits)
    
class leaveOneOutStrategy(splitStrategy):
    '''
    Child class that implements leave one out cross validation
    This method leaves only one sample to test while it trains with all the rest.
    
    '''
    def splitDataset(self, df):
        loo = LeaveOneOut()
        # Returns list of (train_idx, test_idx) tuples
        return list(loo.split(df))
    
class factorySplit:
    @staticmethod
    def selectSplit(splitMethod):
        if splitMethod=="split":
            return dataSplitStrategy()
        elif splitMethod=="kFold":
            return kFoldStrategy()
        elif splitMethod=="LOOCV":
            return leaveOneOutStrategy()
        else:
            return "Split Method not implemented "
# import pandas as pd
# import numpy as np
# path='./data/DDoS-ACK_Fragmentation.csv'
# df=pd.read_csv(path)
# splitMethod=factorySplit.selectSplit("split")
# dataset=splitMethod.splitDataset(df,0.2)
# print(dataset)
# splitMethod=factorySplit.selectSplit("LOOCV")
# dataset=splitMethod.splitDataset(df)
# print(dataset)
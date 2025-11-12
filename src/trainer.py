from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import numpy as np
from Logger import Logger
class trainer:
    '''
    This class is the general class to train a classification or regression problem
    '''
    def __init__(self,df,featureNames,labelName):
        self.df=df
        self.featureNames=featureNames
        self.labelName=labelName
        self.splitArray=[]
        self.model=None
        self.logger=Logger().get_logger()
    
    @Logger.log_exceptions(lambda self: self.logger)  
    def splitDataset(self,splitMethod,params):
        '''
        This method implements the class split which is used to split a dataset in different strategies
        Args:
            splitMethod: it is necessary to select an split method among "split", "kFold", "LOOCV" 
            params: it is a dictionary which can take many values depending of the hiperparameters passed 

        '''
        from split import factorySplit
        objFactorySplit=factorySplit.selectSplit(splitMethod)  #Select the split method
        self.splitArray=objFactorySplit.splitDataset(self.df,**params) #Split the dataset
    
    @Logger.log_exceptions(lambda self: self.logger) 
    def trainTest(self):
        '''
        This method implements the training and testinting of the model in the split dataset 
        '''        
        for train,test in self.splitArray:
            modelTrain=self.train(train)
            modelTest=self.test(test)

    @Logger.log_exceptions(lambda self: self.logger) 
    def train(self,trainDataset):
        '''
        This method implements the training of the model
        '''
        self.model.fit(trainDataset[self.featureNames],trainDataset[self.labelName])

    @Logger.log_exceptions(lambda self: self.logger)     
    def test(self,testDataset):
        '''
        This method implements the testing of the model and calculates confusion matrix, classification report,
        and accuracy 
        '''
        from sklearn.metrics import f1_score
        predicted=self.model.predict(testDataset[self.featureNames])
        groundTruth=testDataset[self.labelName]
        return np.array(predicted), np.array(groundTruth)


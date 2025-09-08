from trainer import trainer
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

class classificationTrainer(trainer):
    '''
    This class extend the trainer class to classification problems specifically
    '''
    def __init__(self,df, featureNames,labelName):
        super().__init__(df,featureNames,labelName)
    
    def selectAlg(self,algName,**params):
        '''
        This method selects the algorithm to train and test
        
        '''
        if algName=="rf":
            self.model=RandomForestClassifier(**params)
        elif algName=="GBC":
            self.model=GradientBoostingClassifier(**params)
        elif algName=="ETC":
             self.model=ExtraTreesClassifier(**params)
        elif algName=="svm":
            self.model=SVC(**params)
        elif algName=="logistic":
             self.model=LogisticRegression(**params)



import pandas as pd
import numpy as np
path='./data/DDoS-ACK_Fragmentation.csv'
df=pd.read_csv(path)
labelName='Label_34_class_encoded'
featuresNames=['Header_Length','Protocol Type']
objClassificationTrainer=classificationTrainer(df,featuresNames,labelName)
objClassificationTrainer.selectAlg("rf")
objClassificationTrainer.splitDataset("split", {"testSize": 0.2})
objClassificationTrainer.trainTest()

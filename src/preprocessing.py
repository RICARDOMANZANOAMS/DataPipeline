class preprocessing:
    '''
    Class that includes all the class for preprocessing such as dropDuplicates and imputeValues
    '''
    def __init__(self,df):
        self.df=df  

    def dropDuplicates(self):
        '''
        Method to drop duplicates in the dataset
        '''
        self.df=self.df.drop_duplciates()
                
    def imputeValue(self,imputeMethod,featureName,replacementValue):
        '''
        Method to impute values in an specific feature in the dataset
        '''
        from imputer import factoryImputer
        objFactoryImputer=factoryImputer.selectImputeMethod(imputeMethod)
        objFactoryImputer.impute(self.df,featureName, replacementValue=None)
        

    
    
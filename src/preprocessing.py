from Logger import Logger
class preprocessing:
    '''
    Class that includes all the class for preprocessing such as dropDuplicates and imputeValues
    '''
    def __init__(self,df):
        self.df=df  
        self.logger=Logger().get_logger()

    @Logger.log_exceptions(lambda self: self.logger)
    def dropDuplicates(self):
        '''
        Method to drop duplicates in the dataset
        '''       
        df=self.df.drop_duplicates()
        return df
        
    @Logger.log_exceptions(lambda self: self.logger)            
    def imputeValue(self,imputeMethod,featureName,replacementValue):
        '''
        Method to impute values in an specific feature in the dataset
        '''
        from imputer import factoryImputer
        objFactoryImputer=factoryImputer.selectImputeMethod(imputeMethod)
        df=objFactoryImputer.impute(self.df,featureName, replacementValue=None)
        return df

    
    
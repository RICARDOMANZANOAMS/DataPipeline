from abc import ABC, abstractmethod
import pandas as pd
from Logger import Logger
import logging
class ImputerStrategy(ABC):
    '''
    This class is the abstract method to create imputers which can be mean, median, None
    Args:
        df: pandas dataframe to process
        featureName: name of the feature to impute in the df

    '''
    def __init__(self):
        self.logger=Logger().get_logger()

    @abstractmethod
    def impute(self, df, featureName, replacementValue=None):
        pass
        

class MeanImputer(ImputerStrategy):
    '''
    Child class of imputerStrategy that replaces none values with the mean of the feature
    
    '''
    @Logger.log_exceptions(lambda self: self.logger)
    def impute(self, df, featureName, replacementValue=None):
        featureCol = df[featureName]        #Select the feature column in the dataset to impute
    
        if pd.api.types.is_numeric_dtype(featureCol):   #Verify if the column is numeric
            mean_val = featureCol.mean()                #Find the mean of the column 
            df[featureName] = featureCol.fillna(mean_val)   #Fill null values with the mean
            self.logger.info(f"Imputed column {featureName} with mean")
            return df
        else:
            raise TypeError(f"Feature '{featureName}' is not numeric, cannot impute with mean.") #Raise error if feature not numeric
    

class MedianImputer(ImputerStrategy):
    '''
    Child class of imputerStrategy that replaces null values with the median
    '''
    @Logger.log_exceptions(lambda self: self.logger)
    def impute(self, df, featureName, replacementValue=None):        
        featureCol = df[featureName] #Select the feature column in the dataset to impute
        if pd.api.types.is_numeric_dtype(featureCol): #Verify if the column is numeric
            median_val = featureCol.median()           #Find the mean of the column 
            df[featureName] = featureCol.fillna(median_val) #Fill null values with the median
            self.logger.info(f"Imputed column {featureName} with median ")
        else:
            raise TypeError(f"Feature '{featureName}' is not numeric, cannot impute with median.") #Raise error if feature not numeric
        return df
       

class ValueNullImputer(ImputerStrategy):
    '''
    Child class of imputerStrategy that replaces null values with a value pass to impute
    '''
    @Logger.log_exceptions(lambda self: self.logger)
    def impute(self, df, featureName, replacementValue=None):
        if replacementValue is None:   #Verify the value pass to the class if it is not null. It should have a value
            raise ValueError("You must provide a replacementValue for valueImputer.")
        
        df[featureName] = df[featureName].fillna(replacementValue)
        self.logger.info(f"Imputed columng {featureName} with value {replacementValue}")
        return df
    
class ValueToNullImputer(ImputerStrategy):
    '''
    Child class of imputerStrategy that replaces a value chosen by null
    '''
    @Logger.log_exceptions(lambda self: self.logger)
    def impute(self, df, featureName, replacementValue):
        import numpy as np
        featureCol = df[featureName]
        df[featureName] = featureCol.replace(replacementValue, np.nan)
        self.logger.info(f"Replace value {replacementValue} in column {featureName} with Null")
        return df
    
    
class FactoryImputer:
    '''
    Factory class to implement all the classes in a modular way
    '''
    @staticmethod
    def selectImputeMethod(imputeMethod):
        
        # try:
            if imputeMethod=="mean":
                return MeanImputer()
            elif imputeMethod=="median":
                return MedianImputer()
            elif imputeMethod=="value":
                return ValueNullImputer()
            elif imputeMethod=="valueToNull":
                return ValueToNullImputer()
            else:
                raise
        # except Exception as e:
        #     logger.error("Error selecting impute method ", exc_info=True)
        #     return None
        
import pandas as pd
import numpy as np


logger=Logger()
logger.create_handler_with_level_and_format("info", "%(asctime)s - %(levelname)s - %(message)s","file",filename="app.log")
log = logger.logger
log.setLevel(logging.DEBUG)

path='./data/DDoS-ACK_Fragmentation.csv'
df=pd.read_csv(path)
featureName="Rate"
replacementValue=np.inf
imputer=FactoryImputer.selectImputeMethod("valueToNull")
df = imputer.impute(df, featureName, replacementValue=np.inf)
print(df)
# replacementValue=np.inf
# objfactoryImputer=factoryImputer.selectImputeMethod("valueToNull")
# df_new=objfactoryImputer.impute(df,featureName,replacementValue)



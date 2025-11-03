from abc import ABC, abstractmethod
import pandas as pd
class imputerStrategy(ABC):
    '''
    This class is the abstract method to create imputers which can be mean, median, None
    Args:
        df: pandas dataframe to process
        featureName: name of the feature to impute in the df

    '''
    def __init__(self,logger):
        self.logger=logger
    @abstractmethod
    def impute(self, df, featureName, replacementValue=None):
        pass
        

class meanImputer(imputerStrategy):
    '''
    Child class of imputerStrategy that replaces none values with the mean of the feature
    
    '''
    def impute(self, df, featureName, replacementValue=None):
        featureCol = df[featureName]        #Select the feature column in the dataset to impute
        try:
            if pd.api.types.is_numeric_dtype(featureCol):   #Verify if the column is numeric
                mean_val = featureCol.mean()                #Find the mean of the column 
                df[featureName] = featureCol.fillna(mean_val)   #Fill null values with the mean
                self.logger.info(f"Imputed column {featureName} with mean")
                return df
            else:
                raise TypeError(f"Feature '{featureName}' is not numeric, cannot impute with mean.") #Raise error if feature not numeric
        except Exception as e:
               self.logger.error("Error in meanImputer", exc_info=True)
               return None


class medianImputer(imputerStrategy):
    '''
    Child class of imputerStrategy that replaces null values with the median
    '''
    def impute(self, df, featureName, replacementValue=None):
        try:
            featureCol = df[featureName] #Select the feature column in the dataset to impute
            if pd.api.types.is_numeric_dtype(featureCol): #Verify if the column is numeric
                median_val = featureCol.median()           #Find the mean of the column 
                df[featureName] = featureCol.fillna(median_val) #Fill null values with the median
                self.logger.info(f"Imputed column {featureName} with median ")
            else:
                raise TypeError(f"Feature '{featureName}' is not numeric, cannot impute with median.") #Raise error if feature not numeric
            return df
        except Exception as e:
            self.logger.error(f"Error in medianImputer", exc_info=True)
            return None

class valueNullImputer(imputerStrategy):
    '''
    Child class of imputerStrategy that replaces null values with a value pass to impute
    '''
    def impute(self, df, featureName, replacementValue=None):
        try:
            if replacementValue is None:   #Verify the value pass to the class if it is not null. It should have a value
                raise ValueError("You must provide a replacementValue for valueImputer.")
            
            df[featureName] = df[featureName].fillna(replacementValue)
            self.logger.info("Imputed columng {featureName} with value {replacementValue}")
            return df
        except:
            self.logger.error("Error in valueNullImputer", exc_info=True)
            return None
class valueToNullImputer(imputerStrategy):
    '''
    Child class of imputerStrategy that replaces a value chosen by null
    '''
    def impute(self, df, featureName, replacementValue):
        try:
            import numpy as np
            featureCol = df[featureName]
            df[featureName] = featureCol.replace(replacementValue, np.nan)
            self.logger.info("Replace value {replacementValue} in column {featureName} with Null")
            return df
        except Exception as e:
            self.logger.error("Error in valueToNullImputer", exc_info=True)

    
class factoryImputer:
    '''
    Factory class to implement all the classes in a modular way
    '''
    @staticmethod
    def selectImputeMethod(imputeMethod):
        logger = logger()  # Get the singleton logger
        try:
            if imputeMethod=="mean":
                return meanImputer()
            elif imputeMethod=="median":
                return medianImputer()
            elif imputeMethod=="value":
                return valueNullImputer()
            elif imputeMethod=="valueToNull":
                return valueToNullImputer()
            else:
                raise
        except Exception as e:
            logger.error("Error selecting impute method ", exc_info=True)
            return None
        
# import pandas as pd
# import numpy as np
# path='./data/DDoS-ACK_Fragmentation.csv'
# df=pd.read_csv(path)
# featureName="Rate"
# replacementValue=np.inf
# objfactoryImputer=factoryImputer.selectImputeMethod("valueToNull")
# df_new=objfactoryImputer.impute(df,featureName,replacementValue)



from abc import ABC, abstractmethod
import pandas as pd

class imputerStrategy(ABC):
    '''
    This class is the abstract method to create imputers which can be mean, median, None
    Args:
        df: pandas dataframe to process
        featureName: name of the feature to impute in the df

    '''
    @abstractmethod
    def impute(self, df, featureName, replacementValue=None):
        pass

class meanImputer(imputerStrategy):
    '''
    Child class of imputerStrategy that replaces none values with the mean of the feature
    
    '''
    def impute(self, df, featureName, replacementValue=None):
        featureCol = df[featureName]        #Select the feature column in the dataset to impute
        if pd.api.types.is_numeric_dtype(featureCol):   #Verify if the column is numeric
            mean_val = featureCol.mean()                #Find the mean of the column 
            df[featureName] = featureCol.fillna(mean_val)   #Fill null values with the mean
        else:
            raise TypeError(f"Feature '{featureName}' is not numeric, cannot impute with mean.") #Raise error if feature not numeric
        return df

class medianImputer(imputerStrategy):
    '''
    Child class of imputerStrategy that replaces null values with the median
    '''
    def impute(self, df, featureName, replacementValue=None):

        featureCol = df[featureName] #Select the feature column in the dataset to impute
        if pd.api.types.is_numeric_dtype(featureCol): #Verify if the column is numeric
            median_val = featureCol.median()           #Find the mean of the column 
            df[featureName] = featureCol.fillna(median_val) #Fill null values with the median
        else:
            raise TypeError(f"Feature '{featureName}' is not numeric, cannot impute with median.") #Raise error if feature not numeric
        return df

class valueImputer(imputerStrategy):
    '''
    Child class of imputerStrategy that replaces null values with a value pass to impute
    '''
    def impute(self, df, featureName, replacementValue=None):
        if replacementValue is None:   #Verify the value pass to the class if it is not null. It should have a value
            raise ValueError("You must provide a replacementValue for valueImputer.")
        
        df[featureName] = df[featureName].fillna(replacementValue)
        return df

class factoryImputer:
    '''
    Factory class to implement all the classes in a modular way
    '''
    @staticmethod
    def selectImputeMethod(imputeMethod):
        if imputeMethod=="mean":
            return meanImputer()
        elif imputeMethod=="median":
            return medianImputer()
        elif imputeMethod=="value":
            return valueImputer()
        else:
            return "No imputation method"

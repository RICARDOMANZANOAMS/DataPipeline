from abc import ABC, abstractmethod
import pandas as pd

class imputerStrategy(ABC):
    @abstractmethod
    def impute(self, df, featureName, replacementValue=None):
        pass

class meanImputer(imputerStrategy):
    def impute(self, df, featureName, replacementValue=None):
        featureCol = df[featureName]
        if pd.api.types.is_numeric_dtype(featureCol):
            mean_val = featureCol.mean()
            df[featureName] = featureCol.fillna(mean_val)
        else:
            raise TypeError(f"Feature '{featureName}' is not numeric, cannot impute with mean.")
        return df

class medianImputer(imputerStrategy):
    def impute(self, df, featureName, replacementValue=None):
        featureCol = df[featureName]
        if pd.api.types.is_numeric_dtype(featureCol):
            median_val = featureCol.median()
            df[featureName] = featureCol.fillna(median_val)
        else:
            raise TypeError(f"Feature '{featureName}' is not numeric, cannot impute with median.")
        return df

class valueImputer(imputerStrategy):
    def impute(self, df, featureName, replacementValue=None):
        if replacementValue is None:
            raise ValueError("You must provide a replacementValue for valueImputer.")
        
        df[featureName] = df[featureName].fillna(replacementValue)
        return df

class factoryImputer:
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

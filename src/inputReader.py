from abc import ABC, abstractmethod
import pandas as pd

class readerStrategy(ABC):
    @abstractmethod
    def readInput(self,path):
        pass

class csvReader(readerStrategy):
    def readInput(self,path):
        df=pd.read_csv(path)  
        return df
    
class jsonReader(readerStrategy):
    def readInput(self, path):
        df=pd.read_json(path)
        return df
    
class factoryReader:
    @staticmethod
    def selectInput(input):
        if input=="csv":
            return csvReader()
        elif input=="json":
            return jsonReader()
        else:
            return "error"
        
# factoryObj=factoryReader.selectInput("csv")
# path="C:/RICARDO/personal/DataPipeline/data/DDoS-ACK_Fragmentation.csv"
# df=factoryObj.readInput(path)
# print(df) 
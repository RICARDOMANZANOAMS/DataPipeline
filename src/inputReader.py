from abc import ABC, abstractmethod
import pandas as pd
from Logger import Logger
import logging
class readerStrategy(ABC):
    def __init__(self):
        self.logger=Logger().get_logger()

    @abstractmethod
    def readInput(self,path):
        pass

class csvReader(readerStrategy):
    @Logger.log_exceptions(lambda self: self.logger)
    def readInput(self,path):        
        df=pd.read_csv(path)  
        self.logger.info("Read csv file")
        return df
        
    
class jsonReader(readerStrategy):
    @Logger.log_exceptions(lambda self: self.logger)
    def readInput(self, path):
        df=pd.read_json(path)
        self.logger.info("Read json file")
        return df
    

class csvReaderFolder(readerStrategy):
    @Logger.log_exceptions(lambda self: self.logger)
    def readInput(self,path):
        import glob
              
        pathcsv=path+"/*.csv"
        paths=glob.glob(pathcsv)
        dfs=[]
        for path in paths:
            dfs.append(pd.read_csv(path))
        df=pd.concat(dfs)
        self.logger.info("Read directory with csv files")
        return df
       

class jpgReader(readerStrategy):
    @Logger.log_exceptions(lambda self: self.logger)
    def readInput(self,path):
        from PIL import Image
        import numpy as np
        img = Image.open(path)  
        img_gray = img.convert('L')         
        img_np = np.array(img_gray)        
        df = pd.DataFrame(img_np )
        return df


class shpReader(readerStrategy):  
    @Logger.log_exceptions(lambda self: self.logger)  
    def readInput(self, path):
        import geopandas as gpd
        gdf = gpd.read_file(path)
        return gdf
        

class lasReader(readerStrategy):
    @Logger.log_exceptions(lambda self: self.logger)
    def readInput(self, path):
        import laspy
        las = laspy.read(path)
        data = {"x": las.x, "y": las.y, "z": las.z}
        attrs = ["intensity", "classification", "return_number", 
                 "number_of_returns", "scan_angle", "user_data"]
        for attr in attrs:
            if hasattr(las, attr):
                data[attr] = getattr(las, attr)
        return pd.DataFrame(data)
        

class factoryReader:
    @staticmethod
    def selectInput(input):
        try:
            if input=="csv":
                return csvReader()
            elif input=="json":
                return jsonReader()
            else:
                return "error"
        except Exception as e:
            logger.error("Error choosing input")            
            return None
        
    


logger=Logger()
logger.create_handler_with_level_and_format("info", "%(asctime)s - %(levelname)s - %(message)s","file",filename="app.log")
log = logger.logger
log.setLevel(logging.DEBUG)

factoryObj=factoryReader.selectInput("csv")
path="C:/RICARDO/personal/DataPipeline/data/DDoS-ACK_Fragmentation.csv"
df=factoryObj.readInput(path)
print(df) 
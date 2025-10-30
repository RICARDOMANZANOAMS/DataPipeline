from abc import ABC, abstractmethod
import pandas as pd
from logger import logger
class readerStrategy(ABC):
    def __init__(self):
        self.logger=logger()

    @abstractmethod
    def readInput(self,path):
        pass

class csvReader(readerStrategy):
    def readInput(self,path):
        try:
            df=pd.read_csv(path)  
            self.logger.info("Read csv file")
            return df
        except Exception as e:
            self.logger.error("Error reading csv file")
            return None
    
class jsonReader(readerStrategy):
    def readInput(self, path):
        try:
            df=pd.read_json(path)
            self.logger.info("Read json file")
            return df
        except Exception as e: 
            self.logger.error("Error reading json file")
            return None

class csvReaderFolder(readerStrategy):
    def readInput(self,path):
        import glob
        try:        
            pathcsv=path+"/*.csv"
            paths=glob.glob(pathcsv)
            dfs=[]
            for path in paths:
                dfs.append(pd.read_csv(path))
            df=pd.concat(dfs)
            self.logger.info("Read directory with csv files")
            return df
        except Exception as e:
            self.logger.error("Error reading directory with csv files")
            return None

class jpgReader(readerStrategy):
    
    def readInput(self,path):
        from PIL import Image
        import numpy as np
        img = Image.open(path)  
        img_gray = img.convert('L')         
        img_np = np.array(img_gray)        
        df = pd.DataFrame(img_np )
        return df


class shpReader(readerStrategy):    
    def readInput(self, path):
        import geopandas as gpd
        gdf = gpd.read_file(path)
        return gdf
        

class lasReader(readerStrategy):
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
        logger=logger()
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
        
    
        
# factoryObj=factoryReader.selectInput("csv")
# path="C:/RICARDO/personal/DataPipeline/data/DDoS-ACK_Fragmentation.csv"
# df=factoryObj.readInput(path)
# print(df) 
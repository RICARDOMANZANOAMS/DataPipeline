import os
import logging
import sys
class Logger:
    def __init__(self,name_logger):
        self.name_logger=name_logger
        self.logger=logging.getLogger(self.name_logger)


    def create_handler_with_level_and_format(self,level_logging,formatter_string,handler_type,**param_handler):
        '''
        This method adds handlers to the logger.
        Handlers are the outputs that a logger can have. For example, it can log to a file or to the console.
        Args:
            level_logging (str): 'debug', 'info', or 'error'
            formatter_string (str): The string format for the logs.
            handler_type (str): 'stream' or 'file'
            **param_handler: Extra parameters (like filename for FileHandler)
        '''
        handler_obj=FactoryHandler.select_handler(handler_type,**param_handler)
        formatter=logging.Formatter(formatter_string)
        level=FactoryLevel.select_level(level_logging)
        handler_obj.setLevel(level)
        handler_obj.setFormatter(formatter)
        self.logger.addHandler(handler_obj)
        return self.logger
    
class FactoryHandler:
        @staticmethod
        def select_handler(handler_type,**param):
            if handler_type=="stream":
                return logging.StreamHandler()
            if handler_type=="file":
                 return logging.FileHandler(**param)
            else:
                 raise ValueError(f"Unknown handler type: {handler_type}")

class FactoryLevel:
     @staticmethod
     def select_level(level_type):
        if level_type=="debug":
            return logging.DEBUG
        if level_type=="info":
            return logging.INFO
        if level_type=="error":
            return logging.ERROR
        else:
            raise ValueError(f"Unknown level type: {level_type}")

          

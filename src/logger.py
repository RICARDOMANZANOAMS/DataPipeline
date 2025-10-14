import os
import logging
import sys
class logger:
    _instance=None
    def __new__(cls):
        if cls._instance==None:
            cls._instance=super(logger,cls).__new__(cls)
            handler=logging.StreamHandler(sys.stdout)
            format_log=logging.Formatter("%(asctime)s [%(levelname)s] %(message)s","%Y-%m-%d %H:%M:%S")
            handler.setFormatter(format_log)

            cls._instance.logger=logging.getLogger("AppLogger")
            cls._instance.logger.setLevel(logging.INFO)
            cls._instance.logger.addHandler(handler)
            cls._instance.logger.propagate=False
               
        return cls._instance
    
    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)



    
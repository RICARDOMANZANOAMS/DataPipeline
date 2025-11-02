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
    
    @staticmethod
    def log_exceptions(get_logger):
        '''Decorator that logs exceptions using a dynamic logger from self or fixed logger.
            This decorator was created to not put try and except wrapping each function.
            In addition, it is dynamic since it takes a logger to log it which does flexible
            Args: 
                get_logger (Logger instance): Logger instance to use to log exceptions
        '''
        def decorator(func):
            '''
            Args:
                func: Original function to be wrapped by the code
            '''
            def wrapper(*args, **kwargs):
                # Support callable or direct logger
                logger = get_logger(args[0]) if callable(get_logger) else get_logger
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if logger:
                        #Logger error to log only the function where the error occurs. 
                        #It does not log the entire traceback. The entire traceback will be log in the upper layer of the flask
                        logger.error(f"Exception in {func.__name__}")
                    raise  # bubble up to Flask or outer layers
            return wrapper
        return decorator
    
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

class Operations:
    def __init__(self,logger):
        self.logger=logger

    @Logger.log_exceptions(lambda self: self.logger)
    def test_div (self,number):
        return number/0        



if __name__ == '__main__':
    try:
        logger=Logger("app")
        logger.create_handler_with_level_and_format("info", "%(asctime)s - %(levelname)s - %(message)s","file",filename="app.log")
        log = logger.logger
        log.setLevel(logging.DEBUG)
        log.info("test")
        log.error("test 1")
        log.info("test 1")
        operations=Operations(log)
        operations.test_div(4)
    except Exception as e:
        log.exception("this is the final error")



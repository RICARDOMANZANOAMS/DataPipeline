import logging
from typing import Callable, Union


class Logger:
    _instances = {}

    def __new__(cls, name= "app_logger"):
        if name in cls._instances:
            return cls._instances[name]
        instance = super().__new__(cls)
        cls._instances[name] = instance
        return instance

    def __init__(self, name_logger= "app_logger"):
        # Ensure __init__ runs only once per singleton instance
        if hasattr(self, "_initialized"):
            return
        self.name_logger = name_logger
        self.logger = logging.getLogger(self.name_logger)
        self._initialized = True

    def get_logger(self):
        """Return the internal logger instance."""
        return self.logger

    def create_handler_with_level_and_format(self, level_logging, formatter_string, handler_type, **param_handler):
        """
        Adds a handler to the logger.

        Args:
            level_logging (str): 'debug', 'info', or 'error' (case-insensitive)
            formatter_string (str): Format string for the log messages
            handler_type (str): 'stream' or 'file'
            **param_handler: Extra parameters for handler (like filename for FileHandler)
        """
        handler_obj = FactoryHandler.select_handler(handler_type, **param_handler)
        formatter = logging.Formatter(formatter_string)
        level = FactoryLevel.select_level(level_logging)

        handler_obj.setLevel(level)
        handler_obj.setFormatter(formatter)

        # Avoid adding duplicate handlers
        if not any(
            isinstance(h, type(handler_obj)) and getattr(h, "baseFilename", None) == getattr(handler_obj, "baseFilename", None)
            for h in self.logger.handlers
        ):
            self.logger.addHandler(handler_obj)

        return self.logger

    @staticmethod
    def log_exceptions(get_logger):
        """
        Decorator to log exceptions for a function using the provided logger.

        Args:
            get_logger (Logger instance or callable): Logger instance or callable returning a logger
            log_traceback (bool): If True, logs the full exception traceback
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Get logger dynamically if callable, else use provided instance
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
    def select_handler(handler_type, **param):
        """Return a logging handler based on type."""
        if handler_type.lower() == "stream":
            return logging.StreamHandler()
        elif handler_type.lower() == "file":
            return logging.FileHandler(**param)
        else:
            raise ValueError(f"Unknown handler type: {handler_type}")


class FactoryLevel:
    @staticmethod
    def select_level(level_type):
        """Return a logging level based on string input."""
        level_type = level_type.lower()
        if level_type == "debug":
            return logging.DEBUG
        elif level_type == "info":
            return logging.INFO
        elif level_type == "error":
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



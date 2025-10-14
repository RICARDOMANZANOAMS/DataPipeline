import unittest
import sys, os
from io import StringIO
from contextlib import redirect_stdout  
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from logger import logger
class testLogger(unittest.TestCase):
    
    def setUp(self):
        logger._instance=None
        self.logger=logger()
    
    def test_singleton_instance(self):
        logger2 = logger()
        self.assertIs(self.logger, logger2)

    def test_info_log_output(self):
        with self.assertLogs('AppLogger',level='INFO') as cm:
            self.logger.info("System started")        
        self.assertIn("INFO:AppLogger:System started",cm.output[0])
    
    def test_error_log_output(self):
        with self.assertLogs('AppLogger', level='ERROR') as cm:
            self.logger.error("System failed")
        self.assertIn("ERROR:AppLogger:System failed", cm.output[0])

   
if __name__ == "__main__":
    unittest.main()
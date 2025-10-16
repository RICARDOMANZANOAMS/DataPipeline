import unittest
import pandas as pd
import numpy as np
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
class testImputer(unittest.TestCase):

    def setUp(self):
        self.df=pd.DataFrame({'a':[4,5,6,np.nan],'b':[3,4,5,6]})
       
    def testMeanInputer(self):
        from imputer import meanImputer
        expected_df=pd.DataFrame({'a':[4,5,6,5],'b':[3,4,5,6]})
        mean_imputer=meanImputer()
        df_result=mean_imputer.impute(self.df,'a')
        pd.testing.assert_frame_equal(df_result, expected_df, check_dtype=False)
        
if __name__ == "__main__":
    unittest.main()

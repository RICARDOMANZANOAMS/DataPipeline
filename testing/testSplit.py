import unittest
import pandas as pd
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

class testSplit(unittest.TestCase):
    def setUp(self):
        self.df=pd.DataFrame({'a':[1,2,3,4,5,6,7,8,9,10],'b':[11,12,13,14,15,16,17,18,19,20]})
    
    def testDataSplitStrategy(self):
        from split import dataSplitStrategy
        data_split_strategy=dataSplitStrategy()
        result_array=data_split_strategy.splitDataset(self.df,0.3)
        train_result,test_result=result_array[0]
        expected_train_len =7
        expected_test_len = 3
        self.assertEqual(len(train_result), expected_train_len)
        self.assertEqual(len(test_result), expected_test_len)

    def test_kfold_strategy(self):
        from split import kFoldStrategy
        kfold_strategy = kFoldStrategy()
        kFolds = 5
        result_array = kfold_strategy.splitDataset(self.df, kFolds)
        self.assertEqual(len(result_array), kFolds)
        # Each split should have train + test = total rows
        for train, test in result_array:
            self.assertEqual(len(train) + len(test), len(self.df))

   
   
if __name__ == "__main__":
    unittest.main()
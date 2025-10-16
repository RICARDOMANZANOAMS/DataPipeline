import unittest
import tempfile
import pandas as pd
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from logger import logger
class testInputReader(unittest.TestCase):
    def setUp(self):
        logger._instance=None
        self.logger=logger()
    
    def testCsvReader(self):
        from inputReader import csvReader
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as tmp:
            df.to_csv(tmp.name, index=False)
            tmp_path = tmp.name
        csv_reader=csvReader()
        result = csv_reader.readInput(tmp_path)
        pd.testing.assert_frame_equal(result, df)
        os.remove(tmp_path)

    def testJsonReader(self):
        from inputReader import jsonReader
        import json
        dict=[{'a':3,'b':4}]
        df_expected = pd.DataFrame(dict)
        with tempfile.NamedTemporaryFile(mode="w+",suffix=".json",delete=False) as tmp:
            json.dump(dict,tmp)
            tmp_path=tmp.name
        json_reader=jsonReader()
        result=json_reader.readInput(tmp_path)
        pd.testing.assert_frame_equal(result, df_expected)
        os.remove(tmp_path)    

    def testCsvReaderFolder(self):   
        from inputReader import csvReaderFolder     
        df1 = pd.DataFrame({"a": [3, 4], "b": [5, 6]})
        df2 = pd.DataFrame({"a": [6, 7], "b": [8, 9]})       
        with tempfile.TemporaryDirectory() as tmp_dir:
            path1 = os.path.join(tmp_dir, "file1.csv")
            path2 = os.path.join(tmp_dir, "file2.csv")
            df1.to_csv(path1, index=False)
            df2.to_csv(path2, index=False)            
            csv_folder_reader = csvReaderFolder()
            result_df = csv_folder_reader.readInput(tmp_dir)
            expected_df = pd.concat([df1, df2], ignore_index=True)
            pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df)


if __name__ == "__main__":
    unittest.main()

    

    

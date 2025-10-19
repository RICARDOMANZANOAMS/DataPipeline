import unittest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

class testTrainer(unittest.TestCase):
    def setUp(self):
        self.df=pd.DataFrame({'f1':[2,3,4],'f2':[4,5,6],'label':[1,0,0]})
        self.featuresName=['f1','f2']
        self.labelName='label'
        self.model=RandomForestClassifier(random_state=32)

    def test_train(self):
        from trainer import trainer
        trainer_obj=trainer(self.df,self.featuresName,self.labelName)
        trainer_obj.model=self.model
        train_df=self.df.iloc[:3]
        test_df=self.df.iloc[3:]
        trainer_obj.train(train_df)
        self.assertTrue(hasattr(trainer_obj.model, "n_classes_"))




if __name__ == "__main__":
    unittest.main()
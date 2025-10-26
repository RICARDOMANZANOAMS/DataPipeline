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

    def test_test(self):
        from trainer import trainer
        import numpy as np
        np.random.seed(32)
        X = np.random.randn(100, 2)
        y = (X[:, 0] + X[:, 1] > 0).astype(int)  # linearly separable

        df = pd.DataFrame(X, columns=["f1", "f2"])
        df["label"] = y

        featuresName = ["f1", "f2"]
        labelName = "label"
        model = RandomForestClassifier(random_state=32, n_estimators=50)

        trainer_obj = trainer(df, featuresName, labelName)
        trainer_obj.model = model

        
        train_df = df.iloc[:80]
        test_df = df.iloc[80:]

        trainer_obj.train(train_df)
        predicted, ground_truth = trainer_obj.test(test_df)

        self.assertIsInstance(predicted, np.ndarray)
        self.assertIsInstance(ground_truth, np.ndarray)
        self.assertEqual(predicted.shape, ground_truth.shape)

        from sklearn.metrics import accuracy_score
        acc=accuracy_score(pd.DataFrame(predicted),pd.DataFrame(ground_truth))       
        self.assertIsInstance(acc, float)
        self.assertGreaterEqual(acc, 0.8)
        self.assertLessEqual(acc, 1.0)



if __name__ == "__main__":
    unittest.main()
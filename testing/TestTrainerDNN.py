import unittest
import torch.nn as nn
import numpy as np
import pandas as pd
import torch
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from trainerDNN import trainerDNN
from torch.utils.data import DataLoader
class TestTrainerDNN(unittest.TestCase):
    
    def setUp(self):
        X=np.random.rand(100,3)
        y=np.random.choice([1,0],size=100)
        self.feature_names=["f1","f2","f3"]
        self.label_name="label"
        X_pd=pd.DataFrame(X,columns=self.feature_names)
        y_pd=pd.DataFrame(y,columns=[self.label_name])
        self.dataset=pd.concat([X_pd,y_pd],axis=1)
        self.neural_network=nn.Sequential(
            nn.Linear(3,10),
            nn.ReLU(),
            nn.Linear(10,2)
        )
        print(self.neural_network)
        self.trainer_DNN=trainerDNN(self.dataset,self.feature_names,self.label_name)

    def test_create_dataloader(self):         
        dataloader= self.trainer_DNN.create_dataloader(batch_size=16, shuffle=True)
        self.assertIsInstance(dataloader,DataLoader)
        

if __name__ == "__main__":
   
    unittest.main(buffer=False)
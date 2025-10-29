import unittest
import torch.nn as nn
import numpy as np
import pandas as pd
import torch
import os
import sys
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from trainerDNN import trainerDNN
from torch.utils.data import DataLoader
class TestTrainerDNN(unittest.TestCase):
    
    def setUp(self):
        X=np.random.rand(120,3)
        y=np.random.choice([1,0],size=120)
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
        
        self.trainer_DNN=trainerDNN(self.dataset,self.feature_names,self.label_name)

    def test_create_dataloader(self):         
        dataloader= self.trainer_DNN.create_dataloader(self.dataset,batch_size=16, shuffle=True)
        self.assertIsInstance(dataloader,DataLoader)

        total_samples = len(self.dataset)
        loaded_samples = sum(batch[0].shape[0] for batch in dataloader)
        self.assertEqual(total_samples, loaded_samples)

    def test_split_split(self):
        split_tensors=self.trainer_DNN.split("split",{"test_size":0.2})
        self.assertIsInstance(split_tensors[0][0],DataLoader)
        self.assertIsInstance(split_tensors[0][1],DataLoader)
        length_dataset=len(self.dataset)
        length_train=length_dataset*0.8
        length_test=length_dataset-length_train
        length_train_dataloader = sum(batch[0].shape[0] for batch in split_tensors[0][0])
        length_test_dataloader = sum(batch[0].shape[0] for batch in split_tensors[0][1])
        self.assertEqual(length_train, length_train_dataloader)
        self.assertEqual(length_test, length_test_dataloader)

        
    def test_split_kfold(self):
        import math
        kFolds=3
        length_dataset=len(self.dataset)
        number_datasamples_test=math.ceil(length_dataset/3)
        number_datasamples_train=length_dataset-number_datasamples_test
        split_tensors=self.trainer_DNN.split("kFold",{"kFolds":kFolds})
        lenght_splits=3
        #Kfold 1
        self.assertEqual(lenght_splits, kFolds)  
        self.assertIsInstance(split_tensors[0][0],DataLoader)
        self.assertIsInstance(split_tensors[0][1],DataLoader)
        length_train_dataloader1 = sum(batch[0].shape[0] for batch in split_tensors[0][0])
        length_test_dataloader1 = sum(batch[0].shape[0] for batch in split_tensors[0][1])
        self.assertEqual(number_datasamples_train, length_train_dataloader1)
        self.assertEqual(number_datasamples_test, length_test_dataloader1)        
        #kfold 2
        self.assertIsInstance(split_tensors[1][0],DataLoader)
        self.assertIsInstance(split_tensors[1][1],DataLoader)
        length_train_dataloader2 = sum(batch[0].shape[0] for batch in split_tensors[1][0])
        length_test_dataloader2 = sum(batch[0].shape[0] for batch in split_tensors[1][1])
        self.assertEqual(number_datasamples_train, length_train_dataloader2)
        self.assertEqual(number_datasamples_test, length_test_dataloader2)
        #kfold 3
        self.assertIsInstance(split_tensors[2][0],DataLoader)
        self.assertIsInstance(split_tensors[2][1],DataLoader)
        length_train_dataloader3 = sum(batch[0].shape[0] for batch in split_tensors[2][0])
        length_test_dataloader3 = sum(batch[0].shape[0] for batch in split_tensors[2][1])
        self.assertEqual(number_datasamples_train, length_train_dataloader3)
        self.assertEqual(number_datasamples_test, length_test_dataloader3)
        
    def test_split_loocv(self):
        import math
        length_dataset=len(self.dataset)
        split_tensors=self.trainer_DNN.split("LOOCV",{})
        lenght_splits=len(split_tensors)
        self.assertEqual(120,  lenght_splits)

        self.assertIsInstance(split_tensors[0][0],DataLoader)
        self.assertIsInstance(split_tensors[0][1],DataLoader)
        length_train_dataloader1 = sum(batch[0].shape[0] for batch in split_tensors[0][0])
        length_test_dataloader1 = sum(batch[0].shape[0] for batch in split_tensors[0][1])
        self.assertEqual( length_dataset-1, length_train_dataloader1)
        self.assertEqual(1, length_test_dataloader1)   
    
    def test_train(self):
        def models_are_equal(model_a, model_b, device="cpu"):
            for p1, p2 in zip(model_a.parameters(), model_b.parameters()):
                if not torch.equal(p1.to(device), p2.to(device)):
                    return False
            return True

        initial_model = copy.deepcopy(self.neural_network)
        modified_model=copy.deepcopy(self.neural_network)
        split_tensors=self.trainer_DNN.split("split",{"test_size":0.2})
        train=split_tensors[0][0]
        test=split_tensors[0][1]
        model_after_training=self.trainer_DNN.train_dnn(train,self.neural_network,10,0.001)
        self.assertFalse(
            models_are_equal(initial_model, model_after_training),
            "Model parameters (weights/biases) did not change after training"
        )
 

if __name__ == "__main__":   
    unittest.main()
from trainer import trainer
class traineDNN(trainer):
    def __init__(self,df,featureNames,labelName):
        super().__init__(df,featureNames,labelName)
        self.split

    def split(self,splitMethod,params):
        from split import factorySplit       
        import torch
        import numpy as np
        objFactorySplit=factorySplit.selectSplit(splitMethod)  #Select the split method
        self.splitArray=objFactorySplit.splitDataset(self.df,**params) #Split the dataset
        split_tensors=[]
        for split_element in self.splitArray:
            train=split_element[0]
            test=split_element[1]
            train_tensor=self.create_dataloader(train)
            test_tensor=self.create_dataloader(test)
            split_tensors.append((train_tensor,test_tensor))
        self.splitArray=split_tensors
            
    def create_dataloader(self,df):
        import torch
        from torch.utils.data import TensorDataset, DataLoader
        features=torch.tensor(df[self.featureNames].to_numpy())
        label=torch.tensor(df[self.labelName].to_numpy())
        tensor_dataset=TensorDataset(features,label)
        dataloader_dataset=DataLoader(tensor_dataset,batch_size=32)
        return dataloader_dataset


   
    

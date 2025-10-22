from trainer import trainer
class trainerDNN(trainer):
    def __init__(self,df,featureNames,labelName):
        super().__init__(df,featureNames,labelName)
        

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
        return split_tensors
            
    def create_dataloader(self,df,batch_size=32,shuffle=True):
        import torch
        from torch.utils.data import TensorDataset, DataLoader
        features=torch.tensor(df[self.featureNames].to_numpy())
        label=torch.tensor(df[self.labelName].to_numpy())
        tensor_dataset=TensorDataset(features,label)
        dataloader_dataset=DataLoader(tensor_dataset,batch_size=batch_size,shuffle=True)
        return dataloader_dataset
    
    def train(self, dataloader, model, num_epochs=10, lr=0.001):
        import torch
        import torch.nn as nn
        import torch.optim as optim
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = model.to(device)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=lr)

        model.train()
        for epoch in range(num_epochs):
            total_loss = 0
            for features, label in dataloader:
                features, label = features.to(device).float(), label.to(device).long()

                optimizer.zero_grad()
                outputs = model(features)
                loss = criterion(outputs, label)
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
        self.model=model
        
    def test(self,dataloader,model):
        import torch
        import torch.nn as nn
        predicted_all=[]
        true_labels_all=[]
        with torch.no_grad():
            for features, labels in dataloader:                
                outputs=model(features)
                probs=nn.functional.softmax(outputs,dim=1)
                _,labels_predicted=torch.max(probs,1)
                               
                predicted_all.extend(labels_predicted.cpu().numpy())
                true_labels_all.append(labels.cpu().numpy())

        return np.array(predicted_all), np.array(true_labels_all)


    
           

    
import numpy as np
import pandas as pd

x=np.random.rand(30,4)
y=np.random.choice([1,0],size=30)    
feature_names=['f1','f2','f3','f4']
X=pd.DataFrame(x,columns=feature_names)
y=pd.DataFrame(y,columns=['label'])
print(X)
print(y)
dataset=pd.concat([X,y],axis=1)
print(dataset)
trainer_dnn=trainerDNN(dataset,feature_names,'label')
dataloader=trainer_dnn.create_dataloader(dataset)
print(dataloader)
train_test=trainer_dnn.split("split",{"test_size":0.2})
print(train_test)

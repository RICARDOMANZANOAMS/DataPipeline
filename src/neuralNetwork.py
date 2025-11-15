import torch.nn as nn
import torch
from Logger import Logger
class BaseModel(nn.Module):
    def __init__(self):
        self.logger=Logger().get_logger()
        super(BaseModel, self).__init__()

    def forward(self, x):
        raise NotImplementedError("Subclasses must implement forward method")
    
class FeedForwardNN(BaseModel):
    
    def __init__(self, input_size, layers_array, output_size):
        super(FeedForwardNN, self).__init__()
        layer_sizes = [input_size] + layers_array + [output_size]
        self.layers = nn.ModuleList([
            nn.Linear(layer_sizes[i], layer_sizes[i + 1])
            for i in range(len(layer_sizes) - 1)
        ])
    @Logger.log_exceptions(lambda self: self.logger) 
    def forward(self, x):
        for i, layer in enumerate(self.layers):
            x = layer(x)
            if i < len(self.layers) - 1:
                x = torch.relu(x)
        return x
    
class CNN(BaseModel):
   
    def __init__(self,input_channels,number_layers,output):
        self.convs = nn.ModuleList()
        for i in range(number_layers):           
            in_channels = input_channels if i == 0 else 10
            conv_layer = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=10, kernel_size=3, padding=1, stride=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3)
            )

            self.convs.append(conv_layer)
        self.flatten=nn.Flatten()
        self.fc = nn.Linear(10 * 3 * 3, output) 
    @Logger.log_exceptions(lambda self: self.logger) 
    def forward(self,x):
        for conv in self.convs:
            x = conv(x)
        x = self.flatten(x)
        x = self.fc(x)
        return x

network=FeedForwardNN(3,[100,100,200],5)
print(network)
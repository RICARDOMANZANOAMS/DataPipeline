import torch.nn as nn
import torch
class BaseModel(nn.Module):
    def __init__(self):
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

    def forward(self, x):
        for i, layer in enumerate(self.layers):
            x = layer(x)
            if i < len(self.layers) - 1:
                x = torch.relu(x)
        return x
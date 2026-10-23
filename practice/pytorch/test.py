import torch
import torch.nn as nn

print("PyTorch:", torch.__version__)

x = torch.randn(2, 4)
layer = nn.Linear(4, 2)
output = layer(x)

print("Output shape:", output.shape)
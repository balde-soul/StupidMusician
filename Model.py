#In[]:
import torch
import torch.nn as nn
import numpy as np

lstm = nn.LSTM(10, 20, 2)

#In[]:
rnn = nn.LSTM(10, 20, 2)
input = torch.randn(5, 3, 10).cuda()
h0 = torch.randn(2, 3, 20).cuda()
c0 = torch.randn(2, 3, 20).cuda()
output, (hn, cn) = rnn(input, (h0, c0))
print(output)

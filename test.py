from reptile import reptile

import torch.nn as nn
from model.config import network

class MPLNetWork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.network = network

    def forward(self, x):
        # x = self.flatten(x)
        logits = self.network(x)
        return logits

from model import model



def check_url(url):
    a = reptile.getImg("https://blog.csdn.net/LJHandCXY/article/details/106974982")
    b= model.check_is_there_ant(a)
    print(b)
    return b[0]
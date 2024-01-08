import torch
import torch.nn as nn
from config import device,network,learning_rate,epoch,load_flag
from data_loader import dataloader,dataset
class MPLNetWork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten=nn.Flatten()
        self.network=network

    def forward(self,x):
        # x = self.flatten(x)
        logits = self.network(x)
        return logits


def train(model,optimizer,loss_fn):
    model.to(device)
    model.train()
    size = len(dataset)
    for batch,(x,y) in enumerate(dataloader):
        x=x.to(device)
        y=y.to(device)
        pred = model(x)

        # pred = torch.argmax(pred,dim=1)
        # pred=pred.to(torch.float32)
        # print(pred,y)
        loss = loss_fn(pred,y)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch% 10==0:
            loss,current = loss.item(),(batch + 1)*len(x)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def main():
    if load_flag:
        model = torch.load('model.pth')
    else:
        model = MPLNetWork()

    loss_function=nn.CrossEntropyLoss()
    optimizer=torch.optim.SGD(model.parameters(),lr=learning_rate)
    for i in range(epoch):
        print(f"--------------epoch{i}-----------------")
        train(model,optimizer,loss_function)
    torch.save(model, 'model1.pth')


if __name__=="__main__":
    main()
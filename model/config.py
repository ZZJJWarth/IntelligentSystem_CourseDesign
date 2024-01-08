import torch.nn as nn
datasets_path="dataset"
batch_size=32
device="cuda:0"
input_size=(256,256)
learning_rate=0.01
epoch=30
load_flag=True
network=nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2, padding=0),

            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2, padding=0),

            nn.Conv2d(64, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2, padding=0),

            nn.Flatten(),

            nn.Linear(16 *32*32, 512),
            nn.ReLU(),
            #
            nn.Linear(512, 2)
        )

def main():
    import torch
    x=torch.rand(1,3,256,256)
    print(network(x).shape)
    # print("?")

if __name__=="__main__":
    main()
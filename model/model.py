import torch
from PIL import Image
from torchvision import transforms
import torch.nn as nn
from model.config import network


# from model.train import MPLNetWork



# from train import MPLNetWork
model = torch.load(r"model\model1.pth").to("cpu")
resize_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])
model.eval()
a = ""


def testImg(path):
    with Image.open(fr"{path}.jpg") as img:
        resize_img = resize_transform(img)
        try:
            a = resize_img.reshape((1, 3, 256, 256))
        except Exception:
            return 1,"none"

        # print(model(a))
        return torch.argmax(a).item(), path


def check_is_there_ant(index):
    for i in range(1, index):
        ans = testImg(fr"image\image{i}")
        if ans[0] == 0:
            return True, ans[1]
        else:
            continue
    return False,-114514

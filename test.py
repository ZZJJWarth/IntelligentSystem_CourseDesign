from reptile import reptile
from model import model
def check_url(url):
    import requests
    try:
        response = requests.get(url)
        if not response.ok:
            return -1,f"we can not connect to the website:{url}"
    except Exception:
        return -1,"there are some errors occurred when we try to connect to the website"
    a = reptile.getImg(url)
    b = model.check_is_there_ant(a)
    print(b)
    if b[0]:
        return 1,"your website might contain some images of ants!"
    else:
        return 0,"your website might not have images of ants!"

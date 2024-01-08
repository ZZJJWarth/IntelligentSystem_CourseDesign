import requests
import re
# website="https://www.bing.com/search?q=%E4%BB%BB%E6%84%8F%E9%95%BF%E5%BA%A6%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&form=ANNNB1&refig=907E5545DEF34BF9A08F1463FC895853&sp=5&lq=0&qs=HS&sk=HS4&sc=10-0&cvid=907e5545def34bf9a08f1463fc895853"

header={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.82"
}
pattern="<img .*>"
pattern1="src=\".*?\""
def operate(website):
    a = requests.get(website, headers=header)
    strr = a.text
    img_label_list = re.findall(pattern, strr)
    ima_url_list = []
    for i in img_label_list:
        span = re.search(pattern1, i).span()
        start = span[0]
        end = span[1]
        # print(i[span[0] + 5:span[1] - 1])
        ima_url_list.append(i[span[0] + 5:span[1] - 1])

    count = 1
    for i in ima_url_list:
        if len(i) < 7 or i[0:4] != "http":
            continue
        with open(fr"image\image{count}.jpg", "wb") as f:
            a = requests.get(i)
            if a.ok:
                f.write(a.content)
                count += 1
            else:
                continue
    return (count)
def getImg(url):
    return operate(url)
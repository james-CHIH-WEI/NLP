import requests
from bs4 import BeautifulSoup
import time

f = open("url.txt", mode="r", encoding="UTF-8")
f2 = open("content_word_cloud.txt", mode="w", encoding="UTF-8")
i = 0

for line in f.read().splitlines():
    print(line)
    r = requests.get(line)
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")

    for content in soup.select("p"):
        if content.text.find("政治中心", 0, 4) < 0 and content.text.find("更多", 0, 2) < 0:
            if content.text.find("全民養肺") > 0:
                continue
            else:
                f2.write(content.text)
    time.sleep(1)
    i += 1
    print(i)

f.close
f2.close

# 351筆新聞

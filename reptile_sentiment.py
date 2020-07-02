# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import requests
from bs4 import BeautifulSoup
import time

f = open("url.txt", mode="r", encoding="UTF-8")
f2 = open("sentiment_content.csv", mode="w", encoding="UTF-8")
i = 0

f2.write("content#,#sentiment#,#positive#,#negative#,#label\n")

for line in f.read().splitlines():
    print(line)
    r = requests.get(line)
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    content_all = ""
    positive = 0
    negative = 0
    for content in soup.select("p"):
        print(content.text)
        if (
            content.text.find("政治中心", 0, 4) < 0
            and content.text.find("更多", 0, 2) < 0
            and content.text != ""
        ):
            if content.text.find("全民養肺") > 0:
                continue
            else:
                content_all += content.text
                sentiment_value = SnowNLP(content.text).sentiments
                if sentiment_value >= 0.5:
                    positive += 1
                else:
                    negative += 1

    if positive > negative:
        label = "正面"
    else:
        label = "負面"

    f2.write(
        content_all
        + "#,#"
        + str(sentiment_value)
        + "#,#"
        + str(positive)
        + "#,#"
        + str(negative)
        + "#,#"
        + label
        + "\n"
    )
    time.sleep(1)
    i += 1
    print(i, "\n\n")

    # if i == 3:
    #     break

f.close
f2.close

# 351筆新聞

# -*- coding: utf-8 -*-
from snownlp import SnowNLP

text = "高雄市長韓國瑜因罷免案下台，其任內主打的路平清水溝政策，讓高雄的路面不再坑坑洞洞，但這幾天，有些高雄人發現三民區、前金區、楠梓區等地的路面，柏油路面都挖補的痕跡，照片曝光後，有粉專直言，「開始想念川伯了」。臉書粉專「韓黑父母不崩潰」今分享幾張高雄「路不平」照片，其中三民區建工路、前金區大同路、楠梓區軍校路和右昌街口，都出現柏油路出現新刨補柏油，蓋掉原有地面標線的場景，粉專直言「熟悉的坑洞最對味」、「開始想念川伯了嗎？」。照片PO出才一小時，就吸引2百多位網友分享、留言，1千多位網友傳達心情。但最讓人驚訝的照片就是楠梓區軍校路和右昌街口，拍攝的盧姓網友說照片時間是在6月15日下午5點多拍攝，該路段位置緊鄰海軍官校。其他網友也表示，「這段路真的爛爆，往後面走更精采，微上坡加補丁，堪稱越野道」。但也有網友說，「要像罷韓盯韓市府一樣的盯新市府」。"
s = SnowNLP(text)
print(s.sentiments)
p = 0
n = 0

for sentence in s.sentences:
    # print(sentence)
    if SnowNLP(sentence).sentiments >= 0.5:
        p += 1
    else:
        n += 1

print("正向：", p)
print("負向：", n)
# s1 = SnowNLP(s.sentences[0])
# print(s1.sentiments)


# s1 = SnowNLP(s.sentences[1])
# s1.sentiments
# print(s1.sentiments)

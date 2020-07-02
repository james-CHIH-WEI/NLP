from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import numpy as np
from collections import Counter

with open("content_word_cloud.txt", encoding="utf8", errors="ignore") as f:
    text = f.read()

# 設定使用 big5 斷詞
jieba.set_dictionary("dict.txt")
wordlist = jieba.cut(text)
words = " ".join(wordlist)
# 文字雲造型圖片
# mask = np.array(Image.open("picture.png"))  # 文字雲形狀
# 從 Google 下載的中文字型
font = "SourceHanSansTW-Regular.otf"
# 背景顏色預設黑色，改為白色、使用指定圖形、使用指定字體
my_wordcloud = WordCloud(background_color="white", font_path=font).generate(words)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
# 存檔
my_wordcloud.to_file("word_cloud.png")


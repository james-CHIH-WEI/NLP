from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(chrome_options=options)
driver.get(
    "https://tw.news.yahoo.com/search?p=%E9%9F%93%E5%9C%8B%E7%91%9C&fr=uh3_news_vert_gs&fr2=p%3Anews%2Cm%3Asb"
)


def pulldown():
    time.sleep(5)
    t = True
    i = 1
    while t:
        check_height = driver.execute_script(
            "return document.documentElement.scrollHeight;"
        )
        for _ in range(10):
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,1000)")
            print("第%s頁" % str(i))
            i += 1

            check_height1 = driver.execute_script(
                "return document.documentElement.scrollHeight;"
            )
            print(str(check_height) + "**************" + str(check_height1))
        if check_height == check_height1:
            print("finish")
            t = False
            soup = BeautifulSoup(driver.page_source, "html.parser")
            f = open("url.txt", mode="r+", encoding="UTF-8")
            for a in soup.select("li.StreamMegaItem a"):
                f.write("https://tw.news.yahoo.com" + a["href"] + "\n")
            f.close


pulldown()

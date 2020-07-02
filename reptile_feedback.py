from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(chrome_options=options)
driver.get(
    "https://tw.news.yahoo.com/%E7%8E%8B%E9%87%91%E5%B9%B3-%E9%9F%93%E5%9C%8B%E7%91%9C%E5%9D%90-%E8%B5%B7-%E4%BA%92%E5%8B%95%E7%95%AB%E9%9D%A2%E6%9B%9D%E5%85%89-024011859.html"
)

time.sleep(7)
driver.find_element_by_css_selector(".button.Fz").click()
# link = driver.find_element_by_link_text("顯示較多內容")
# link.click()

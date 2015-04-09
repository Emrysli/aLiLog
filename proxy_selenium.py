#-*-coding:utf8-*-
from selenium import webdriver
PROXY = "socks5://127.0.0.1:1080"

chrome_options = webdriver.ChromeOptions()
print chrome_options
chrome_options.add_argument("--proxy-server={}".format(PROXY) )
chrome = webdriver.Chrome(executable_path=r"C:/Program Files/Google/Chrome/Application/chromedriver.exe", chrome_options=chrome_options)
chrome.get("https://www.google.com")


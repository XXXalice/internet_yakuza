from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
chrome.get("https://www.google.co.jp")
sleep(5)
chrome.close()
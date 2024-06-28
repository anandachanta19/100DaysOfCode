from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
assets = []
buys = driver.find_elements(By.CSS_SELECTOR, value="#store b")

# Slicing the Extra Div
buys = buys[:len(buys)-1]

# Getting Prices
for buy in buys:
    cost = buy.text.split(" - ")[1]
    if "," in cost:
        cost = "".join(cost.split(","))
    assets.append(int(cost))


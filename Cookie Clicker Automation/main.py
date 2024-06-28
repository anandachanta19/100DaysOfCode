from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

timeout = time.time() + 5
five_min = time.time() + 300

while True:
    cookie.click()
    # Every 5 seconds check for assets
    if time.time() > timeout:

        # Calculating Prices
        options = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        prices = []

        for opt in options:
            if opt.text != "":
                prices.append(float(opt.text.split(" - ")[1].replace(",", "")))

        # Calculating the current money
        money = float(driver.find_element(By.CSS_SELECTOR, value="#money").text.replace(",", ""))

        # Finding the most expensive one which can be affordable can be Affordable!
        for i in range(len(prices)):
            if prices[i] < money:
                continue
            else:
                options[i - 1].click()
                break

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_rate = driver.find_element(By.XPATH, value='//*[@id="cps"]').text
        print(cookie_rate)
        break


import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

load_dotenv()

GOOGLE_FORM = os.getenv("GOOGLE_FORM")

content = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
website_html = content.text
soup = BeautifulSoup(website_html, "html.parser")
# Getting track of links
links_elements = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor", href=True)
links = []
for link in links_elements:
    links.append(link["href"])
# Getting track of addresses
address_elements = soup.find_all(name="address")
addresses = []
for address in address_elements:
    addresses.append(address.text.replace("  ", ""))
# Getting track of prices
price_elements = soup.find_all(name="span", attrs="PropertyCardWrapper__StyledPriceLine")
prices = []
for price in price_elements:
    prices.append(price.text[:6])

# Filling the form using selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(chrome_options)
count = 0
while count < len(links):
    driver.get(url=GOOGLE_FORM)
    sleep(3)
    # Entering the data
    # Addresses
    q1 = driver.find_element(
        By.XPATH,
        value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    q1.click()
    q1.send_keys(addresses[count])
    # Price per month
    q2 = driver.find_element(
        By.XPATH,
        value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    q2.click()
    q2.send_keys(prices[count])
    # Link
    q3 = driver.find_element(
        By.XPATH,
        value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    q3.click()
    q3.send_keys(links[count])
    # Submit
    submit = driver.find_element(
        By.XPATH,
        value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span'
    )
    submit.click()
    count += 1

driver.quit()

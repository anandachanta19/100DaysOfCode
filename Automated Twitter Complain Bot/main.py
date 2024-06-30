import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

load_dotenv()

# Promised Network Details
PROMISED_DOWN = 150
PROMISED_UP = 10
# Twitter Credentials
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
# Speed Test Website
SPEED_TEST_URL = "https://www.speedtest.net/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        self.driver.maximize_window()
        # Targeting Go Button
        start = self.driver.find_element(By.CSS_SELECTOR, value="a .start-text")
        start.click()
        print("Hold on! Just 1 min\nBot on duty..Fetching Results!!!")
        # Wait for 1 min to fetch results
        sleep(60)
        self.down = float(
            self.driver.find_element(
                By.XPATH,
                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                      '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        )
        self.up = float(
            self.driver.find_element(
                By.XPATH,
                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                      'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        )
        # Don't use self.driver.quit() it may caus Max Retry Error
        print("Successfully Fetched Internet Speed")

    def complain_via_twitter(self):
        sleep(10)
        self.driver.get("https://x.com/login")
        sleep(3)
        self.driver.maximize_window()
        email = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
                  '/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
        )
        sleep(3)
        email.click()
        email.send_keys(TWITTER_EMAIL, Keys.ENTER)
        sleep(3)
        try:
            password = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
                      '/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
            )
            sleep(2)
            password.click()
            password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                      'div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
            )
            sleep(3)
            username.send_keys(TWITTER_USERNAME, Keys.ENTER)
            sleep(3)
            password = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div'
                      '/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
            )
            sleep(2)
            password.click()
            password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        sleep(2)
        tweet = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div'
                  '/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div'
                  '/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        )
        sleep(2)
        message = (f"Hey Internet Provider, why is my internet speed {self.down}"
                   f"down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet.click()
        tweet.send_keys(message)
        post = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]'
                  '/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span'
        )
        sleep(1)
        post.click()
        sleep(2)
        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
sleep(5)
if twitter_bot.down < PROMISED_DOWN or twitter_bot.up < PROMISED_UP:
    print("Oh no! The speeds are slower than promised we should complain. Bot on duty!")
    twitter_bot.complain_via_twitter()
else:
    print("Hurray! You got a perfect provider!")

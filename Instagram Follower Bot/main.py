import os
from dotenv import load_dotenv
from selenium import webdriver
from time import sleep

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

INSTA_EMAIL = os.getenv("INSTA_EMAIL")
INSTA_PASSWORD = os.getenv("INSTA_PASSWORD")
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        print("Bot Started LogIn Process")
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        sleep(2)
        email = self.driver.find_element(
            By.XPATH,
            value='//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        sleep(2)
        email.send_keys(INSTA_EMAIL)
        sleep(1)
        password = self.driver.find_element(
            By.XPATH,
            value='//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        sleep(2)
        password.send_keys(INSTA_PASSWORD)
        sleep(1)
        login = self.driver.find_element(
            By.XPATH,
            value='//*[@id="loginForm"]/div/div[3]/button'
        )
        login.click()
        print("Login Success!")
        sleep(10)

        # Closing Save LogIn Info
        not_now = self.driver.find_element(
            By.XPATH,
            value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'
        )
        sleep(1)
        not_now.click()
        sleep(10)

        # Closing Notifications Popup
        notifications = self.driver.find_element(
            By.XPATH,
            value='/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
        )
        sleep(1)
        notifications.click()

    def find_followers(self):
        sleep(3)
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        sleep(5.2)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        sleep(5)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

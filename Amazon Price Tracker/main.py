from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

load_dotenv()

FROM = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_APP_PASSWORD")
TO = os.getenv("TO_EMAIL")
AMAZON_PRODUCT_URL = ("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
TARGET_PRICE = 100

HEADERS = {
    "User-Agent": "Mozilla/5.0 "
                  "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,te;q=0.8"
}

response = requests.get(url=AMAZON_PRODUCT_URL, headers=HEADERS)
website_html = response.text
soup = BeautifulSoup(website_html, "lxml")
price = float(soup.find(name="span", attrs="a-price-whole").text)
name = " ".join(soup.find(name="span", attrs="product-title-word-break").text.split()[:5])


if price <= TARGET_PRICE:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=FROM, password=PASSWORD)
    connection.sendmail(from_addr=FROM,
                        to_addrs=TO,
                        msg=f"Subject:Product Price Declined!\n\n"
                            f"Hey! {name}.. has decreased to the target price! "
                            f"Go Ahead and Buy Now!"
                            f"Here is the link: {AMAZON_PRODUCT_URL}")
    connection.close()
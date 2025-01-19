from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("SENDER_EMAIL")
recipient_email = os.getenv("RECIPIENT_EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")

URL = "https://appbrewery.github.io/instant_pot/"
header = {"Accept-Language": "en-US,en",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
response = requests.get(url=URL, headers=header)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, 'html.parser')
whole_price = soup.find(name="span", class_="a-price-whole").getText()
decimal_price = soup.find(name="span", class_="a-price-fraction").getText()
price = float(whole_price + decimal_price)
product_name = soup.select("span.a-size-large.product-title-word-break")[0].getText()

if price < 100:
    subject = "Amazon Price Alert!"
    body = f"{product_name} is now ${price}"
    msg=f"Subject:{subject}\n\n{body}".encode('utf-8')

    try:
        with smtplib.SMTP(smtp_server) as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_password)
            connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=msg)

    except smtplib.SMTPAuthenticationError:
        print("Failed to login, check your email and password.")

    except Exception as e:
        print(f"An error occurred: {e}")

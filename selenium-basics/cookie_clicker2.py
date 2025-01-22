from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value="cookie")


def click():
    for _ in range(500):
        try:
            cookie.click()
        except Exception as e:
            print(f"Error clicking the cookie: {e}")
            break


def get_item_prices():
    items = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab"]
    prices = []
    for item in items:
        try:
            price_text = driver.find_element(By.ID, value=item).text.split()[-1].replace(",", "")
            prices.append(int(price_text))
        except Exception:
            prices.append(float("inf"))  # Set to infinity if the element is unavailable
    return items, prices


for _ in range(10):  # Adjust the range to control the runtime
    click()
    time.sleep(5)

    # Update cookies count
    try:
        current_cookies = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
    except Exception as e:
        print(f"Error retrieving cookies count: {e}")
        current_cookies = 0

    # Get current item prices
    item_names, item_values = get_item_prices()

    # Find affordable items
    affordable_items = [
        (name, value) for name, value in zip(item_names, item_values) if value <= current_cookies
    ]

    # Buy the most expensive affordable item
    if affordable_items:
        max_item = max(affordable_items, key=lambda item: item[1])
        try:
            driver.find_element(By.ID, value=max_item[0]).click()
        except Exception as e:
            print(f"Error buying upgrade {max_item[0]}: {e}")

time.sleep(15)
driver.quit()

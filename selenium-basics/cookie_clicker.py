# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# URL = "https://orteil.dashnet.org/experiments/cookie/"
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(URL)
#
# cookie = driver.find_element(By.ID, value="cookie")
# cursor = int(driver.find_element(By.ID, value="buyCursor").text.split()[2].replace(",", ""))
# grandma = int(driver.find_element(By.ID, value="buyGrandma").text.split()[2].replace(",", ""))
# factory = int(driver.find_element(By.ID, value="buyFactory").text.split()[2].replace(",", ""))
# mine = int(driver.find_element(By.ID, value="buyMine").text.split()[2].replace(",", ""))
# shipment = int(driver.find_element(By.ID, value="buyShipment").text.split()[2].replace(",", ""))
# alchemy_lab = int(driver.find_element(By.ID, value="buyAlchemy lab").text.split()[3].replace(",", ""))
# current_cookies = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
#
#
# def click():
#     global cookie
#     for i in range(500):
#         cookie.click()
#
#
# for _ in range(10):
#     click()
#     time.sleep(5)
#     item_names = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab"]
#     item_values = [cursor, grandma, factory, mine, shipment, alchemy_lab]
#
#     affordable_items = [(name, value) for name, value in zip(item_names, item_values) if value <= current_cookies]
#
#     if affordable_items:
#         max_item = max(affordable_items, key=lambda item: item[1])
#         driver.find_element(By.ID, value=max_item[0]).click()
#
#
# time.sleep(15)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, name in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = name


        # Purchase the most expensive affordable upgrade
        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
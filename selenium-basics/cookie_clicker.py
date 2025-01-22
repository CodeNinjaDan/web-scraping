from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value="cookie")
cursor = int(driver.find_element(By.ID, value="buyCursor").text.split()[2].replace(",", ""))
grandma = int(driver.find_element(By.ID, value="buyGrandma").text.split()[2].replace(",", ""))
factory = int(driver.find_element(By.ID, value="buyFactory").text.split()[2].replace(",", ""))
mine = int(driver.find_element(By.ID, value="buyMine").text.split()[2].replace(",", ""))
shipment = int(driver.find_element(By.ID, value="buyShipment").text.split()[2].replace(",", ""))
alchemy_lab = int(driver.find_element(By.ID, value="buyAlchemy lab").text.split()[3].replace(",", ""))
current_cookies = int(driver.find_element(By.ID, value="money").text.replace(",", ""))


def click():
    global cookie
    for i in range(500):
        cookie.click()


for _ in range(10):
    click()
    time.sleep(5)
    item_names = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab"]
    item_values = [cursor, grandma, factory, mine, shipment, alchemy_lab]

    affordable_items = [(name, value) for name, value in zip(item_names, item_values) if value <= current_cookies]

    if affordable_items:
        max_item = max(affordable_items, key=lambda item: item[1])
        driver.find_element(By.ID, value=max_item[0]).click()


time.sleep(15)
driver.quit()
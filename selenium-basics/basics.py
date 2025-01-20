from selenium import webdriver
from selenium.webdriver.common.by import By

# URL = "https://www.amazon.com/dp/B0CN8HL597/ref=sspa_dk_detail_6?s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw"
URL = "https://www.python.org/"

#Keep browser open after code finishes running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_fraction}")

#By Name
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#By ID
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#By CSS Selector
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#By Xpath
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


#-----------Print Event Dates from python.org---------------

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# driver.close()#Close current tab
driver.quit()#Close browser

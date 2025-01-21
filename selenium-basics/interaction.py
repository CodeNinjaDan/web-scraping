import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# URL = "https://en.wikipedia.org/wiki/Main_Page"
URL = "https://secure-retreat-92358.herokuapp.com/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# # #Click link
# # article_numbers = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# # article_numbers.click()
#
# # #Find element by Link Text
# # all_links = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_links.click()
#
# #Find the search <input/> by name
# search = driver.find_element(By.NAME, value="search")
#
# #Send keyboard input to Selenium
# search.send_keys("Python", Keys.ENTER)


fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
fname.send_keys("Dan", Keys.ENTER)
lname.send_keys("Muiru", Keys.ENTER)
email.send_keys("dnlmuiru@gmail.com", Keys.ENTER)

time.sleep(5)
driver.quit()
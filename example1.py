# python -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("A:\\Users\\nkomo\\Documents\\DevOps\\projects\\B2\\python_selenium_sf\\python_selenium_sf\\chromedriver.exe")
driver.get("http://130.193.37.179/app/pets")
t = (driver.find_elements(By.XPATH, "//*[@id=\"image\"]"))[0].click()
sleep(3)

driver.save_screenshot("pet_home987964.png")
sleep(100)
driver.quit()
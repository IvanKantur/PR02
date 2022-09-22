from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("C:/Users/1/VSCode_projects/pr02/chromedriver")
driver.get("https://google.com")
driver.find_element(By.XPATH, "//input[@title=\'Поиск\']").send_keys('Долина привидений' + Keys.RETURN)

sleep(1)

driver.save_screenshot('sf.png')
driver.quit()
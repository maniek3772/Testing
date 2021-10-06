#Selenium Tutorial 2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "F:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

# wyszukaj na stronie 1) ID, 2) name, 3 class
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))
    ariticles = main.find_elements_by_tag_name("article")
    for article in ariticles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()

driver.quit()
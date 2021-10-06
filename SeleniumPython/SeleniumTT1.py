# Selenium Tutorial 1 
# webdriver chrome https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver

PATH = "F:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
# przejdź na strone
driver.get("https://www.facebook.com/")
# wyświetl nazwę strony
print(driver.title)
# zamknij kartę
#driver.close()
# zamknij przeglądarkę
#driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


filepath = "F:\\Testing\\SeleniumPython\\TrasaKato.txt"
f = open(filepath, "r")
f1 = open('F:\\Testing\\SeleniumPython\\TrasaKato1.txt',"w")
plik = f.read()
lista = plik.split("\n")


PATH = "F:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 10)

# otwórz Google Maps
driver.get("https://www.google.com/maps/@50.2322642,18.9995082,14.54z")

# przewinięcie na dół strony
driver.find_element_by_tag_name('html').send_keys(Keys.END)
time.sleep(1)

#maksymalizacja okna
driver.maximize_window()

# wyłącz okno z prywatnością
driver.find_element_by_xpath('//button[@jsname="higCR"] ').click()

# przejdź do trasy
wait.until(EC.presence_of_element_located((By.XPATH,'//button[@class="xoLGzf-T3iPGc"]'))).click()

x=0
for x in range(x,len(lista)):
    lista1 = lista[x].split(';')
    y = lista1[0]
    z = lista1[1]

    # od miejsca
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sb_ifc51 > input'))).clear()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sb_ifc51 > input'))).send_keys(y)
    time.sleep(1)

    #wait.until(EC.presence_of_element_located(())).click()
    # do miejsca
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sb_ifc52 > input'))).send_keys(z)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sb_ifc52 > input'))).send_keys(Keys.RETURN)

    # trasa samochodowa
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[2]/button'))).click()
    time.sleep(1)

    # dystans pomiedzy
    droga = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[2]/div')))

    #zapis do pliku
    print(lista[x] + "; " + droga.text)
    f1.write(lista[x] + "; " + droga.text + '\n')

    # od miejsca czyszczenie
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sb_ifc51 > input'))).clear()
    time.sleep(1)
    # do miejsca czyszczenie
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sb_ifc52 > input'))).clear()

f1.close()
f.close()
driver.quit()
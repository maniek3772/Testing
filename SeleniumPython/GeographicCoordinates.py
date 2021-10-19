#-*- coding: iso-8859-2 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


filepath = 'F:\\Testing\\SeleniumPython\\KatoCoordinates.txt'
f = open(filepath, "r",encoding='utf8')
f1 = open('F:\\Testing\\SeleniumPython\\KatoCoordinates1.txt',"w")
plik = f.read()
lista = plik.split("\n")
print(lista)

PATH = "F:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver,10)
driver.maximize_window()

#otwórz Google Maps
driver.get("https://www.google.com/maps/@50.2322642,18.9995082,14.54z")

# przewiń na dół strony
driver.find_element_by_tag_name('html').send_keys(Keys.END)
time.sleep(2)
#wyłącz okno z prywatnością
wait.until(EC.presence_of_element_located((By.XPATH,'//button[@jsname="higCR"] '))).click()
print("Wyłączenie okna z prywatnością")

# przejdź do trasy
wait.until(EC.presence_of_element_located((By.XPATH,'//button[@class="xoLGzf-T3iPGc"]'))).click()

x=-1
for x in range(x+1,len(lista)):

    # od miejsca
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sb_ifc51 > input'))).clear()
    #wpisanie adresu
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#sb_ifc52 > input'))).send_keys(lista[x])
    #potwierdzenie
    #wait.until(EC.presence_of_element_located((By.XPATH,'//button[@id="xoLGzf-T3iPGc"]'))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sb_ifc51 > input'))).send_keys(Keys.ENTER)
    time.sleep(3)
    a = driver.current_url
    e = a[int(a.rfind("@"))+1:int(a.rfind("@"))+22]
    print(lista[x] +"; "+ e)
    f1.write(lista[x] +"; "+ e + '\n')
    # czyszczenie i nowy cel
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sb_ifc52 > input'))).clear()


f1.close()
f.close()

driver.quit()

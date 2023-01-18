# This creates the list of links to info pages with selenium
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re

out_file = open("links.txt","w")

URL = 'https://www.borsaitaliana.it/borsa/etf.html'
print(URL)
driver = webdriver.Firefox()
driver.implicitly_wait(2)
driver.get(URL)

accetta = driver.find_element_by_xpath("//button[@id='ccc-acceopt-all']")
accetta.click()

time.sleep(3)

successiva=driver.find_element_by_xpath("//a[@title='Successiva']")

while successiva:
    successiva=False
    driver.get(driver.current_url)
    results = driver.find_elements_by_xpath("//*[@id='tableResults']/div[1]/table/tbody/tr[*]/td[1]/a")

    data = []
    for result in results:
        link = result.get_attribute('href')
        out_file.write(f'{link}\n')
        data.append(link)
    
    print(data)
    print("---------------------------------")
    time.sleep(1)
    try:
        successiva=driver.find_element_by_xpath("//a[@title='Successiva']")
        successiva.click()
    except NoSuchElementException:
        print("Fine - tutti i link alle pagine degli ETF sono stati scritti in links.txt")
        
out_file.close()
driver.quit()

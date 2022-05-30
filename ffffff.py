# this opens the links file and puts informations in an excel file with panda
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

phrases = []

with open('links.txt') as file:
    for idx, line in enumerate(file):
        req = requests.get(line)
        
        soup = BeautifulSoup(req.text, 'lxml')

        elements = soup.find_all('td')

        words = []
        words.append(re.sub('\n+$', '',line))
        for element in elements:
            element = re.sub('\t+', '', element.get_text())
            element = re.sub(' +', ' ', element)
            element = re.sub('\n+', '', element)
            element = re.sub('\r+', '', element)
            words.append(element)

        phrases.append(words)

        print(words)
        print('------', f'{idx}','-------------------------------------------------------------')



dataframe = pd.DataFrame(data=phrases)
dataframe.to_excel('etfs.xlsx')
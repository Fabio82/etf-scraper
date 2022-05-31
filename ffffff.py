# this opens the links file and puts informations in antori  excel file with panda
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

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct




with open('links.txt') as file:
    for idx, line in enumerate(file):
        append=True

        req = requests.get(line)
        
        soup = BeautifulSoup(req.text, 'lxml')

        elements = soup.find_all('td')

        words = []
        dizionario = []

        words.append('ETF')
        words.append(re.sub('\n+$', '',line))

        for element in elements:
            element = re.sub('\t+', '', element.get_text())
            element = re.sub(' +', ' ', element)
            element = re.sub('\n+', '', element)
            element = re.sub('\r+', '', element)


            if words[len(words)-2] == 'Performance 1 anno':
                append=False
            if element =='Tipo strumento':
                append=True
            if append == True:
              words.append(element)


        dizionario = Convert(words)
        phrases.append(dizionario)

        print(words)
        print('------', f'{idx}','-------------------------------------------------------------')



dataframe = pd.DataFrame(data=phrases)
dataframe.to_excel('etfs.xlsx')
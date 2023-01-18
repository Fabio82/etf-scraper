# this opens the links file and puts informations in antori  excel file with panda
from cgitb import text
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

etfs_dataframe = []
pandas_all_dividends = pd.DataFrame([])

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

with open('links.txt') as file:
    for idx, line in enumerate(file):
        append=True

        req = requests.get(line)
        soup = BeautifulSoup(req.text, 'lxml')
        elements = soup.find_all('td')

        etf_list = []
        etf_dictionary = []

        etf_list.append('ETF')
        etf_list.append(re.sub('\n+$', '',line))

        for element in elements:
            element = re.sub('\t+', '', element.get_text())
            element = re.sub(' +', ' ', element)
            element = re.sub('\n+', '', element)
            element = re.sub('\r+', '', element)

            if etf_list[len(etf_list)-2] == 'Performance 1 anno':
                append=False
            if element =='Tipo strumento':
                append=True
            if append == True:
              etf_list.append(element)



        etf_dictionary = Convert(etf_list)
        etfs_dataframe.append(etf_dictionary)
        print(etf_list)
        print('------', f'{idx}','-------------------------------------------------------------')

        dividends_link = soup.find(href=re.compile("/borsa/etf/dividendi.html"))
        if dividends_link:
            dividends_link = 'https://www.borsaitaliana.it'+dividends_link.get('href')
            req_dividends = requests.get(dividends_link)
            soup_dividends_page = BeautifulSoup(req_dividends.text, 'lxml')
            soup_dividends_tables = soup_dividends_page.find_all('table')
            pandas_dividends = pd.read_html(str(soup_dividends_tables), decimal=',', thousands='')[0]
            pandas_dividends['etf_link'] = ' =HYPERLINK( "'+ re.sub('\n+$', '',line) + '" ; "' + etf_dictionary['Codice Isin'] + '" ) ' +' \r'
            pandas_dividends['perf1Y'] = etf_dictionary['Performance 1 anno']
            pandas_dividends['Open'] = etf_dictionary['Apertura']
            print(pandas_dividends)

            pandas_all_dividends = pd.concat([pandas_all_dividends, pandas_dividends])


dataframe = pd.DataFrame(data=etfs_dataframe)
dataframe.to_excel('etfs.xlsx')
pandas_all_dividends.to_excel('dividends.xlsx')
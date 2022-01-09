import pandas as pd

import csv

def getData():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from datetime import datetime

    driver = webdriver.Safari()

    URL0 = "https://stockanalysis.com/ipos/2019/"
    URL1 = "https://stockanalysis.com/ipos/2020/"
    URL2 = "https://stockanalysis.com/ipos/2021/"

    def mdy_to_ymd(d):
        return datetime.strptime(d, '%b %d, %Y').strftime('%Y-%m-%d')

    with open('ipos.csv', 'w', encoding='UTF8') as f:
        def getInfoIPO(URLIPO):
            header = ['dateIpo', 'ticker','ipoPrice']

            driver.get(URLIPO)
            results = []
            content = driver.page_source
            soup = BeautifulSoup(content)
            table = soup.find_all(attrs={'class': 'ipo-table'})
            rows = soup.find('tbody')
            tr = rows.find_all("tr")

            writer = csv.writer(f)
            writer.writerow(header)

            for tree in tr:
                td = tree.find_all("td")
                price = td[3].text
                price = float(price[1:])
                data = [mdy_to_ymd(td[0].text), td[1].text, price]
                print(data)
                writer.writerow(data)
        getInfoIPO(URL2)
        getInfoIPO(URL1)
        getInfoIPO(URL0)
    driver.close()

def csvInfo():
    pass


def getStockData():
    #all data points collected should be the same for all periods except for the amount of data 
    def get1w():
        #get data about the stock in period of one week
        pass
    def get1m():
        #get data about the stock in period of one month

        pass
    def get1q():
        #get data about the stock in period of one quarter

        pass
    def get1y():
        #get data about the stock in period of one year

        pass

    
getData()
print("===================================")
print("ALL OK")
print("===================================")
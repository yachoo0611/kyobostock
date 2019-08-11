import requests
from bs4 import BeautifulSoup as BS


def getStock(isbn):
    url = 'http://www.kyobobook.co.kr/prom/2013/general/StoreStockTable.jsp?barcode=' + isbn + '&ejkgb=KOR'
    res = requests.get(url)
    soup = BS(res.text, 'html.parser')
    store = soup.select('th')
    num = soup.select('a')
    stock = {}
    for i, j in zip(store, num):
        i = i.text
        i = i.strip()
        if i == '':
            pass
        else:
            stock[i] = j.text
    return stock


def bookInfo(title):
    clientId = "BsGqKYMK02FYfiAaMGCh"
    clientSecret = "FcO6DvI5Yb"
    url = "https://openapi.naver.com/v1/search/book?query=" + title + "&display=5&sort=count"
    headers = {"X-Naver-Client-Id": clientId, "X-Naver-Client-Secret": clientSecret}
    res = requests.get(url, headers=headers)
    search = res.json()
    book = search['items']
    for i in book:
        t = i['title']
        t = t.replace('<b>', '').replace('</b>', '')
        # t = t.replace('</b>', '')
        i['title'] = t
        i['isbn'] = i['isbn'][11:]
    return book

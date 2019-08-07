import requests
from bs4 import BeautifulSoup as BS

def getStock(isbn):
    try:
        url = 'http://www.kyobobook.co.kr/prom/2013/general/StoreStockTable.jsp?barcode=' + isbn + '&ejkgb=KOR'
    except:
        return ''
    res = requests.get(url)
    soup = BS(res.text, 'html.parser')
    store = soup.select('th')
    num = soup.select('a')
    kb = {}
    # stock[0] : 지점명 리스트
    # stock[1] : 재고수량 리스트
    for i, j in zip(store, num):
        i = i.text
        i = i.strip()
        if i == '':
            pass
        else:
            kb[i] = j.text
    return kb

def bookInfo(title):
    clientId = "BsGqKYMK02FYfiAaMGCh"
    clientSecret = "FcO6DvI5Yb"
    url = "https://openapi.naver.com/v1/search/book?query=" + title + "&display=5&sort=count"
    headers={"X-Naver-Client-Id":clientId, "X-Naver-Client-Secret": clientSecret}
    res = requests.get(url, headers=headers)
    resCode = res.status_code
    if resCode == 200:
        search = res.json()
        book = search['items']
        for i in book:
            i['isbn'] = i['isbn'][11:]
        return book
    else:
        print("Error Code:" + resCode)
        # res.raise_for_status()  200 아니면 오류


if __name__ == "__main__":
    title = input("도서명을 입력하세요 : ")
    book = bookInfo(title)
    print(book)
    stock = getStock(book[0]['isbn'])
    print(stock)
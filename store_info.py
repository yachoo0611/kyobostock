# coding=utf-8
import requests
from django.db import models
from django.conf import settings
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from search.models import Store
from api_engine import getStock


def getStore(s, pub):
    headers = {'Authorization': 'KakaoAK 793a3aea80b0d4afed533b515e500f9a'}
    info = ['place_name', 'road_address_name', 'phone', 'x', 'y']
    seoul = ['서울', '경기', '인천']
    stores = {}
    for i in s:
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query=' + pub + i
        res = requests.get(url, headers=headers)
        result = res.json()
        result['documents'][0]['place_name'] = i 
        stores[i] = {}
        for j in info:
            stores[i][j] = result['documents'][0][j]
            if any(a in result['documents'][0]['road_address_name'] for a in seoul):
                stores[i]['in_seoul'] = True
            else:
                stores[i]['in_seoul'] = False
            stores[i]['stock'] = 0
    print(stores)
    return stores

if __name__ == "__main__":
    store = getStock('9788936433598')
    kb = list(store.keys())
    result = getStore(kb, '교보문고')
    Store.objects.all().delete()
    n = 1
    for i in result:
        q = Store(**result[i])
        q.id = n # id를 1부터 재설정
        q.save()
        n += 1

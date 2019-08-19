# coding=utf-8
import requests
from django.db import models
from django.conf import settings
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from search.models import Store

def getStore(s, pub):
    headers = {'Authorization': 'KakaoAK 793a3aea80b0d4afed533b515e500f9a'}
    info = ['place_name', 'road_address_name', 'phone', 'x', 'y']
    seoul = ['서울', '경기', '인천']
    stores = {}
    for i in s:
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query=' + pub + i
        res = requests.get(url, headers=headers)
        result = res.json()
        stores[i] = {}
        for j in info:
            stores[i][j] = result['documents'][0][j]
            if any(a in result['documents'][0]['road_address_name'] for a in seoul):
                stores[i]['in_seoul'] = True
            else:
                stores[i]['in_seoul'] = False
    return stores

if __name__ == "__main__":
    kb = ['광화문', '가든파이브', '강남', '동대문', '디큐브', '목동', '서울대', '수유', '영등포', '은평', '이화여대', '잠실', '천호', '청량리', '합정', '가천대', '광교점', '광교월드스퀘어', '부천', '분당점', '성균관대', '송도', '인천', '일산', '판교', '평촌', '경성대ㆍ부경대', '광주상무', '대구', '대전', '반월당', '부산', '세종', '센텀시티', '울산', '전북대', '전주', '창원', '천안', '칠곡', '포항공대점', '해운대']
    result = getStore(kb, '교보문고')
    for i in result:
        q = Store(**result[i])
        q.save()
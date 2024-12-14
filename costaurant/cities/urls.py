'''
1. ''빈 문자열과 매칭되면 index뷰 호출하기
2. 문자열로 된 url이 매칭되면 문자열을 city라는 변수에 담아서 city_detail뷰를 호출하기기
'''

from django.urls import path
from . import views # view를 import

urlpatterns = [
    path('', views.index),
    path('<str:name>/', views.city_detail),
]

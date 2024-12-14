from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello) # 여기에 코드를 작성하세요
]

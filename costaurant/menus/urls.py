# costaurant/menus/urls.py
from django.urls import path
from . import views # view를 import

urlpatterns = [
    path('/menus', views.index_view),
    path('', views.index_view),# path('URL 패턴', view 함수)
]

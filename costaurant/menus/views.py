from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index_view(request):
    # return HttpResponse("<H1>menus 코스토랑 오픈!<H1>")
    today = str(datetime.now().date()) # 형식 변환하기
    context = {"today":today}
    return render(request, 'menus/index.html', context=context)

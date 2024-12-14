from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.today().date
    print("오늘은 ---> ", today)
    # 응답할 때는 무조건 dictionary 형으로 
    context = {"date":today}
    return render(request, 'foods/index.html', context=context)
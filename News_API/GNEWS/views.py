from http.client import HTTPResponse
from django.shortcuts import render
import requests
API_KEY = '540f1899cdde617624a21697bbd4f36d'
Key_word = 'IT'


# Create your views here.


def home(request):
    
    url = f'https://gnews.io/api/v4/search?q={Key_word}&token={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)

    context = {
        'data':data
    }

    return render(request,'GNEWS/home.html',context)






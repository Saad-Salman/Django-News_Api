from http.client import HTTPResponse
import mimetypes
from django.shortcuts import render
import requests
API_KEY = '540f1899cdde617624a21697bbd4f36d'
Key_word = 'IT'


# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    
    url = f'https://gnews.io/api/v4/search?q={Key_word}&token={API_KEY}&max=20'
    response = requests.get(url)
    data = response.json()['articles']
    
    return JsonResponse(data, safe=False)







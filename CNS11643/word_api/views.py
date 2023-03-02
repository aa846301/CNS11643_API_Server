from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.



def word_view(request):
    data = {'word': '你好，世界！'}
    return JsonResponse(data)
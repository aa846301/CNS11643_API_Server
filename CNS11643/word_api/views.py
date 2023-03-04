from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from word_api.models import CharMap

def word_encode(request,word):
    if len(word) == 1:
        word_uni = hex(ord(word))[2:].upper()
        char_maps = CharMap.objects.filter(unicode_code=word_uni)
        data = []
        for char_map in char_maps:
            data.append({
                'CNS':char_map.cns_code,
                'BIG5':char_map.big5_code,
                'Unicode':char_map.unicode_code,
                })
        return JsonResponse(data,safe=False)
    else:
        return HttpResponse(None)
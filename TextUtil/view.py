from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analysis(request):
    text_to_analyze=request.GET.get('text','default')
    chars=len(text_to_analyze)
    params={'no_of_characters':chars}
    return render(request,'analyzed.html',params)
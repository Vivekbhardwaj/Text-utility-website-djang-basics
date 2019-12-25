from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analysis(request):
    text_to_analyze=request.GET.get('text','default')
    cw=request.GET.get('count words','off')
    rp=request.GET.get('remove punctuations','off')
    if cw=='on' :
        chars=len(text_to_analyze)
        params={'analysis':'number of characters','ans':chars}
        return render(request,'analyzed.html',params)
    elif rp=='on' :
        punctuations='''!@#$%^&*~()__-?/""'''
        resultant_string=''
        for char in text_to_analyze : 
            if char not in punctuations :
                resultant_string=resultant_string+char
        params={'analysis':'text after removing punctuations is ','ans': resultant_string}
        return render(request,'analyzed.html',params)
    else :
        return HttpResponse('Nothing selected')
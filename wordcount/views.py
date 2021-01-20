from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    mytext=request.GET['textbox']
    mytextlist=mytext.split()
    dict={}
    for word in mytextlist:
        if word in dict:
            dict[word]=dict[word]+1
        else:
            dict[word]=1
    return render(request,'count.html',{'dict':dict.items})
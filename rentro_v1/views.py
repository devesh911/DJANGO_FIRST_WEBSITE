# i made thh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse(""" this is home page """)


def about(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/" target = "_blank" >Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)


def solution(request):
    djtext = request.POST.get('text', 'default')
    djtext = int(djtext)
    bnry = request.POST.get('binary', "off")
    deci = request.POST.get('decimal', "off")
   

    if bnry == "on":
        result = bin(djtext).replace("0b", "")
        params = {"primary": "binary", "binary_convert":result}

    elif deci == "on":
        djtext = str(djtext)
        li = list(djtext)
        value = 0
        for i in range(len(djtext)):

            digit = li.pop()
            if digit == '1':
                value = value + pow(2, i)
                djtext = value
            params = {"primary": " decimal", "decimal_convert": value}

    else:
        return HttpResponse("error")

    return render(request, 'sol.html', params)

from django.http import HttpResponse
from django.shortcuts import render


def x(request):
    return render(request, 'x.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuatuions', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charactercounter == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'Character Counted', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charactercounter != "on"):
        return HttpResponse("Please Enter Something")

    return render(request, 'analyze.html', params)

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render (request, 'contactus.html')




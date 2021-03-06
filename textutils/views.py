# I have created this file - Monita
from django.http import HttpResponse
from django.shortcuts import render

#Code for tut6

"""
def index(request):
    return HttpResponse('''hello <h1>monita</h1> <a href = "https://indianaiproduction.com/directing-customers-to-subscription-through-financial-app-behavior-analysis-ml-project/">Code with Monita</a>''')

def about(request):
    return HttpResponse("About monita")
"""

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    print(removepunc)
    print(djtext)
    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charactercounter == "on"):
        analyzed = ""
        count = 0
        for i in djtext:
            count = count + 1
            analyzed = count
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if  not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n"and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and charactercounter != "on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Please select any operation and try again!")

    return render(request, 'analyze.html', params)

# I have created this file - Keith
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('Hello World!')

# def about(request):
#     return HttpResponse('<h1>How about you?</h1>')

# def sites(request):
#     return HttpResponse('<a href="www.google.com"></a><br><a href="www.youtube.com"></a><br><a href="www.github.com"></a>')


def index(request):
    # return HttpResponse('Home')
    # params = {
    #     'name': 'Keith',
    #     'place': 'Mars'
    # }
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'off')
    # check the checkbox values
    rmvpnc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinermv = request.POST.get('newlinermv', 'off')
    spacermv = request.POST.get('rmvspace', 'off')
    countchar = request.POST.get('countchar', 'off')
    # print(djtext)
    # print(rmvpnc)
    # analze the text
    # analyzed = djtext
    # check if checkbox is on/off
    if rmvpnc == "on":
        punctuations = '''!()-[]{};:""\<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {
            'purpose': 'Remove punctuations',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        # return HttpResponse('remove punc<br><a href="/">back</a>')

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {
            'purpose': 'Change to uppercase',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlinermv == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char

        params = {
            'purpose': 'New line Character',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if spacermv == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {
            'purpose': 'Remove extra space',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if countchar == "on":
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed += 1
        params = {
            'purpose': 'Count characters',
            'analyzed_text': analyzed
        }
        # return render(request, 'analyze.html', params)

    if (rmvpnc != "on" and fullcaps != "on" and newlinermv != 'on' and spacermv != "on" and countchar != "on"):
        HttpResponse("Error - Please select any operation")

    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse('capitalize first<br><a href="/">back</a>')

# def newlineremove(request):
#     return HttpResponse('new line remove<br><a href="/">back</a>')

# def spaceremover(request):
#     return HttpResponse('space remover<br><a href="/">back</a>')

# def charcount(request):
#     return HttpResponse('char count<br><a href="/">back</a>')

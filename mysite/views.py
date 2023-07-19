# made by -Gajendra
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dict ={'name':'gajendra','place':'Gudamalani'}
    return render(request, 'index.html',dict)
    # return HttpResponse('''Home <br><a href="http://127.0.0.1:8000/analyze">Next</a> ''')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')
    print(djtext)
    #checkbox value check
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitlize','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    charactercounter = request.POST.get('charactercounter','off')

    purpose=''
    analized=djtext
    if (removepunc == "on"):
        an= ""
        punctuations='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        for char in analized:
            if char not in punctuations:
                an=an+char
        analized=an
        purpose=purpose+'Punctuation Removed '
    if(capitalize == "on"):
        an= analized.upper()
        purpose=purpose+', All letter in UPPER CASE '
        analized=an
    if(newlineremove =="on"):
        an=""
        for char in analized:
            if char !='\n'and char != '\r':
                an=an+char
        purpose=purpose+', New line Removed '
        analized=an
    if(extraspaceremove =="on"):
        an=""
        for index,char in enumerate(analized):
            if not(analized[index]==' ' and analized[index+1]==' '):
                an=an+char

        purpose=purpose+', Extra Space Removed '
        analized=an
    if(charactercounter =="on"):
        count= 0
        for char in djtext:
            count+=1

        analized= analized+'  Number of char is: '+ str(count)
        purpose=purpose+',Character Count '
    params={'purpose':purpose,'analyzed_text': analized}
    return render(request, 'analyze.html',params)

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')




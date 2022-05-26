# hello i have created this file

from django.http import HttpResponse
from django.shortcuts import render

#code for video 6 in with hello word is show in page
# def index(request):
#     return HttpResponse('''<h1>hello</h1> <br> <h2>! i am diksha</h2> <a href="https://www.onlinesbi.com/">Sbi Website<a/>''')
#
# def about(request):
#     return HttpResponse("hello ! i am Nidhi")


#code for video 7 designing pipes
def index(request):
    # params = {'name':'Diksha', 'place':'mars'}            #third argument upar bnayenge and call return render me as a third positional argument karenge
    return render(request, 'index.html')                #render pahili argument request gheto aani dusri template ch name

    # return HttpResponse('''  <button type="button"><a href="Newlineremove">Back</button></a>
    #                           <h1>Home</h1>''')

def Analyze(request):
    #get the text
    DjText = (request.POST.get('text', 'default'))

    #Checkbox value
    RemoveText = (request.POST.get('Removepunc', 'off'))

    Showpunc = (request.POST.get('showpunc', 'off'))

    Allcaps = (request.POST.get('Allcaps', 'off'))

    Newlineremover = (request.POST.get('Newlineremover', 'off'))

    Extraspaceremover =(request.POST.get('Extraspaceremover','off'))

    Countchar = (request.POST.get('Countchar', 'off'))

 #Check Which check box is on
    if RemoveText == "on":
        # *********** analyze the text ****************************
        # analyzed=DjText               #== kelyamule DJText var je pan set hot text te analyzed_text cya ithe aala
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in DjText:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose': 'removed Punctuations', 'analyzed_text': analyzed}

        DjText=analyzed
        # return render(request, 'analyze.html', param)


    if Showpunc == "on":
        # *********** analyze the text ****************************
        # analyzed=DjText               #== kelyamule DJText var je pan set hot text te analyzed_text cya ithe aala
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for punc in DjText:
            if punc in punctuations:
                analyzed = analyzed + punc
        param = {'purpose':'Show punctuations', 'analyzed_text': analyzed}

        DjText = analyzed
        # return render(request, 'analyze.html', param)

    #UPPERCASE
    if Allcaps == "on":
        analyzed =" "
        for char in DjText:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Change Text In UpperCase', 'analyzed_text': analyzed}

        DjText = analyzed
        # return render(request, 'analyze.html', param)

    #New Line Remover
    if Newlineremover == "on":
        analyzed = " "
        for char in DjText:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        param = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

        DjText = analyzed
       # return render(request, 'analyze.html', param)

   # Extra Space Remover
    if Extraspaceremover == "on":
        analyzed = " "
        for index,char in enumerate(DjText):
            if not (DjText[index] == " " and DjText[index + 1]==" "):
                analyzed = analyzed + char
        param = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}

        DjText = analyzed
        # return render(request, 'analyze.html', param)

    # Char Count
    if Countchar == "on":
        analyzed =""
        for char in DjText:
            analyzed = "total char:"+str(len(DjText))
        param = {'purpose': 'Change Text In UpperCase', 'analyzed_text': analyzed}

    if (RemoveText != 'on' and Showpunc != 'on' and Allcaps !='on' and Newlineremover !='on' and Extraspaceremover !='on' and Countchar !='on'):
        return HttpResponse("AAP ne koi text Select nahi kiya !! Please select operater")

    # else:
    #     return HttpResponse("Gadbad bai bhai !!")
    return render(request, 'analyze.html', param)




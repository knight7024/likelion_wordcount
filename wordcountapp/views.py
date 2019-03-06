from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wordcountapp/index.html')

def count(request):
    full_text = request.GET['fulltext']
    split_full_text = full_text.split()
    dic_full_text = {}
    for word in split_full_text:
        if word in dic_full_text: dic_full_text[word] += 1
        else: dic_full_text[word] = 1
    return render(request, 'wordcountapp/count.html', { 'fulltext': full_text, 'countfulltext': len(split_full_text), 'dicfulltext': dic_full_text })
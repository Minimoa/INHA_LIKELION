from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import Word
from django.core.paginator import Paginator
# Create your views here.

def home(req):  
    words = Word.objects.all().order_by('-id') 
    keyword = req.GET.get('search')
    if keyword is not None:
            words = Word.objects.filter(title__contains=keyword)
    
    paginator = Paginator(words,5) 
    page = req.GET.get('page')
    page_posts = paginator.get_page(page)

    print(words)
    return render(req,'index.html',{'page_posts':page_posts,'words':words}) 

    #return render(req, 'index.html', {'words' : words})

def detail(req, word_id):
    word = get_object_or_404(Word, id = word_id) # get_object_or_404(Word, pk = word_id)
    return render(req, 'detail.html', {'word' : word})

def delete(req, word_id):
    word = get_object_or_404(Word, id = word_id)
    word.delete()
    return redirect('/')

def new(req):
    return render(req, 'new.html')

def create(req):
    word = Word()
    word.title = req.POST['title']
    word.writer = req.POST['writer']
    word.content = req.POST['content']
    word.save()
    return redirect('/') #redirect('/word/'+str(word_id))

def edit(req, word_id):
    word = get_object_or_404(Word, id = word_id)
    return render(req, 'edit.html', {'word' : word})

def update(req,word_id):
    word = get_object_or_404(Word, id = word_id)
    word.title = req.POST['title']
    word.writer = req.POST['writer']
    word.content = req.POST['content']
    word.save()
    return redirect('/') #redirect('/word/'+str(word_id))

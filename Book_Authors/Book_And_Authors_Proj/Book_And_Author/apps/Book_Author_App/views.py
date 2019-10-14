
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    all_books = Book.objects.all()
    context ={
        'all_books': all_books
    }
    
    return render (request, 'index.html', context)

def NewBook (request):
    # print(request.POST['title'])
    if len(request.POST['title']) > 1 and len(request.POST['desc']) > 5 :
        Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    else:
        messages.add_message(request, messages.INFO, "Book Added!")
    return redirect('/')

def ShowBook (request, number):
    book = Book.objects.get(id=int(number))
    book_authors = book.authors.all()
    all_authors = Author.objects.all()
    context = {
        'book' : book,
        'book_authors': book_authors,
        'all_authors' : all_authors
    }
    return render(request, "bookinfo.html", context)

def RemoveBook(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/')

def removeauthor(request,id):
    author = Author.objects.get(id =id)
    author.delete()
    return redirect ('/viewauthors')

def newauthor (request):
    if len(request.POST['first_name']) > 1 and len(request.POST['last_name']) > 1 and len(request.POST['note']) > 1:
        Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['note'])
    else:
        messages.add_message(request, messages.INFO, "Author Added!")
    return redirect('/')


def ShowAuthor (request):
    all_authors = Author.objects.all()
    context = {
        "all_authors" : all_authors
    }
    return render(request, "viewauthor.html", context)

def viewauthor (request, id):
    author = Author.objects.get(id=id)
    all_authors = Author.objects.all()
    all_books = Book.objects.all()
    context = {
        'author' : author,
        'all_authors' : all_authors,
        'all_books': all_books
    }
    return render( request, 'authorsinfo.html', context)

def addbook(request, id):
    author_id = id
    add_book_id = int(request.POST['bookid'])

    c = Author.objects.get(id = author_id)
    d = Book.objects.get(id= add_book_id)
    c.books.add(d)
    return redirect (f'/author_info/{id}')
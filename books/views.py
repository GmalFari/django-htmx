from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Books,Author
from .forms import BookForm, BookFormSet
# Create your views here.


def create_book(request,pk):
    author = Author.objects.get(pk=pk )
    form = BookForm(request.POST or None)
    books = Books.objects.filter(author=author)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False) 
            book.author = author
            book.save()
            return redirect("book-detail",pk=book.id)
        else:
            return render(request,"books/partials/book_form.html",{
            "form":form
        })

    context = {
        "formset":form,
        "author":author,
        "books":books
    }
    return render(request,"books/create_book.html",context=context)
def create_book_form(request):
    context = {
        "form":BookForm()
    }
    return render(request,"books/partials/book_form.html",context=context)

def update_book(request,pk):
    book = Books.objects.get(id=pk)
    form = BookForm(request.POST or None , instance=book)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save() 
            book.save()
            return redirect("book-detail",pk=book.id)
    context = {
    "form":form,
    "book":book
}
    return render(request,"books/partials/book_form.html",context=context)
def detail_book(request,pk):
    book = Books.objects.get(id=pk)
    context = {
        "book":book
    }
    
    return render(request,"books/partials/book_detail.html",context=context)
def delete_book(request,pk):
    book = Books.objects.get(pk=pk)
    book.delete()
    return HttpResponse(' ')
    
    





 
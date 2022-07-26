
from django.shortcuts import render

from AppProyectoFinalPython.models import Contact, Book, Author
from AppProyectoFinalPython.forms import ContactFormulario, BookForm, AuthorForm

def inicio(self):
    return render(self, "inicio.html")

def contactUs(self):
    
    if (self.method == 'POST'):
        contactFormulario = ContactFormulario(self.POST)
        print(contactFormulario.is_valid())
        print(self.POST)
        if contactFormulario.is_valid():
            data = contactFormulario.cleaned_data
            contact = Contact(name=data['name'], email=data['email'], phone=data['phone'], message=data['message'])
            contact.save()
            return render(self,'inicio.html')
    else:
        
        return render(self, "contactUs.html")

def books(self):
    
    if (self.method == 'POST'):
        bookForm = BookForm(self.POST)
        print(bookForm.is_valid())
        print(self.POST)
        if bookForm.is_valid():
            data = bookForm.cleaned_data
            book = Book(name=data['name'], author=data['author'], genre=data['genre'], date=data['date'])
            book.save()
            return render(self,'inicio.html')
    else:
        
        return render(self, "books.html")

def authors(self):
    
    if (self.method == 'POST'):
        authorForm = AuthorForm(self.POST)
        print(authorForm.is_valid())
        print(self.POST)
        if authorForm.is_valid():
            data = authorForm.cleaned_data
            author = Author(name=data['name'], last_name=data['last_name'], born=data['born'])
            author.save()
            return render(self,'inicio.html')
    else:
        
        return render(self, "authors.html")
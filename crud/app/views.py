from django.shortcuts import render, HttpResponseRedirect  #inport user data for validation and sending data to db 
from .forms import BookAddition
from .models import bookDetails       

# Create your views here.

def index(request):
    if request.method == 'POST':    #checks if request is POST
        formFields = BookAddition(request.POST)                            #object creation 
        if formFields.is_valid():                                                 #validate
            name = formFields.cleaned_data['name']                                #find form data
            author = formFields.cleaned_data['author']
            ISBN = formFields.cleaned_data['ISBN']
            registeration = bookDetails(name = name, author = author, ISBN = ISBN) # form field value assignment
            registeration.save()                                                  #insert data into db
        formFields = BookAddition()
    else:
        formFields = BookAddition() #if request is GET then show form fields blank
    stud = bookDetails.objects.all()
    return render(request, 'addandshow.html', {'form':formFields,'stud':stud })

# function to delete row
def deleteBook(request, id):
    if request.method == 'POST':
        dataDelete = bookDetails.objects.get(pk=id)
        dataDelete.delete()
        return HttpResponseRedirect('/app')                #to redirect home page with dynamic url

# fucntion to update data

def updateBook(request, id):                                #get request with id
    if request.method == 'POST':                                    #method check if POST
        formData = bookDetails.objects.get(pk=id)                          #primary key to get data
        formBook = BookAddition(request.POST, instance = formData) #instance creation for taking data to form fields
        if formBook.is_valid():                                         #validate
            formBook.save()                                             #update the data
    else:
        formData = bookDetails.objects.get(pk=id)
        formBook = BookAddition(instance = formData)
    return render(request, 'update.html', {'formBook':formBook})        #render on url with key value data.
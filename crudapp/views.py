from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save() That's the direct method we can submit data without add any objects
            #This is the second way to create object and cleaned data and submit data to the database
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pm)
            reg.save()
            messages.success(request, "Your Details has been Submitted.")
            # It refresh the form and show the form empty
            fm = StudentRegistration() 
    else:
        fm = StudentRegistration()
    show = User.objects.all()    
    return render(request,'index.html',{'form':fm, 'show':show})
    

def delete_data(request, id):
    if request.method == 'POST':
        delete = User.objects.get(pk=id)  #pk means primary key
        delete.delete()
        messages.info(request, "Delete Successfully.")
        return redirect('/')


def update_data(request, id):
    if request.method == 'POST':
        edit = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=edit)
        if fm.is_valid():
            fm.save()
        messages.info(request, "Update Successfully.")

    else:
        edit = User.objects.get(pk=id)
        fm = StudentRegistration(instance=edit)
    return render(request, 'update.html', {'form':fm})
    return redirect('/')




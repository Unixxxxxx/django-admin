from django.shortcuts import render 
from .forms import ContactForm, NewForm , AlpahForm
from .models import Contact, new
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello Swagger!"})


def index(request):
    return render(request,'index.html',{} )

def home(request):
    return render(request,'home.html',{})

def menu(request):
    return render(request, 'menu.html', {})

def about(request):
    return render(request,'about.html',{})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'success.html', {"name": name})
    else:
        form = ContactForm()


    return render(request, 'contact.html', {"form": form})

def new_form_view(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = NewForm()
    return render(request, 'new/new_form.html', {'form': form})

def success_view(request):
    return render(request, 'new/success.html')


def alpha_form(request):
    if request.method == 'POST':
        form =NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alpsuccess')
        else:
            form = NewForm()
        return render=(request, 'alpha.html')

def alpha_views(request):
    return render(request, 'alpsuccess')

from django.shortcuts import render 
from .forms import ContactForm 
from .models import Contact
from .models import Blog

# Create your views here.

def index(request):
    return render(request,'index.html',{} )

def home(request):
    return render(request,'home.html',{})

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

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

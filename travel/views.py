# travel/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import QuoteRequestForm

def get_quote(request):
    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Your request has been submitted!"})
        return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = QuoteRequestForm()
    return render(request, "travel/get_quote.html", {"form": form})


def home(request):
    form = QuoteRequestForm()
    return render(request, "index.html", {"form": form})

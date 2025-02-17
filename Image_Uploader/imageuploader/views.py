from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'home.html', {'form': form, 'img':img})


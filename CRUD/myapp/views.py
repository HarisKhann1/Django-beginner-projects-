from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import imgForm
from .models import img

# Create your views here.
def hello(request,pk):
    return HttpResponse(f'<h1> Hello World! {pk} </h1>')

def create_view(request):
    form = imgForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': form}

    return render(request, 'create_view.html', context)

def list_view(request):
    items = img.objects.all()
    context = {'items':items}
    return render(request, 'list_view.html', context)

def single_view(request, pk=None):
    if id:
        item = img.objects.get(pk=pk)
    else:
        item = ''

    context = {'item': item}
    return render(request, 'single_view.html', context)

def edit(request, pk=None):
    if pk:
        obj = img.objects.get(pk = pk)
    else:
        obj = ''

    context = {'obj': obj}
    return render(request, 'update.html', context)
    

# def update(request, id):  
#     obj = img.objects.get(id=id)  
#     print('dfdfdfdf',obj.id,obj.img_name, obj.img_desc)
#     form = imgForm(request.POST, instance = obj)  
#     if form.is_valid():  
#         form.save()  
#         # return redirect("/view")  
#     context = {'obj': obj}
#     # return render(request, 'update.html', context)
#     return render(request, 'update.html', context)


def update(request, id=None):
    obj = img.objects.get(id = id)
    if request.method == 'POST':
        obj.img_name = request.POST.get('name')
        obj.img_desc = request.POST.get('desc')

        obj.save()

        return redirect('/view')
    
def deleteView(request, pk=None):
    if pk:
        obj = img.objects.get(pk = pk)
        obj.delete()

    return redirect('/view')

























    
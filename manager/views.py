from django.shortcuts import render, redirect
from manager.models import foodProducts
from .forms import addItemForm

def home(request):
    item = foodProducts.objects.all()
    item_count = item.count()
    return render(request, 'manager/main.html', {'itemList': item, 'item_count': item_count})

def addItem(request):
    form = addItemForm() #oten
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = addItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'manager/add_item.html', context)

def updateItem(request, pk):
    item = foodProducts.objects.get(id=pk)
    form = addItemForm(instance=item)
    
    if request.method == 'POST':
        form = addItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'manager/add_item.html', {'form': form})

def deleteItem(request, pk):
    item = foodProducts.objects.get(id=pk)
    item.delete()

    return redirect('home')

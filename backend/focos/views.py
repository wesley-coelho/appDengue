from django.shortcuts import render, redirect
from .forms import FocoForm

def adicionar_foco(request):
    if request.method == 'POST':
        form = FocoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FocoForm()
    return render(request, 'addFoco.html', {'form': form})

def index(request):
    return render(request, 'index.html')

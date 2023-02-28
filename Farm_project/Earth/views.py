from django.shortcuts import render
from .models import DataVegetables
from .forms import MyForm




def addVeg(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request,"Earth/form/getVeg.html",{'form':form})


def main_page(request):
    return render(request,'Earth/main/index.html')    


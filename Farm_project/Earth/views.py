from django.shortcuts import render
from .models import DataVegetables, Vegetables
from .forms import MyForm


def show_test(request):
    name_saler = Vegetables.objects.filter(user__First_name='Vladislav')
    return render(request,'Earth/show.html',{'name':name_saler})


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


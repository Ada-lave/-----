from django.shortcuts import render
from .models import DataVegetables
from .forms import MyForm

def showDataBase(request):
    vegetables = DataVegetables.objects.all()
    return render(request,'Earth/page.html',{'data':vegetables})


def addVeg(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request,"Earth/getVeg.html",{'form':form})
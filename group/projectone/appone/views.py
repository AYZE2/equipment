from django.shortcuts import render, redirect
from .models import Item
from .forms import CreateItemForm, ItemForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.



def home(request):
    item = Item.objects.all()
    context = {'item':item}
    return render(request, 'appone/home.html',context)



@login_required
def Blist(request, id ):
    listitem = Item.objects.get(id=id)

    if request.method == 'POST':
        form =ItemForm(request.POST, instance=listitem)
        if form.is_valid():
            listitem.save()
            return redirect('homepage')
    else:
            form= ItemForm(instance=listitem)    
    context ={'listitem':listitem,'form': form}
    return render(request, 'appone/Blist.html', context)
 
@login_required
def createItem(request):
    if request.method == "POST":
        form = CreateItemForm(request.POST)
        if form.is_valid():item = form.save()
        return redirect("homepage")
    else:
        form = CreateItemForm()
        return render(request, "appone/createitem.html", {"form": form})
    

def deleteItem(request,id):
     item=Item.objects.get(id=id)
     if request.method == "POST":
          item.delete()
          return redirect('homepage')
     return render(request, 'appone/deleteitem.html',{'item':item})

def register(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}!')
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request,'appone/register.html',{'form':form})
            

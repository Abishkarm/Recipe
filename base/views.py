import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.template import loader
from .models import Recipe
# Create your views here.
def home(request):
   Recipe_objs=Recipe.objects.all()
   content={'Recipes':Recipe_objs}
   return render( request,'index.html',context=content)

def create(request):
    if request.method=="POST":
        picture=request.FILES.get('picture')
        name=request.POST.get('name')
        category=request.POST.get('category')
        ingredients=request.POST.get('ingredients')
        description=request.POST.get('description')
        process=request.POST.get('process')
        Recipe.objects.create(name=name,category=category, ingredients=ingredients,description=description,process=process,picture=picture)
        return redirect('home')
    return render(request,'create.html')

def edit(request, pk):
    Recipe_obj=Recipe.objects.get(id=pk)
    pic=Recipe_obj.picture
    content={'Recipe':Recipe_obj}
    if request.method=="POST":
        Recipe_obj.picture=request.FILES.get('picture')
        Recipe_obj.name=request.POST.get('name')
        Recipe_obj.category=request.POST.get('category')
        Recipe_obj.ingredients=request.POST.get('ingredients')
        Recipe_obj.description=request.POST.get('description')
        Recipe_obj.process=request.POST.get('process')
        if Recipe_obj.picture == None:
            Recipe_obj.picture=pic
            Recipe_obj.save()
        else:
            try:
                os.remove(f'media/{pic}')
            except Exception:
                pass
            # 
            Recipe_obj.save()


        return redirect('home')    
    return render(request, 'edit.html',context=content)

def delete(request,pk):
    delete_recipe=Recipe.objects.get(id=pk)
    pic=delete_recipe.picture
    try:
        os.remove(f'media/{pic}')
    except Exception:
        pass
    delete_recipe.delete()
    return redirect('home')

def details(request,pk):
    Recipe_obj=Recipe.objects.get(id=pk)
    content={'Recipe':Recipe_obj}
    return render(request, 'details.html',context=content)
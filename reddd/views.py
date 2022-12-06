from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)     # TTL - Time to live


# def get_recipe(filter_recipe = None):
#     if filter_recipe: 
#         print("DATA COMING FROM DB")
        
#         recipes = Recipe.objects.filter(name__contains = filter_recipe)
#     else:
#         recipes = Recipe.objects.all()
#     return recipes


# def home(request):
    
#     filter_recipe = request.GET.get('recipe')
#     if cache.get(filter_recipe):
#         # print(cache.ttl("filter_recipe"))
#         print("DATA COMING FROM CACHE")
#         recipe = cache.get(filter_recipe)
#     else:
#         if filter_recipe:
#             recipe = get_recipe(filter_recipe)
#             cache.set(filter_recipe, recipe)
#         else:
#             recipe = get_recipe()
        
#     context = {'recipe': recipe}
#     return render(request, 'home.html' , context)

# def show(request , id):
#     if cache.get(id):
#         print("DATA COMING FROM CACHE")
#         recipe = cache.get(id)
#     else:
#         print("DATA COMING FROM DB")

#         recipe = Recipe.objects.get(id = id)
#         cache.set(id , recipe)
#     context = {'recipe' : recipe}
#     return render(request, 'show.html' , context)



class RecipeCreate(CreateView):
    model = Recipe
    fields = "__all__"

    def form_valid(self,form):
        form.save()
        return redirect('reddd:recipecreate')

class RecipeList(ListView):
    model = Recipe
    template_name = 'reddd/recipe_list.html'

class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'reddd/recipe_detail.html'

    def get(self,request, *args, **kwargs):
        recipe_id = kwargs['pk']
        # if data is present in cache then data will be shown from the cache 
        if cache.get(recipe_id):
            print("CACHE_TTL - ",cache.ttl(recipe_id))
            recipe = cache.get(recipe_id)
            print('--------------DATA COMING FROM CACHE------------')

        # if not present in cache then data will be shown from db and it will be added to cache    
        else:
            recipe =Recipe.objects.get(pk = recipe_id)
            cache.set(recipe_id,recipe)
            print('--------------DATA COMING FROM DB------------')
        context = {'recipe':recipe}
        return render( request, self.template_name,context)


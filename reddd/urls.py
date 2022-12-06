from django.urls import path
from django.views import View
from reddd import views
from .views import *

app_name="reddd"

urlpatterns = [
    # path('',home , name='home'),
    # path('<int:id>',show , name='show'),
    path('',views.RecipeList.as_view(), name='recipelist'),
    path('detail/<int:pk>/',views.RecipeDetail.as_view(), name='recipedetail'),
    path('create',views.RecipeCreate.as_view(), name='recipecreate')
]
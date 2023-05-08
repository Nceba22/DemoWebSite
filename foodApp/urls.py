from django.urls import path
from . import views

#namespacing urls
app_name= "foodApp"
urlpatterns = [
    path('', views.index, name='index'),
    #/foodapp/1
    path('<int:item_id>/', views.detail, name= 'detail'),
    path('item', views.item, name='item')
]
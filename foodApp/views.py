from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    #template = loader.get_template('foodApp/index.html')
    context ={
        'item_list':item_list

    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'foodApp/index.html', context)
    

def item(request):
    return HttpResponse('<h1>Items of the food</h1>')

def detail(request, item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    #return HttpResponse("Item id: %s" % item_id)
    return render(request, 'foodApp/detail.html',context)
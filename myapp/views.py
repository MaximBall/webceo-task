from django.shortcuts import render
from .models import Item
from django.views.generic import View

class ItemListView(View):
    
    def get(self, request):

        items = Item.objects.all()
        context = {"items": items}
        return render(request, "item_list.html", context)

class BuyView(View):

    def get(self, request, name):

        # item = Item.objects.first(name=name)
        items = Item.objects.filter(name=name)
        context = {"items": items, "name": name}
        return render(request, "buy_item.html", context)
        

    def post(self, request, name):
        pass

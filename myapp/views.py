from django.shortcuts import render
from .models import Item
from django.views.generic import View

class ItemListView(View):
    
    def get(self, request):

        items = Item.objects.all()
        context = {"items": items}
        return render(request, "item_list.html", context)

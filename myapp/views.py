from annoying.decorators import render_to
from .models import Item


@render_to('item_list.html')
def item_list(request):
    items = Item.objects.all()
    return {'items': items}

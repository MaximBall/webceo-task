from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ItemListView, BuyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', ItemListView.as_view(), name='item_list'),
    path('buy/<str:name>', BuyView.as_view(), name='buy_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ItemListView, LoginView, SaleListView, HistoryPriceView, BuyViewCreate

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', ItemListView.as_view(), name='item_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('sales/', SaleListView.as_view(), name='sales_list'),
    path('history/', HistoryPriceView.as_view(), name='history_price'),

    path('sale/new/', BuyViewCreate.as_view(), name='sale_new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
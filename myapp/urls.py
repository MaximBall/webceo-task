from django.contrib import admin
from django.urls import path
from .views import ItemListView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', ItemListView.as_view(), name='item_list')
]
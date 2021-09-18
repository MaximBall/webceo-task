from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.item_list, name='item_list'),
]

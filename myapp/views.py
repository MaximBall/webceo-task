from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.utils.html import DOTS
from .models import Employee, Item, Sale, ChangePrice
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm


@receiver(post_save, sender = Item)
def change_price_item(instance, **kwargs):
    ChangePrice.objects.create(
        item = instance,
        price = instance.price
    )


class ItemListView(View):
    
    def get(self, request):

        items = Item.objects.all()
        context = {"items": items}
        return render(request, "item_list.html", context)

class SaleListView(LoginRequiredMixin, View):
    
    def get(self, request):

        sales = Sale.objects.order_by('-date_sale')

        sales_paginator = Paginator(sales, 5)

        page_num = request.GET.get('page')

        page = sales_paginator.get_page(page_num)

        context = {"page": page}
        return render(request, "sales_list.html", context)

class BuyViewCreate(CreateView):
    model = Sale
    template_name = 'buy_item.html'
    fields = ['item', 'count']


class LoginView(View):

    def get(self, request):
        try:
            logout(request)
            form = AuthenticationForm(request)
            context = {"form": form}
            return render(request, "login.html", context)
        except KeyError:
            form = AuthenticationForm(request)
            context = {"form": form}
            return render(request, "login.html", context)
        
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = AuthenticationForm(request)
            message = 'Username or password is not valid'
            context = {'message': message, 'form': form}
            return render(request, "login.html", context)

class HistoryPriceView(LoginRequiredMixin, TemplateView):

    template_name = "history_price.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prices'] = ChangePrice.objects.all()
        return context
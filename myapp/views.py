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
from django.views.generic.edit import FormView


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

class SaleListView(LoginRequiredMixin, TemplateView):
    
    template_name = 'sales_list.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        sales = Sale.objects.order_by('-date_sale')
        sales_paginator = Paginator(sales, 5)
        page_num = self.request.GET.get('page')
        context['page']=sales_paginator.get_page(page_num)
        return context
        
class BuyViewCreate(CreateView):
    model = Sale
    template_name = 'buy_item.html'
    fields = ['item', 'count']


class LoginView(FormView):

    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    def get_initial(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        else: pass

    def form_valid(self, form):
        if form.is_valid():
            user = form.get_user()
            login(self.request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')

class HistoryPriceView(LoginRequiredMixin, TemplateView):

    template_name = "history_price.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prices'] = ChangePrice.objects.all()
        return context
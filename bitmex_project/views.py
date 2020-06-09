import django
from django.conf import settings
from django.urls.base import reverse
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

from orders.models import Order, Account


class HomeView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse('main')
        else:
            return reverse('login')


class MainView(ListView):
    template_name = 'main.html'

    def get_queryset(self):
        return Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['title'] = "Welcome to bitmex!"
        return context


class AccountCreate(CreateView):
    template_name = 'orders/create_account.html'
    model = Account
    fields = ['name', 'test_exchange', 'api_key', 'api_secret']

    def get_context_data(self, **kwargs):
        context = super(AccountCreate, self).get_context_data(**kwargs)
        context['accounts'] = Account.objects.all()
        return context

    def get_success_url(self):
        return reverse('create_account')

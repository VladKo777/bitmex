from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import HomeView, MainView, AccountCreate
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('main/', MainView.as_view(), name='main'),
    path('create_account/', AccountCreate.as_view(), name='create_account'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),
]

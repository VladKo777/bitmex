from django.urls import path, include
from . import views

app_name = "orders"

urlpatterns = [
    path('', include('orders.api.urls')),
    path('websoket/', views.index, name='index'),
    path('websoket/<str:room_name>/', views.room, name='room'),
]
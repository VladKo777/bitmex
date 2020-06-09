from django.urls import path
from .views import GetOrderView, OrdersView, WebsoketView


urlpatterns = [
    path('orders/', OrdersView.as_view(), name='get_orders'),
    path('orders/<str:order_id>/', GetOrderView.as_view(), name='get_order'),
    path('subscribe/', WebsoketView.as_view(), name='websoket_subscribe'),
]

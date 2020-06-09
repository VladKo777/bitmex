from rest_framework.response import Response
from rest_framework.views import APIView
from orders.api.bitmex_api import get_orders, get_order_by_id, delete_orders, create_order
from orders.models import Order, Account
from orders.views import ws_auth
from .serializer import CreateOrderSerializer, GetOrders, GetAccount, Subscribe
from django.shortcuts import get_object_or_404


class WebsoketView(APIView):

    def post(self, request):
        data = request.data
        # {"account": "Ksenia", "action": "subscribe"}
        serializer = Subscribe(data=data)
        if serializer.is_valid(raise_exception=True):
            account_name = data.get("account")
            account = get_object_or_404(Account, name=account_name)
            action = data.get('action')
            if action == "subscribe":
                data = ws_auth(account)
        return Response(data)


class GetOrderView(APIView):

    def get(self, request, order_id):
        data = request.data
        serializer = GetAccount(data=data)
        if serializer.is_valid(raise_exception=True):
            account_name = data.get("account")
            account = get_object_or_404(Account, name=account_name)
            data, status = get_order_by_id(account, order_id)
        return Response(data, status=status.status_code)

    def delete(self, request, order_id):
        data = request.data
        serializer = GetAccount(data=data)
        if serializer.is_valid(raise_exception=True):
            account_name = data.get("account")
            account = get_object_or_404(Account, name=account_name)
            data, status = delete_orders(account, order_id)
            return Response(data, status=status.status_code)


class OrdersView(APIView):

    def get(self, request):
        # Example: {"account": "Ksenia", "symbol": "XBTUSD", "ord_status":"Filled"}
        data = request.data
        serializer = GetOrders(data=data)
        if serializer.is_valid(raise_exception=True):
            account_name = data.get("account")
            symbol = data.get("symbol")
            ord_status = data.get("ord_status")
            account = get_object_or_404(Account, name=account_name)
            data, status = get_orders(account, symbol, ord_status)
            return Response(data, status=status.status_code)

    def post(self, request):
        data = request.data
        serializer = CreateOrderSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            account_name = data.get("account")
            account = get_object_or_404(Account, name=account_name)
            symbol = data.get('symbol')
            order_type = data.get('ordType')
            order_qty = data.get('orderQty')
            side = data.get('side')
            data, status = create_order(account, symbol, order_type, order_qty, side)
            if str(status) == "200 OK":
                Order.objects.create(
                    order_id=data['orderID'],
                    symbol=data['symbol'],
                    volume=data['orderQty'],
                    order_type=data['ordType'],
                    side=data['side'],
                    price=data['price'],
                    account=account,
                )
            return Response(data, status=status.status_code)

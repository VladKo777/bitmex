import bitmex
import json


def get_client(account):
    return bitmex.bitmex(test=account.test_exchange, api_key=account.api_key, api_secret=account.api_secret)


def get_orders(account, symbol='XBTUSD', ord_status=None):
    client = get_client(account)
    if ord_status:
        result = client.Order.Order_getOrders(symbol=symbol, filter=json.dumps({'ordStatus': ord_status}),
                                              reverse=True).result()
    else:
        result = client.Order.Order_getOrders(symbol=symbol, reverse=True).result()
    return result


def get_order_by_id(account, order_id):
    client = get_client(account)
    result = client.Order.Order_getOrders(filter=json.dumps({'orderID': order_id}), reverse=True).result()
    return result


def delete_orders(account, order_id):
    client = get_client(account)
    result = client.Order.Order_cancel(orderID=order_id).result()
    return result


def create_order(account, symbol, order_type, order_qty, side):
    if side == "sell":
        order_qty *= -1
    client = get_client(account)
    result = client.Order.Order_new(symbol=symbol, ordType=order_type, orderQty=order_qty).result()
    return result

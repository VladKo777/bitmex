from django.shortcuts import render
from bitmex_websocket import BitMEXWebsocket


def ws_auth(account):
    ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                         api_key=account.api_key, api_secret=account.api_secret)
    dict_data = ws.get_instrument()
    dict_response = dict([[k, v] for k, v in dict_data.items() if k in ('timestamp', 'symbol', 'lastPrice')])
    dict_response['account'] = account.name
    return dict_response


def index(request):
    return render(request, 'orders/index.html')


def room(request, room_name):
    return render(request, 'orders/room.html', {
        'room_name': room_name
    })



import requests

from django.db import transaction
from django.utils import timezone

from .models import Stock, Player, PlayerStock


def fetch_quotes(symbols):
    """Fetch stock prices from list of symbols"""

    quotes = {}
    query_string = ','.join(symbols)
    link = "https://api.iextrading.com/1.0/stock/market/batch?symbols={}&types=quote".format(query_string)  # noqa
    # print(link)

    try:
        response = requests.get(link)
    except:
        return None
    if response.status_code != 200:
        return None

    data = response.json()
    for stock in data:
        quotes[stock] = data[stock]['quote']

    return quotes


@transaction.atomic
def update_all_stock_prices():
    all_stocks = Stock.objects.all()
    symbol_list = [s.code for s in all_stocks]
    quotes = fetch_quotes(symbol_list)
    for stock in all_stocks:
        stock.price = quotes[stock.code]['latestPrice']
        stock.diff = quotes[stock.code]['change']
        stock.last_updated = timezone.now()
        stock.save()


@transaction.atomic
def update_all_player_assets():
    all_players = Player.objects.all()
    for player in all_players:
        playerObj = Player.objects.select_for_update().filter(
            user=player.user)[0]
        playerObj.value_in_stocks = 0
        for j in PlayerStock.objects.select_for_update().filter(player=playerObj):  # noqa
            playerObj.value_in_stocks += j.stock.price * j.quantity
        playerObj.save()
        print("updated ", playerObj)

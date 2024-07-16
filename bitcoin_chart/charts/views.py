# charts/views.py
import requests
from django.http import JsonResponse
from django.shortcuts import render

def get_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    data = response.json()
    return data['bpi']['USD']['rate_float']


def bitcoin_chart(request):
    return render(request, 'charts/bitcoin_chart.html')

def bitcoin_price_data(request):
    price = get_bitcoin_price()
    return JsonResponse({'price': price})

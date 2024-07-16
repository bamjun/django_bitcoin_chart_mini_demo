from django.urls import path
from .views import bitcoin_chart, bitcoin_price_data

urlpatterns = [
    path('', bitcoin_chart, name='bitcoin_chart'),
    path('bitcoin-price-data/', bitcoin_price_data, name='bitcoin_price_data'),
]

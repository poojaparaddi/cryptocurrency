from celery import shared_task
from .utils import get_crypto_data
@shared_task
def scrape_coin_data(coin):
    data = get_crypto_data(coin)
    return {coin: data}
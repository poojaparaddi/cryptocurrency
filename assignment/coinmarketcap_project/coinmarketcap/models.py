

from django.db import models
class CryptoData(models.Model):
    coin = models.CharField(max_length=50)
    price = models.FloatField()
    price_change = models.FloatField()
    market_cap = models.BigIntegerField()
    market_cap_rank = models.IntegerField()
    volume = models.BigIntegerField()
    volume_rank = models.IntegerField()
    volume_change = models.FloatField()
    circulating_supply = models.BigIntegerField()
    total_supply = models.BigIntegerField()
    diluted_market_cap = models.BigIntegerField()
    contracts = models.JSONField()
    official_links = models.JSONField()
    socials = models.JSONField()

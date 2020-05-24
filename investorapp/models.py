from django.db import models

class Stock(models.Model):

    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10,unique=True)
    closing_price = models.DecimalField(decimal_places=2,max_digits=10)

class Broker(models.Model):

    name = models.CharField(max_length=100)
    minimum_fee = models.DecimalField(decimal_places=2,max_digits=10)
    trading_fee = models.DecimalField(decimal_places=2,max_digits=10)

class Transaction(models.Model):

    order_type = models.PositiveSmallIntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity = models.IntegerField()
    txn_date = models.IntegerField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
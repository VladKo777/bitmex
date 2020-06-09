from django.db import models, transaction

TEST_EXCHANGE = True
API_KEY = "zGg4Rjf7Zux5GVZeIyztIS08"
API_SECRET = "zp0q9021mh9IktGUCfj81iSp44xTOodd5JKtCndd4ssUd_kM"


class Account(models.Model):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    name = models.CharField(max_length=255, blank=True, null=True, default=None, unique=True, verbose_name='Name')
    test_exchange = models.BooleanField(default=True, verbose_name='TEST_EXCHANGE')
    api_key = models.CharField(max_length=255, blank=True, null=True, default=None, unique=True, verbose_name='API_KEY')
    api_secret = models.CharField(max_length=255, blank=True, null=True, default=None, unique=True,
                                  verbose_name='API_SECRET')

    def __str__(self):
        return "{}, test_exchange:{}".format(self.name, self.test_exchange)


class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    STATUSES = (
        ('buy', 'Buy order'),
        ('sell', 'Sell order'),
    )

    order_id = models.CharField(max_length=50, blank=True, null=True, default=None, unique=True, verbose_name='orderID')
    symbol = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='symbol')
    volume = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='volume')
    order_type = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name='order_type')
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Create date')
    side = models.CharField(max_length=15, choices=STATUSES, default="sell")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return "{} {} - ({} {})".format(self.account, self.volume, self.price, self.symbol)

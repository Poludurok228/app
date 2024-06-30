from django.db import models
from django.contrib.auth import get_user_model
from cat.models import Asic
from django.urls import reverse


User = get_user_model()


class WalletUSDT(models.Model):
    title = models.CharField(verbose_name='Название сети, например: TRC20', max_length=20)
    wallet = models.CharField(verbose_name='Кошелёк:', max_length=255)
    img = models.ImageField(verbose_name='QR', upload_to='qr/wallet/')
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'QrUSDT'
        verbose_name_plural = 'QrUSDT'

    def get_absolute_url(self):
        return reverse('telegram:wallet_usdt', kwargs={'slug': self.slug})



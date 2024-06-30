import math

from django.db import models
from django.urls import reverse
import random
from .variables import BTC, USDT, DAY, DIFF, BLOCK, TWO, HASH
from decimal import Decimal

PERCENT = Decimal('0.8')
USD = Decimal('40.54')
GRIVEN = Decimal('0.449')


def generate_random_number():
    return random.randint(10000000, 99999999)


def asic_directory_path(instance, filename):
    return f'asic/{instance.title_min}/{filename}'


def asic_detail_directory_path(instance, filename):
    return f'asic_detail/{instance.title}/{filename}'


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=1)


class PopularAsicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=1, popular=1)


class AsicPopularBg(models.Model):
    title = models.CharField(verbose_name='Основной цвет, пример: синий', max_length=255)
    back_card = models.CharField(verbose_name='Задний фон для карты, пример: #000', max_length=255, blank=True,
                                 null=True)
    text_color = models.CharField(verbose_name='Цвет текста, пример: #000', max_length=255, blank=True, null=True)
    back_th = models.CharField(verbose_name='Задний фон для TH/s, пример: #000', max_length=255, blank=True, null=True)
    color_th = models.CharField(verbose_name='Цвет текста TH/s, пример: #000', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задний фон'
        verbose_name_plural = 'Задний фон'


class AsicDetailPhoto(models.Model):
    title = models.CharField(verbose_name='Название асика для фото', max_length=255)
    img = models.FileField(verbose_name='Фото', upload_to=asic_detail_directory_path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class AsicBrand(models.Model):
    title = models.CharField(verbose_name='Название бренда', max_length=255)
    image = models.FileField(verbose_name='Фото для бренда(svg)', upload_to='brand/')
    svg = models.FileField(verbose_name='Фото TELEGRAM для бренда(svg)', upload_to='brand_light/', blank=True, null=True)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def get_absolute_url(self):
        return reverse('catalog:brand_slug', kwargs={'slug': self.slug})

    def get_absolute_url_telegram(self):
        return reverse('telegram:brand_detail_t', kwargs={'slug': self.slug})


class FastFilter(models.Model):
    title = models.CharField(verbose_name='Название фильтра', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Быстрый фильтер'
        verbose_name_plural = 'Быстрые фильтры'

    def get_absolute_url(self):
        return reverse('catalog:fil_slug', kwargs={'slug': self.slug})


class Coin(models.Model):
    title = models.CharField(verbose_name='Название монеты', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'


class MiniProperty(models.Model):
    title = models.CharField(verbose_name='Название Асика для характеристик', max_length=255)
    algo = models.CharField(verbose_name='Алгоритм', max_length=100)
    coin = models.CharField(verbose_name='Добываемые(ая) монеты(а)', max_length=100)
    electro = models.CharField(verbose_name='Энергопотребление, пример: 3 080 Вт/ч ± 5%', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мини характеристика'
        verbose_name_plural = 'Мини характеристики'


class Property(models.Model):
    title = models.CharField(verbose_name='Название Асика для характеристик', max_length=255)
    firm = models.CharField(verbose_name='Производитель', max_length=255)
    model = models.CharField(verbose_name='Модель', max_length=20)
    crpt = models.CharField(verbose_name='Криптовалюта(ы)', max_length=100)
    hesh = models.CharField(verbose_name='Хешрэйт, пример: 63,5 Th/s', max_length=100)
    algo = models.CharField(verbose_name='Алгоритм', max_length=100)
    coin = models.CharField(verbose_name='Добываемые(ая) монеты(а)', max_length=100)
    electro = models.CharField(verbose_name='Энергопотребление, пример: 3 080 Вт/ч ± 5%', max_length=100)
    elect_ef = models.CharField(verbose_name='Энергоэффективность, пример: 48 J/TH', max_length=100, blank=True, null=True)
    temp = models.CharField(verbose_name='Рабочая температура, пример: от 0 до 40 °С', max_length=255)
    power = models.CharField(verbose_name='Источник питания', max_length=100)
    cold = models.CharField(verbose_name='Охлаждение', max_length=100)
    size = models.CharField(verbose_name='Размеры, пример: 195х290х400 мм', max_length=255)
    nose = models.CharField(verbose_name='Уровень шума, пример: 75 дБ', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class AsicDescription(models.Model):
    title = models.CharField(verbose_name='Название Асика для описания', max_length=100)
    our = models.TextField(verbose_name='О товаре')
    el = models.TextField(verbose_name='Какую криптовалюту можно добывать')
    protect = models.TextField(verbose_name='Особенности оборудования')
    firm = models.TextField(verbose_name='О производителе')
    money = models.TextField(verbose_name='Доходность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'


class Asic(models.Model):
    title = models.CharField(verbose_name='Полное название Асика', max_length=255)
    title_min = models.CharField(verbose_name='Краткое название Асика', max_length=255)
    asic_number = models.PositiveIntegerField(verbose_name='Номер асика', default=0, blank=True, null=True)
    main_img = models.ImageField(verbose_name='Главное фото Асика', upload_to=asic_directory_path)
    detail_img = models.ManyToManyField(AsicDetailPhoto, verbose_name='Фото асика для слайдера(детальная страница)')
    hesh = models.DecimalField(verbose_name='Хешрэйт, пример: 65.6', max_digits=5, decimal_places=1)
    power = models.PositiveIntegerField(verbose_name='Потребление, пример: 3200', default=0)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=0)
    old_price = models.DecimalField(verbose_name='Старая Цена (если есть)', max_digits=8, decimal_places=0, blank=True, null=True)
    active = models.BooleanField(verbose_name='Активный', default=True)
    availability = models.BooleanField(verbose_name='Наличие', default=True)
    popular = models.BooleanField(verbose_name='Популярный асик', default=False)
    brand = models.ForeignKey(AsicBrand, verbose_name='Бренд Асика', on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, verbose_name='Основная добываемая монета', on_delete=models.PROTECT)
    mini_property = models.OneToOneField(MiniProperty, verbose_name='Мини Характеристики', on_delete=models.PROTECT)
    property = models.OneToOneField(Property, verbose_name='Основные Характеристики', on_delete=models.PROTECT)
    description = models.OneToOneField(AsicDescription, verbose_name='Описание', on_delete=models.PROTECT, blank=True, null=True)
    article = models.BigIntegerField(verbose_name='Артикул', default=generate_random_number, editable=True)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(verbose_name='Изменён', auto_now=True, blank=True, null=True)
    percentages = models.DecimalField(verbose_name='Различие дохода в процентах, пример: 0.8', default=1.25, decimal_places=2, blank=True, null=True, max_digits=4)
    percent = models.DecimalField(verbose_name='Процент скидки: 0.8', default=0.8, decimal_places=2, blank=True, null=True, max_digits=4)
    bg_fon = models.ForeignKey(AsicPopularBg, on_delete=models.PROTECT, verbose_name='ЗАДНИЙ ФОН', blank=True, null=True)
    usdt = models.PositiveIntegerField(verbose_name='Цена в USDT', blank=True, null=True)

    back_card = models.CharField(verbose_name='Задний фон для карты, пример: #000', max_length=255, blank=True, null=True)
    text_color = models.CharField(verbose_name='Цвет текста, пример: #000', max_length=255, blank=True, null=True)
    back_th = models.CharField(verbose_name='Задний фон для TH/s, пример: #000', max_length=255, blank=True, null=True)
    color_th = models.CharField(verbose_name='Цвет текста TH/s, пример: #000', max_length=255, blank=True, null=True)

    slug = models.SlugField(verbose_name='URL', unique=True)

    faovarit = models.BooleanField('В избранном', default=False, blank=True, null=True)

    grivn_calc = models.DecimalField(verbose_name='Процент для перевода в гривны', decimal_places=5, max_digits=10, default=0.305)

    objects = models.Manager()
    published = PublishedManager()
    popularity = PopularAsicManager()

    def __str__(self):
        return self.title_min

    class Meta:
        verbose_name = 'Асик'
        verbose_name_plural = 'Асики'

    def get_absolute_url(self):
        return reverse('catalog:asic_detail', kwargs={'slug': self.slug})

    def get_percent_price(self):
        price = self.price * self.percent
        return round(price, 0)

    def profit_for_day(self):
        if self.coin.title == 'BTC':
            result = (((self.hesh * Decimal('10') ** 12) * BLOCK) * DAY) / (DIFF * TWO) * BTC * USDT
            rs_r = result / USDT
            rs_round = round(rs_r, 2)
            return rs_round

        else:
            result = ((((HASH * Decimal('10') ** 12) * BLOCK) * DAY) / (DIFF * TWO) * BTC * USDT) * self.percentages
            rs_r = result / USDT
            rs_round = round(rs_r, 2)
            return rs_round

    def profit_for_month(self):
        if self.coin.title == 'BTC':
            result = ((((self.hesh * Decimal('10') ** 12) * BLOCK) * DAY) / (DIFF * TWO) * BTC * USDT) * 30 * GRIVEN
            rs_r = result / USDT
            rs_round = round(rs_r, 2)
            return rs_round

        else:
            result = (((((HASH * Decimal('10') ** 12) * BLOCK) * DAY) / (DIFF * TWO) * BTC * USDT) * 30) * self.percentages
            rs_r = result / USDT
            rs_round = round(rs_r, 2)
            return rs_round

    def payback(self):
        if self.coin.title == 'BTC':
            result = self.price / (
                        ((((self.hesh * Decimal('10') ** 12) * BLOCK) * DAY) / (DIFF * TWO) * BTC * USDT) * 30)
            rs_round = round(result, 1)
            return rs_round

        else:
            result = self.price / (
                    ((((HASH * Decimal('10') ** 12) * BLOCK) * DAY) / (DIFF * TWO) * BTC * USDT) * 30 * self.percentages)
            rs_round = round(result, 1)
            return rs_round

    def get_usd_price(self):
        pr = self.usdt * USD
        return math.ceil(pr / 100) * 100


class StabilizerImage(models.Model):
    title = models.CharField(verbose_name='Название стабилизатора', max_length=255)
    img = models.FileField(verbose_name='Фото', upload_to='stabilizer/dop_photo/')

    def __str__(self):
        return f'Фото для {self.title}'

    class Meta:
        verbose_name = 'Доп фото стабилизатора'
        verbose_name_plural = 'Доп фото стабилизатора'


class StabilizerProperty(models.Model):
    title = models.CharField(verbose_name='Название характеристики', max_length=255)
    description = models.CharField(verbose_name='Описание характеристики', max_length=255)

    def __str__(self):
        return f'{self.title}: {self.description}'

    class Meta:
        verbose_name = 'Описание стабилизатора'
        verbose_name_plural = 'Описание стабилизатора'


class StabilizerBrand(models.Model):
    title = models.CharField(verbose_name='Название бренда', max_length=255)
    image = models.FileField(verbose_name='Фото если надо', upload_to='stabilizer/brand/', blank=True)
    show_title = models.CharField(verbose_name='Отображаемое название если надо', max_length=255, blank=True)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд Стабилизатора'
        verbose_name_plural = 'Бренды Стабилизаторов'

    def get_absolute_url(self):
        return reverse('catalog:stabilizer_brand', kwargs={'slug': self.slug})


class Phase(models.Model):
    title = models.CharField(verbose_name='Фаза', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фаза'
        verbose_name_plural = 'Фаза'

    def get_absolute_url(self):
        return reverse('catalog:phase_detail', kwargs={'slug': self.slug})


class Stabilizer(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, null=True)
    phase = models.ForeignKey(Phase, verbose_name='Фаза', on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(StabilizerBrand, on_delete=models.CASCADE, verbose_name='Производитель', null=True)
    price = models.DecimalField(verbose_name='Цена', decimal_places=0, max_digits=10, null=True)
    st_property = models.ManyToManyField(StabilizerProperty, verbose_name='Характеристики')
    main_img = models.ImageField(verbose_name='Главное фото', upload_to='stabilizer/', null=True)
    add_photo = models.ManyToManyField('StabilizerImage', verbose_name='Дополнительные фото', blank=True)
    slug = models.SlugField(verbose_name='URL', unique=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стабилизатор'
        verbose_name_plural = 'Стабилизаторы'

    def get_absolute_url(self):
        return reverse('catalog:stabilizer_detail', kwargs={'slug': self.slug})

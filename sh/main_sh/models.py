from django.db import models
from django.urls import reverse
from cat.models import Asic
import random
import string
from django.utils import timezone
import datetime
from django.utils.text import slugify
from decimal import Decimal

USDT = Decimal('95')


class MainSlide(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(main_page=1)


class ModelPublish(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(publish=1)


def generate_random_number():
    return random.randint(1000000000, 9999999999)


def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def generate_unique_slug(klass, field):
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{origin_slug}-{numb}'
        numb += 1
    return unique_slug


class SvgImgSlide(models.Model):
    title = models.CharField(verbose_name='Номер фото слайда', max_length=255, blank=True, null=True)
    number_slide = models.PositiveIntegerField(verbose_name='Номер слайда', default=0)
    svg = models.FileField(verbose_name='Svg для слайда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Svg для слайда'
        verbose_name_plural = 'Svg для слайда'


class Reviews(models.Model):
    title = models.CharField(verbose_name='Имя автора', max_length=255)
    description = models.TextField(verbose_name='Текст комментария')
    link_name = models.CharField(verbose_name='Имя аккаунта, пример: @dimadayn', max_length=255)
    link = models.CharField(verbose_name='Ссылка на аккаунт, пример: https://tme/dimadayn', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Slide(models.Model):
    title = models.CharField(verbose_name='Главный текст слайда', max_length=255)
    description = models.TextField(verbose_name='Описание слайда')
    img = models.ImageField(verbose_name='Главное фото', upload_to='slide_main_photo/', blank=True, null=True)
    color = models.CharField(verbose_name='Цвет текста, пример: #000', max_length=255)
    bg_color = models.CharField(verbose_name='Цвет слайда, пример: #000', max_length=255)
    number = models.PositiveIntegerField(verbose_name='Номер слайда', default=0, blank=True, null=True)
    main_page = models.BooleanField(verbose_name='Отображается на главной странице', default=False)
    svg_img = models.ManyToManyField(SvgImgSlide, verbose_name='Svg картинки для слайда, максимум 5')
    bg_hover_btn = models.CharField(verbose_name='Цвет при наведение на кнопку', max_length=255, blank=True, null=True)

    slug = models.SlugField(verbose_name='URL', unique=True)

    objects = models.Manager()
    main_slide = MainSlide()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def get_absolute_url(self):
        return reverse('main_page:slide_detail', kwargs={'slug': self.slug})


class BlogParagraph(models.Model):
    title = models.CharField(verbose_name='Заголовок абзаца', max_length=255)
    text = models.TextField(verbose_name='Текст абзаца')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Абзац'
        verbose_name_plural = 'Абзацы'


class BlogTag(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('main_page:detail_tag', kwargs={'slug': self.slug})


class BlogNews(models.Model):
    title = models.CharField(verbose_name='Заголовок новости', max_length=255)
    description = models.TextField(verbose_name='Описание новости')
    img = models.ImageField(verbose_name='Фото для новости(желательно 16:9, хуй знает как другая выглядеть будет)', upload_to='news/')
    created = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=False)
    paragraphs = models.ManyToManyField(BlogParagraph, verbose_name='Параграфы для новости')
    tegs = models.ManyToManyField(BlogTag, verbose_name='Теги для новости(любые, похуй)')
    publish = models.BooleanField(verbose_name='Опубликован', default=True)
    slug = models.SlugField(verbose_name='URL', unique=True)

    published = ModelPublish()
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('main_page:detail_news', kwargs={'slug': self.slug})


class Shipping(models.Model):
    PAYMENT_WAY_CHOICES = (
        ('usdt_self', 'USDT (оплатить самостоятельно)'),
        ('usdt_manager', 'USDT (оплатить с менеджером)'),
        ('card', 'На карту'),
        ('cash', 'Наличными'),
    )

    GET_WAY_CHOICES = (
        ('office_pickup', 'Самовывоз из офиса в Москве'),
        ('delivery', 'Доставка'),
    )

    payment_way = models.CharField(max_length=100, choices=PAYMENT_WAY_CHOICES)
    get_way = models.CharField(max_length=100, choices=GET_WAY_CHOICES)
    address = models.TextField(blank=True, null=True)
    recipient_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Информация о доставке для {self.phone}"


class OrderLot(models.Model):
    title = models.CharField(verbose_name='Для какого заказа, пример: Лот для заказа 1', max_length=255)
    number = models.PositiveIntegerField(verbose_name='Номер лота (в списке)', default=1)
    asic = models.ForeignKey(Asic, verbose_name='Асик для лота', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество асиков в лоте', default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'


class Order(models.Model):
    title = models.CharField(verbose_name='Номер заказа, например: Заказ 1', max_length=255)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, editable=True)
    order_number = models.BigIntegerField(verbose_name='Номер заказа', editable=True, unique=True)
    in_processing = models.BooleanField(verbose_name='В обработке', default=True)
    in_assembly = models.BooleanField(verbose_name='В сборке', default=False)
    in_transit = models.BooleanField(verbose_name='В пути', default=False)
    ready = models.BooleanField(verbose_name='Готов к выдаче', default=False)
    delivery_date = models.DateTimeField(verbose_name='Дата доставки(ну +-, или на которую договорились)')
    order_lots = models.ManyToManyField(OrderLot, verbose_name='Пункты в заказе')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Информация по доставке')
    slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_total_price(self):
        total = 0
        order_lots = self.order_lots.all()
        for lot in order_lots:
            total += lot.asic.price * lot.quantity * lot.asic.percent / USDT
        return round(total, 0)

    def save(self, *args, **kwargs):
        if not self.delivery_date:
            self.delivery_date = timezone.now() + datetime.timedelta(days=21)
        creating = not self.pk
        super(Order, self).save(*args, **kwargs)
        if creating or not self.slug:
            self.slug = generate_unique_slug(Order, self.title)
            super(Order, self).save(update_fields=['slug'])


class Application(models.Model):
    title = models.CharField(verbose_name='Заявка', max_length=255, default='Заявка')
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    created_at = models.DateTimeField(auto_now_add=True)
    payed = models.BooleanField(default=False, verbose_name='Оплачено')

    def __str__(self):
        return f'{self.title} для Заказа №{self.order.order_number}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def is_link_active(self):
        return timezone.now() <= self.created_at + timezone.timedelta(minutes=30)


class Warranty(models.Model):
    title = models.CharField(verbose_name='Для какого заказа, пример: Для заказа 1', max_length=255)
    order = models.OneToOneField(Order, verbose_name='Какой заказ', on_delete=models.CASCADE)
    art = models.CharField(verbose_name='Номер гарантии', default=generate_random_string, editable=True, max_length=9)
    ready = models.BooleanField(verbose_name='Заказ получили', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантии'


class AboutSteps(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    num = models.CharField(max_length=3)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']


class TrustSteps(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']


class PhotoLocation(models.Model):
    title = models.CharField(verbose_name='Номер картинки', max_length=20)
    img = models.ImageField(verbose_name='Фото', upload_to='about_slider/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотки'


class OrderSteps(models.Model):
    title = models.CharField(verbose_name='Название шага', max_length=255)
    step_number = models.PositiveIntegerField(verbose_name='Номер шага', default=1)
    description = models.TextField(verbose_name='Описание шага')
    img = models.ImageField(verbose_name='Фото для шага', upload_to='order_steps/')
    step_class = models.CharField(verbose_name='Класс для шага, пример: step__item1', max_length=255)
    timer = models.PositiveIntegerField(verbose_name='Время в минутах', default=5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги'


class UploadFile(models.Model):
    title = models.CharField(verbose_name='Название файла', max_length=255)
    file = models.FileField(verbose_name='Файл', upload_to='files/price_list')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Прайс лист'
        verbose_name_plural = 'Прайс листы'
        ordering = ['-id']


class ContractParagraphPoint(models.Model):
    text = models.TextField(verbose_name='Текст пункта')
    number = models.PositiveIntegerField(verbose_name='Номер пункта')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'


class ContractParagraph(models.Model):
    title = models.CharField(verbose_name='Название параграфа', max_length=255)
    paragraph_number = models.PositiveIntegerField(verbose_name='Номер параграфа')
    point = models.ManyToManyField(ContractParagraphPoint, verbose_name='Пункт параграфа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'
        ordering = ['paragraph_number']


class Contracts(models.Model):
    title = models.CharField(verbose_name='Название договора', max_length=255)
    contract_number = models.PositiveIntegerField(verbose_name='Номер договора')
    paragraph = models.ManyToManyField(ContractParagraph, verbose_name='Параграф')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'




























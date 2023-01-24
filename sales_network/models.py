from django.core.validators import MinValueValidator
from django.db import models
from user.models import CustomUser


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class Contact(models.Model):

    email = models.EmailField(verbose_name='Email', max_length=100, unique=True)
    country = models.CharField(verbose_name='Страна', max_length=100, blank=True)
    city = models.CharField(verbose_name='Город', max_length=100, blank=True)
    street = models.CharField(verbose_name='Улица', max_length=100, blank=True)
    number = models.CharField(verbose_name='Номер дома', max_length=10, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Product(models.Model):

    title = models.CharField(verbose_name='Название', max_length=255, unique=False)
    model = models.CharField(verbose_name='Модель', max_length=255)
    sellers = models.ManyToManyField('Participant', related_name='sellers', blank=True)
    issued = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Participant(models.Model):
    class Level(models.IntegerChoices):
        factory = 0, 'Завод'
        retail_network = 1, 'Розничная сеть'
        entrepreneur = 2, 'Индивидуальный предприниматель'

    title = models.CharField(verbose_name='Название', max_length=255, unique=True)
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень', choices=Level.choices, default=Level.entrepreneur
    )
    contact = models.ForeignKey(Contact, verbose_name='Контактная информация',
                                on_delete=models.DO_NOTHING, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    products = models.ManyToManyField('Product', related_name='products', blank=True)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return self.title


class Supplier(models.Model):

    seller = models.ForeignKey(Participant, verbose_name='Продавец', related_name='seller',
                               on_delete=models.CASCADE, unique=False)
    buyer = models.OneToOneField('Participant', verbose_name='Покупатель', related_name='buyer',
                                 on_delete=models.CASCADE)
    debt = models.DecimalField(verbose_name="Задолженность", decimal_places=2,
                               default=0.00, max_digits=25, validators=([MinValueValidator(0)]))

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.buyer.title



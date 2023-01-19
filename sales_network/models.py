from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import ForeignKey


class BaseModel(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=True)
    contacts = ArrayField(models.CharField(max_length=100), blank=True)
    produce = models.CharField(max_length=50, blank=True) # создать отдельный класс - Produce
    employee = models.CharField(max_length=50, blank=True)
    supplier = ''  # верно указать связи
    debt = ''  # верно указать связи
    created_date = models.DateTimeField(auto_now_add=True)


class Produce:
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    data = ForeignKey(BaseModel.created_date)


class Factory(BaseModel):
    pass


class Distributor(BaseModel):
    pass


class Dealership(BaseModel):
    pass


class RetailChain(BaseModel):
    pass


class IndividualEntrepreneur(BaseModel):
    pass


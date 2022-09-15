from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Bars(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bars'


class Customers(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Orders(models.Model):
    order_date = models.DateTimeField(blank=True, null=True)
    order_date_modification = models.DateTimeField(blank=True, null=True)
    order_date_modification_admin = models.IntegerField(blank=True, null=True)
    commentary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersDetails(models.Model):
    order = models.OneToOneField(
        Orders, models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(
        'Staff', models.DO_NOTHING, blank=True, null=True)
    bars = models.ForeignKey(Bars, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(
        Customers, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_details'


class OrdersDetailsReferences(models.Model):
    orders_details = models.OneToOneField(
        OrdersDetails, models.DO_NOTHING, primary_key=True)
    references = models.ForeignKey('References', models.DO_NOTHING)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_details_references'
        unique_together = (('orders_details', 'references'),)


class References(models.Model):
    ref = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'references'


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    hire_date = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Stock(models.Model):
    bars = models.ForeignKey(Bars, models.DO_NOTHING, blank=True, null=True)
    references = models.ForeignKey(
        References, models.DO_NOTHING, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class ViewStock(models.Model):
    reference = models.IntegerField()
    bars = models.IntegerField()
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_stock'

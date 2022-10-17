from django.db import models


class Bar(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["id"]


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    bar = models.ForeignKey(Bar, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.ForeignKey("Reference", models.DO_NOTHING, blank=True, null=True)
    count = models.BigIntegerField(default=1)

    class Meta:
        ordering = ["id"]


class Reference(models.Model):
    id = models.BigAutoField(primary_key=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["id"]


class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    stock = models.BigIntegerField(blank=True, null=True)
    bar = models.ForeignKey(Bar, models.DO_NOTHING, blank=True, null=True)
    reference = models.ForeignKey(Reference, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ["id"]

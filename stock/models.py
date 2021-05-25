# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StockTable2330(models.Model):
    stock_id = models.AutoField(primary_key=True, blank=True, null=False)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)
    #restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'stock_table_2330'
        


class Stock_list(models.Model):
    number = models.CharField(max_length=20)
    fullname= models.CharField(max_length=60)


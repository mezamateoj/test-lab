from django.db import models

# Create your models here.
class Card(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    supertype = models.TextField()
    subtypes = models.TextField(blank=True, null=True)  # This field type is a guess.
    types = models.TextField(blank=True, null=True)  # This field type is a guess.
    set = models.ForeignKey('Set', models.DO_NOTHING)
    number = models.TextField()
    rarity = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card'

class Set(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    series = models.TextField()
    printed_total = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    ptcgo_code = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    symbol_url = models.TextField(blank=True, null=True)
    logo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set'


class Market(models.Model):
    id = models.BigAutoField(primary_key=True)
    card = models.ForeignKey(Card, models.DO_NOTHING)
    url = models.TextField()
    updated_at = models.DateField()
    market = models.TextField()

    class Meta:
        managed = False
        db_table = 'market'

class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    card = models.ForeignKey(Card, models.DO_NOTHING)
    url = models.TextField()
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'image'

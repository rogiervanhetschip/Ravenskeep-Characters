from django.db import models

class Character(models.Model):
    spelerid = models.PositiveIntegerField()
    character_naam = models.CharField(max_length=50)
    ras = models.ForeignKey('Ras')
    live = models.PositiveIntegerField()
    lives_overleefd = models.PositiveIntegerField()
    xp_besteed = models.PositiveIntegerField()
    xp_restant = models.PositiveIntegerField()
    hitpoints = models.PositiveIntegerField()
    mana = models.PositiveIntegerField()
    god_id = models.ForeignKey('God')
    skills = models.ManyToManyField('Skill')
    opmerkingen = models.TextField()
    x_factor = models.CharField(max_length=250)
    spreuk1 = models.ManyToManyField('Spreuk')
    spreuk2 = models.ManyToManyField('Spreuk')
    spreuk3 = models.ManyToManyField('Spreuk')
    spreuk4 = models.ManyToManyField('Spreuk')
    spreuk5 = models.ManyToManyField('Spreuk')
    spreuk6 = models.ManyToManyField('Spreuk')
    spreuk7 = models.ManyToManyField('Spreuk')
    spreuk8 = models.ManyToManyField('Spreuk')
    spreuk9 = models.ManyToManyField('Spreuk')

class Skill(models.Model):
    naam = models.CharField(max_length=50)
    punten = models.PositiveIntegerField()

class God(models.Model):
    naam = models.CharField(max_length=50)

class Ras(models.Model):
    naam = models.CharField(max_length=50)

class Item(models.Model):
    naam = models.CharField(max_length=50)
    character_id = models.ForeignKey('Character')

class Spreuk(models.Model):
    naam = models.CharField(max_length=50)
    niveau = models.PositiveIntegerField()


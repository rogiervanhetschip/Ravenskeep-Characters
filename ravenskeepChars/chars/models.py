from django.db import models
from django.contrib import admin
from django.db.models import Sum
import pdb

class Character(models.Model):
    speler = models.ForeignKey('Player')
    character_naam = models.CharField(max_length=50)
    ras = models.ForeignKey('Race')
    eerste_live = models.PositiveIntegerField(default=31)
    live_nr = models.PositiveIntegerField(default=1)
    hitpoints = models.PositiveIntegerField(default=1)
    mana = models.PositiveIntegerField(default=0)
    god = models.ForeignKey('God', null=True, blank=True)
    subgod = models.ForeignKey('God', null=True, blank=True, related_name='subgod_character')
    skills = models.ManyToManyField('Skill', null=True, blank=True, related_name='skills')
    opmerkingen = models.TextField(blank=True)
    x_factor = models.CharField(max_length=250, blank=True)
    x_factor_skill = models.ForeignKey('Skill', null=True, blank=True, related_name='x_factor_skill')
    spreuken = models.ManyToManyField('Spell', null=True, blank=True)
    dood = models.BooleanField()

    def xp_totaal(self):
        return 15 + self.live_nr - 1 + self.ras.xp_extra

    def xp_besteed(self):
        return self.xp_besteed_skills + self.xp_besteed_spreuken + self.xp_besteed_recepten

    def xp_besteed_skills(self):
        aggregate_skills = self.skills.aggregate(Sum('punten'))
        return aggregate_skills['punten__sum']

    def xp_besteed_recepten(self):
        return 0

    def xp_besteed_spreuken(self):
        return 0

    def xp_restant(self):
        return self.xp_totaal() - self.xp_besteed()

    def __unicode__(self):
        return self.character_naam

    class Meta:
        ordering = ['speler', 'character_naam']

class Player(models.Model):
    voornaam = models.CharField(max_length=50)
    tussenvoegsels = models.CharField(max_length=50, blank=True)
    achternaam = models.CharField(max_length=50)

    def naam(self):
        if self.tussenvoegsels is None:
            return self.voornaam + " " + self.achternaam
        return self.voornaam + " " + self.tussenvoegsels + " " + self.achternaam

    def __unicode__(self):
        return self.naam()

    class Meta:
        ordering = ['achternaam', 'voornaam']    

class Skill(models.Model):
    naam = models.CharField(max_length=50)
    punten = models.PositiveIntegerField()

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['naam']

class God(models.Model):
    naam = models.CharField(max_length=50)

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['naam']

class Race(models.Model):
    naam = models.CharField(max_length=50)
    skill = models.ForeignKey('Skill', null=True, blank=True)
    xp_extra = models.BooleanField()

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['naam']

class Item(models.Model):
    naam = models.CharField(max_length=50)
    character = models.ForeignKey('Character')

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['character', 'naam']

class Spell(models.Model):
    naam = models.CharField(max_length=50)
    niveau = models.PositiveIntegerField()
    xp = models.PositiveIntegerField()
    mana = models.PositiveIntegerField()

    def __unicode__(self):
        return self.naam + " (" + str(self.niveau) + ")"

    class Meta:
        ordering = ['naam', 'niveau']

class ItemInline(admin.TabularInline):
    model = Item

class SkillInline(admin.TabularInline):
    model = Race

class CharacterAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]

    list_display = ('character_naam', 'speler')

    readonly_fields = ('xp_totaal', 'xp_besteed', 'xp_restant', 'id')



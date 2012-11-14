from django.db import models
from django.contrib import admin
from django.db.models import Sum
from django.forms.widgets import CheckboxSelectMultiple, SelectMultiple
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
    mage_spells = models.ManyToManyField('MageSpell', null=True, blank=True, related_name='MageSpells')
    priest_spells = models.ManyToManyField('PriestSpell', null=True, blank=True, related_name='Priest_Spells')
    recipes = models.ManyToManyField('Recipe', null=True, blank=True)
    dood = models.BooleanField()
    leermeesterpunten = models.PositiveIntegerField(default=0)

    def xp_total(self):
        return 14 + self.live_nr + self.ras.xp_extra + self.leermeesterpunten

    def xp_spent(self):
        return self.xp_spent_skills() + self.xp_spent_mage_spells() + self.xp_spent_priest_spells() + self.xp_spent_recipes()

    def xp_spent_skills(self):
        aggregate_skills = self.skills.aggregate(Sum('xp'))
        return aggregate_skills['xp__sum']

    def xp_spent_recipes(self):
        recipe_count = self.recipes.count()
        aggregate_recipes = self.skills.aggregate(Sum('free_recipes'))
        x_factor = 0
        if(self.x_factor_skill):
            x_factor = self.x_factor_skill.free_recipes
        return max(recipe_count - aggregate_recipes['free_recipes__sum'] - x_factor, 0)

    def xp_spent_mage_spells(self):
        aggregate_mage_spells = self.mage_spells.aggregate(Sum('xp'))
        return max(aggregate_mage_spells['xp__sum'], 0)

    def xp_spent_priest_spells(self):
        xp = 0
        spell_groups = [[1, 4, 'free_123_spells'], [4, 7, 'free_456_spells'], [7, 10, 'free_789_spells']]
        for spell_group in spell_groups:
            for level in range(spell_group[0], spell_group[1]):
                # Find all spells of appropriate level, order by xp
                spells = self.priest_spells.filter(niveau=level).order_by('xp').reverse()
                number_of_free_spells = self.skills.aggregate(Sum(spell_group[2]))[spell_group[2]+'__sum']
                # Remove most expensive of each level you're allowed to have
                if(number_of_free_spells > 0):
                    spells = spells[number_of_free_spells:].annotate()
                # Sum the rest
                xp += max(spells.aggregate(Sum('xp'))['xp__sum'], 0)
        return xp

    def xp_remaining(self):
        return self.xp_total() - self.xp_spent()

    def hitpoints(self):
        hp_count = { 1 : 1,
                     2 : 1,
                     3 : 2,
                     4 : 2,
                     5 : 2,
                     6 : 3,
                     7 : 3,
                     8 : 3,
                     9 : 3,
                    10 : 4,
                    11 : 4,
                    12 : 4,
                    13 : 4,
                    14 : 4,
                    15 : 5,
                    16 : 5,
                    17 : 5,
                    18 : 5,
                    19 : 5,
                    20 : 5,
                    21 : 6,
                    22 : 6,
                    23 : 6,
                    24 : 6,
                    25 : 6,
                    26 : 6,
                    27 : 6,
                    28 : 7,
                    29 : 7,
                    30 : 7,
                    31 : 7,
                    32 : 7,
                    33 : 7,
                    34 : 7,
                    35 : 7,
                    36 : 8,
                    37 : 8,
                    38 : 8,
                    39 : 8,
        }
        aggregate_hitpoints = self.skills.aggregate(Sum('extra_hitpoints'))
        return hp_count[self.live_nr] + aggregate_hitpoints['extra_hitpoints__sum']

    def mana(self):
        aggregate_mana = self.skills.aggregate(Sum('extra_mana'))
        return 5 + self.live_nr + aggregate_mana['extra_mana__sum']

    def __unicode__(self):
        return self.character_naam

    class Meta:
        ordering = ['speler', 'character_naam']

class Player(models.Model):
    voornaam = models.CharField(max_length=50)
    tussenvoegsels = models.CharField(max_length=50, blank=True)
    achternaam = models.CharField(max_length=50)

    class Meta:
        ordering = ['voornaam', 'achternaam']

    def naam(self):
        if self.tussenvoegsels is None:
            return self.voornaam + " " + self.achternaam
        return self.voornaam + " " + self.tussenvoegsels + " " + self.achternaam

    def __unicode__(self):
        return self.naam()

class Skill(models.Model):
    naam = models.CharField(max_length=50)
    xp = models.PositiveIntegerField()
    extra_hitpoints = models.PositiveIntegerField(default=0)
    extra_mana = models.PositiveIntegerField(default=0)
    free_123_spells = models.PositiveIntegerField(default=0)
    free_456_spells = models.PositiveIntegerField(default=0)
    free_789_spells = models.PositiveIntegerField(default=0)
    free_recipes = models.PositiveIntegerField(default=0)

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

class PriestSpell(Spell):
    pass

class MageSpell(Spell):
    pass

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    class Meta:
        ordering = ['name', 'code']

    def __unicode__(self):
        return self.name + " (" + self.code + ")"

class ItemInline(admin.TabularInline):
    model = Item

class SkillInline(admin.TabularInline):
    model = Race

class CharacterAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]

    list_display = ('character_naam', 'speler')

    readonly_fields = ('id', 'xp_total', 'xp_spent', 'xp_remaining', 'hitpoints', 'mana')

    formfield_overrides = {
#        models.ManyToManyField: { 'widget': SelectMultiple(attrs={'style':'height: 200px'}) },
#        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
#ChosenSelectMultiple
    }

    filter_horizontal = [
        'skills',
        'spreuken',
        'priest_spells',
        'mage_spells',
        'recipes',
    ]



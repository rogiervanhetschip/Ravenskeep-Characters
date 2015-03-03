# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.db.models import Q
import pdb

class Migration(DataMigration):

    def forwards(self, orm):
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        for char in orm.Character.objects.all():
            skills = self.all_skills(char, orm)
            if skills.filter(gives_mana=True).count() > 0:
                char.first_live_nr_mana = 1
                char.save()

    def all_skills(self, char, orm):
        if char.x_factor_skill == None:
            return orm['chars.skill'].objects.filter(Q(id__in=char.skills.all()))
        else:
            return orm['chars.skill'].objects.filter(Q(id=char.x_factor_skill.id) | Q(id__in=char.skills.all()))


    def backwards(self, orm):
        for char in orm.Character.objects.all():
            char.first_live_nr_mana = 0
            char.save()

    models = {
        'chars.character': {
            'Meta': {'ordering': "['speler', 'character_naam']", 'object_name': 'Character'},
            'character_naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dood': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eerste_live': ('django.db.models.fields.PositiveIntegerField', [], {'default': '31'}),
            'first_live_nr_mana': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'god': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.God']", 'null': 'True', 'blank': 'True'}),
            'has_mana': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leermeesterpunten': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'live_nr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'mage_spells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MageSpells'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['chars.MageSpell']"}),
            'opmerkingen': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'priest_spells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Priest_Spells'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['chars.PriestSpell']"}),
            'ras': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.Race']"}),
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['chars.Recipe']", 'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'skills'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['chars.Skill']"}),
            'speler': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.Player']"}),
            'spreuken': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['chars.Spell']", 'null': 'True', 'blank': 'True'}),
            'subgod': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subgod_character'", 'null': 'True', 'to': "orm['chars.God']"}),
            'x_factor': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'x_factor_skill': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'x_factor_skill'", 'null': 'True', 'to': "orm['chars.Skill']"})
        },
        'chars.god': {
            'Meta': {'ordering': "['naam']", 'object_name': 'God'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.item': {
            'Meta': {'ordering': "['character', 'naam']", 'object_name': 'Item'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.magespell': {
            'Meta': {'ordering': "['naam', 'niveau']", 'object_name': 'MageSpell', '_ormbases': ['chars.Spell']},
            'spell_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['chars.Spell']", 'unique': 'True', 'primary_key': 'True'})
        },
        'chars.player': {
            'Meta': {'ordering': "['voornaam', 'achternaam']", 'object_name': 'Player'},
            'achternaam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tussenvoegsels': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'voornaam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.priestspell': {
            'Meta': {'ordering': "['naam', 'niveau']", 'object_name': 'PriestSpell', '_ormbases': ['chars.Spell']},
            'spell_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['chars.Spell']", 'unique': 'True', 'primary_key': 'True'})
        },
        'chars.race': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Race'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.Skill']", 'null': 'True', 'blank': 'True'}),
            'xp_extra': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'chars.recipe': {
            'Meta': {'ordering': "['code', 'name']", 'object_name': 'Recipe'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.skill': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Skill'},
            'extra_hitpoints': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'extra_mana': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'free_123_spells': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'free_456_spells': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'free_789_spells': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'free_recipes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'gives_mana': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'xp': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'chars.spell': {
            'Meta': {'ordering': "['naam', 'niveau']", 'object_name': 'Spell'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mana': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'niveau': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'xp': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['chars']
    symmetrical = True

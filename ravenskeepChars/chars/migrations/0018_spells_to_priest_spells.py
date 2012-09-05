# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from chars.models import Spell, PriestSpell

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        for spell in orm.Spell.objects.all():
            priest_spell = PriestSpell()
            priest_spell.mana = spell.mana
            priest_spell.niveau = spell.niveau
            priest_spell.naam = spell.naam
            priest_spell.xp = spell.xp
            priest_spell.save()
            spell.delete()

    def backwards(self, orm):
        "Write your backwards methods here."
        for priest_spell in orm.PriestSpell.objects.all():
            spell = Spell()
            spell.mana = priest_spell.mana
            spell.niveau = priest_spell.niveau
            spell.naam = priest_spell.naam
            spell.xp = priest_spell.xp
            spell.save()
            priest_spell.delete()

    models = {
        'chars.character': {
            'Meta': {'ordering': "['speler', 'character_naam']", 'object_name': 'Character'},
            'character_naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dood': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eerste_live': ('django.db.models.fields.PositiveIntegerField', [], {'default': '31'}),
            'god': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.God']", 'null': 'True', 'blank': 'True'}),
            'hitpoints': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live_nr': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'mage_spells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MageSpells'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['chars.MageSpell']"}),
            'mana': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'opmerkingen': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'priest_spells': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Priest_Spells'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['chars.PriestSpell']"}),
            'ras': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.Race']"}),
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
            'Meta': {'ordering': "['achternaam', 'voornaam']", 'object_name': 'Player'},
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
        'chars.skill': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'punten': ('django.db.models.fields.PositiveIntegerField', [], {})
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

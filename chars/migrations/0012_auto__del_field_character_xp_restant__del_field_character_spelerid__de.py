# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Character.xp_restant'
        db.delete_column('chars_character', 'xp_restant')

        # Deleting field 'Character.spelerid'
        db.delete_column('chars_character', 'spelerid_id')

        # Deleting field 'Character.xp_besteed'
        db.delete_column('chars_character', 'xp_besteed')

        # Deleting field 'Character.xp_totaal'
        db.delete_column('chars_character', 'xp_totaal')

        # Adding field 'Character.speler'
        db.add_column('chars_character', 'speler',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chars.Player']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Character.xp_restant'
        db.add_column('chars_character', 'xp_restant',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.spelerid'
        db.add_column('chars_character', 'spelerid',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chars.Player']),
                      keep_default=False)

        # Adding field 'Character.xp_besteed'
        db.add_column('chars_character', 'xp_besteed',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.xp_totaal'
        db.add_column('chars_character', 'xp_totaal',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Character.speler'
        db.delete_column('chars_character', 'speler_id')


    models = {
        'chars.character': {
            'Meta': {'object_name': 'Character'},
            'character_naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'eerste_live': ('django.db.models.fields.PositiveIntegerField', [], {'default': '31'}),
            'god': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.God']", 'null': 'True', 'blank': 'True'}),
            'hitpoints': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lives_overleefd': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'mana': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'opmerkingen': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ras': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.Race']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['chars.Skill']", 'null': 'True', 'blank': 'True'}),
            'speler': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.Player']"}),
            'spreuken': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['chars.Spell']", 'null': 'True', 'blank': 'True'}),
            'x_factor': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'chars.god': {
            'Meta': {'object_name': 'God'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.item': {
            'Meta': {'object_name': 'Item'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.player': {
            'Meta': {'object_name': 'Player'},
            'achternaam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tussenvoegsels': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'voornaam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.race': {
            'Meta': {'object_name': 'Race'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.skill': {
            'Meta': {'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'punten': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'chars.spell': {
            'Meta': {'object_name': 'Spell'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'niveau': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['chars']
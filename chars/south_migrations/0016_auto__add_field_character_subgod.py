# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Character.subgod'
        db.add_column('chars_character', 'subgod',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='subgod_character', null=True, to=orm['chars.God']),
                      keep_default=False)
        
        # Rename 'lives_overleefd' field to 'live_nr'
        db.rename_column('chars_character', 'lives_overleefd', 'live_nr')

    def backwards(self, orm):
        # Deleting field 'Character.subgod'
        db.delete_column('chars_character', 'subgod_id')

        # Rename 'live_nr' field to 'lives_overleefd'
        db.rename_column('chars_character', 'live_nr', 'lives_overleefd')



    models = {
        'chars.character': {
            'Meta': {'ordering': "['speler', 'character_naam']", 'object_name': 'Character'},
            'character_naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dood': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eerste_live': ('django.db.models.fields.PositiveIntegerField', [], {'default': '31'}),
            'god': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chars.God']", 'null': 'True', 'blank': 'True'}),
            'hitpoints': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lives_overleefd': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'mana': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'opmerkingen': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
        'chars.player': {
            'Meta': {'ordering': "['achternaam', 'voornaam']", 'object_name': 'Player'},
            'achternaam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tussenvoegsels': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'voornaam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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

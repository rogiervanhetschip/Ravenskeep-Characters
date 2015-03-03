# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Race.skill'
        db.add_column('chars_race', 'skill',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chars.Skill'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Race.xp_extra'
        db.add_column('chars_race', 'xp_extra',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.x_factor_skill'
        db.add_column('chars_character', 'x_factor_skill',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='x_factor_skill', null=True, to=orm['chars.Skill']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Race.skill'
        db.delete_column('chars_race', 'skill_id')

        # Deleting field 'Race.xp_extra'
        db.delete_column('chars_race', 'xp_extra')

        # Deleting field 'Character.x_factor_skill'
        db.delete_column('chars_character', 'x_factor_skill_id')


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
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'niveau': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['chars']
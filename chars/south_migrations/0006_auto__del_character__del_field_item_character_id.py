# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Character'
        db.delete_table('chars_character')

        # Removing M2M table for field spreuken on 'Character'
        db.delete_table('chars_character_spreuken')

        # Removing M2M table for field skills on 'Character'
        db.delete_table('chars_character_skills')

        # Deleting field 'Item.character_id'
        db.delete_column('chars_item', 'character_id_id')


    def backwards(self, orm):
        # Adding model 'Character'
        db.create_table('chars_character', (
            ('xp_restant', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('god', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chars.God'], null=True, blank=True)),
            ('spelerid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chars.Player'])),
            ('character_naam', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mana', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('eerste_live', self.gf('django.db.models.fields.PositiveIntegerField')(default=31)),
            ('lives_overleefd', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('xp_besteed', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('opmerkingen', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('x_factor', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('hitpoints', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('xp_totaal', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ras', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chars.Race'])),
        ))
        db.send_create_signal('chars', ['Character'])

        # Adding M2M table for field spreuken on 'Character'
        db.create_table('chars_character_spreuken', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm['chars.character'], null=False)),
            ('spell', models.ForeignKey(orm['chars.spell'], null=False))
        ))
        db.create_unique('chars_character_spreuken', ['character_id', 'spell_id'])

        # Adding M2M table for field skills on 'Character'
        db.create_table('chars_character_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm['chars.character'], null=False)),
            ('skill', models.ForeignKey(orm['chars.skill'], null=False))
        ))
        db.create_unique('chars_character_skills', ['character_id', 'skill_id'])

        # Adding field 'Item.character_id'
        db.add_column('chars_item', 'character_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['chars.Character']),
                      keep_default=False)


    models = {
        'chars.god': {
            'Meta': {'object_name': 'God'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'chars.item': {
            'Meta': {'object_name': 'Item'},
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
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character_naam', models.CharField(max_length=50)),
                ('eerste_live', models.PositiveIntegerField(default=None)),
                ('live_nr', models.PositiveIntegerField(default=1)),
                ('first_live_nr_mana', models.PositiveIntegerField(default=0)),
                ('has_mana', models.BooleanField(help_text=b'Character has mana of its own, even without receiving mana from Skills')),
                ('opmerkingen', models.TextField(blank=True)),
                ('x_factor', models.CharField(max_length=500, blank=True)),
                ('dood', models.BooleanField()),
                ('leermeesterpunten', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['speler', 'character_naam'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='God',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['naam'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(max_length=50)),
                ('character', models.ForeignKey(to='chars.Character')),
            ],
            options={
                'ordering': ['character', 'naam'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voornaam', models.CharField(max_length=50)),
                ('tussenvoegsels', models.CharField(max_length=50, blank=True)),
                ('achternaam', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150, blank=True)),
            ],
            options={
                'ordering': ['voornaam', 'achternaam'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(max_length=50)),
                ('xp_extra', models.BooleanField()),
            ],
            options={
                'ordering': ['naam'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['code', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(max_length=50)),
                ('xp', models.PositiveIntegerField()),
                ('gives_mana', models.BooleanField()),
                ('extra_hitpoints', models.PositiveIntegerField(default=0)),
                ('extra_mana', models.PositiveIntegerField(default=0)),
                ('free_123_spells', models.PositiveIntegerField(default=0)),
                ('free_456_spells', models.PositiveIntegerField(default=0)),
                ('free_789_spells', models.PositiveIntegerField(default=0)),
                ('free_recipes', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['naam'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(max_length=50)),
                ('niveau', models.PositiveIntegerField()),
                ('xp', models.PositiveIntegerField()),
                ('mana', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['niveau', 'naam'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriestSpell',
            fields=[
                ('spell_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='chars.Spell')),
            ],
            options={
            },
            bases=('chars.spell',),
        ),
        migrations.CreateModel(
            name='MageSpell',
            fields=[
                ('spell_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='chars.Spell')),
            ],
            options={
            },
            bases=('chars.spell',),
        ),
        migrations.AddField(
            model_name='race',
            name='skill',
            field=models.ForeignKey(blank=True, to='chars.Skill', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='god',
            field=models.ForeignKey(blank=True, to='chars.God', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='mage_spells',
            field=models.ManyToManyField(related_name='MageSpells', null=True, to='chars.MageSpell', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='priest_spells',
            field=models.ManyToManyField(related_name='Priest_Spells', null=True, to='chars.PriestSpell', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='ras',
            field=models.ForeignKey(to='chars.Race'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='recipes',
            field=models.ManyToManyField(to='chars.Recipe', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(related_name='skills', null=True, to='chars.Skill', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='speler',
            field=models.ForeignKey(to='chars.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='subgod',
            field=models.ForeignKey(related_name='subgod_character', blank=True, to='chars.God', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='x_factor_skill',
            field=models.ForeignKey(related_name='x_factor_skill', blank=True, to='chars.Skill', null=True),
            preserve_default=True,
        ),
    ]

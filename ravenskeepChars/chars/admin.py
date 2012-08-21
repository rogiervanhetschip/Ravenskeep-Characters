from chars.models import Character, Player, Skill, God, Race, Item, Spell, CharacterAdmin
from django.contrib import admin

admin.site.register(Character, CharacterAdmin)
admin.site.register(Player)
admin.site.register(Skill)
admin.site.register(God)
admin.site.register(Race)
admin.site.register(Item)
admin.site.register(Spell)



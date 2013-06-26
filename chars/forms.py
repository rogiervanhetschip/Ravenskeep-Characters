from django.forms import ModelForm
from chars.models import Character

class CharacterForm(ModelForm):
  class Meta:
    model = Character


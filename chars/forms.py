from django.forms import ModelForm, TextInput, DateInput, SelectMultiple
from chars.models import Character
from chosen.forms import ChosenSelectMultiple
import pdb

class CharacterForm(ModelForm):
  # http://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django
  def __init__(self, *args, **kwargs):
    super(CharacterForm, self).__init__(*args, **kwargs)
    for field_name in self.fields:
      field = self.fields.get(field_name)  
      if field:
        if type(field.widget) in (TextInput, DateInput): # TODO: DateInput verwisselen met een TextInput?!
          field.widget = TextInput(attrs={'placeholder': field.label})
        elif type(field.widget) is SelectMultiple:
          field.help_text = '' # Bug: https://code.djangoproject.com/ticket/9321
          field.widget = ChosenSelectMultiple(overlay='Type away...', choices=field.choices)

  class Meta:
    model = Character


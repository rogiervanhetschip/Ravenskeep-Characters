from django import forms
from chars.models import Character

class IndexForm(forms.Form):
  char_id = forms.IntegerField(min_value=1, max_value=Character.objects.count, required=True)
  old = forms.BooleanField(required=True, widget=forms.HiddenInput())


from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms.models import inlineformset_factory
from chars.models import Character, Item
from chars.forms import CharacterForm
import pdb

def admin_rights(request):
  if request.user.is_staff:
    return True
  return False

@login_required
def home(request):
  c = {}
  c.update(csrf(request))
  chars_complete = Character.objects.filter(dood=False)
  p = Paginator(chars_complete, 10)
  page_nr = request.GET.get('page_nr')
  try:
    chars = p.page(page_nr)
  except PageNotAnInteger:
    chars = p.page(1)
  except EmptyPage:
    chars = p.page(p.num_pages)
  return render(request, 'index.html', { 'chars': chars, 'c': c, 'admin': admin_rights(request) })

@login_required
def charRead(request, char_id):
  char = get_object_or_404(Character, id=char_id)
  return render_to_response('char.html', { 'char': char })
  # char_form = CharacterForm(instance=char)

@login_required
def charPrintPreview(request, char_id):
  char = get_object_or_404(Character, id=char_id)
  return render_to_response('charPrintPreview.html', { 'chars': { char } })

@login_required
def charsPrintPreview(request, chars):
  return render_to_response('charPrintPreview.html', { 'chars': chars })

@login_required
def charNew(request):
  c = {}
  c.update(csrf(request))
  ItemInlineFormSet = inlineformset_factory(Character, Item)
  if request.method == 'POST':
    form = CharacterForm(request.POST)
    items_form = ItemInlineFormSet() #???
    if form.is_valid() and items_form.is_valid():
      # Character save
      form.save()
      # Items save
      items_form.save()
      return redirect('home') # TODO: "Opgeslagen!" melding sturen
  else:
    form = CharacterForm()
    items_form = ItemInlineFormSet() #???
  return render(request, 'charNew.html', { 'form': form, 'c': c, 'items': items_form, 'admin': admin_rights(request) })
# TODO: Foutmeldingen op het scherm tonen

@login_required
def logout_user(request):
  logout(request)
  return redirect('login')


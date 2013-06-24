from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from chars.models import Character
import pdb

@login_required
def home(request):
  c = {}
  c.update(csrf(request))
  chars = Character.objects.filter(dood=False) # Evt. later values() gebruiken, maar dan moet method 
  return render(request, 'index.html', { 'chars': chars, 'c': c })

@login_required
def charRead(request, char_id):
  char = get_object_or_404(Character, id=char_id)
  return render_to_response('char.html', {'char': char})

@login_required
def charPrintPreview(request, char_id):
  char = get_object_or_404(Character, id=char_id)
  return render_to_response('charPrintPreview.html', {'chars': { char } })

@login_required
def charsPrintPreview(request, chars):
  return render_to_response('charPrintPreview.html', {'chars': chars})

@login_required
def logout_user(request):
  logout(request)
  return redirect('/login/')


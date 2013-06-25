from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from chars.models import Character
import pdb

@login_required
def home(request):
  c = {}
  c.update(csrf(request))
  chars_complete = Character.objects.filter(dood=False)
  p = Paginator(chars_complete, 1)
  page_nr = request.GET.get('page_nr')
  try:
    chars = p.page(page_nr)
  except PageNotAnInteger:
    chars = p.page(1)
  except EmptyPage:
    chars = p.page(p.num_pages)

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


from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from chars.models import Character
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        if request.POST['oldornew'] == 'old':
            return redirect('char/' + request.POST['charId'] + '/printpreview/', c)
        return redirect('char/' + request.POST['charId'], c)
    return render_to_response('index.html', c)

@login_required
def charRead(request, char_id):
    char = get_object_or_404(Character, id=char_id)
    return render_to_response('char.html', {'char': char})

@login_required
def charPrintPreview(request, char_id):
    char = get_object_or_404(Character, id=char_id)
    return render_to_response('charPrintPreview.html', {'char': char})

@login_required
def logout_user(request):
    logout(request)
    return redirect('/login/')


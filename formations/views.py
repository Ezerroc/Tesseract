from django.shortcuts import render
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Formation
import os

def formation(request):
    formations = Formation.objects.all()
    return render(request, 'formations/formations.html', {'formations': formations})

def pdf_view(request, pdf_id):
    formation = get_object_or_404(Formation, id=pdf_id)
    if formation.pdf_file and os.path.exists(formation.pdf_file.path):
        return FileResponse(open(formation.pdf_file.path, 'rb'), content_type='application/pdf')
    else:
        raise Http404()

from ast import Return
import datetime
from pipes import Template 
from django.http import HttpResponse
from django.template import Context, Template, loader

from AppFamilia.views import familiar


def probandoTemplate(request):
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(familiar)

    return HttpResponse(documento)

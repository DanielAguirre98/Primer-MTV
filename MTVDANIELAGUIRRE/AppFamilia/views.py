from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
# Create your views here.

def familiar(request):

    familiar1= Familiar(nombre="Daniel Aguirre", edad= 24, fecha="1998-02-01")
    familiar1.save()
    familiar2= Familiar(nombre="Paula Stele", edad= 26, fecha="1996-03-13")
    familiar2.save()
    familiar3= Familiar(nombre="Pia Nicoli", edad= 6, fecha="1998-02-01")
    familiar3.save()

    documento_texto= f"""Nombre de familiar: {familiar1.nombre} , Edad del familiar: {familiar1.edad} , Fecha de nacimiento del familiar: {familiar1.fecha} 
                         Nombre de familiar: {familiar2.nombre} , Edad del familiar: {familiar2.edad} , Fecha de nacimiento del familiar: {familiar2.fecha} 
                         Nombre de familiar: {familiar3.nombre} , Edad del familiar: {familiar3.edad} , Fecha de nacimiento del familiar: {familiar3.fecha}"""
    return HttpResponse(documento_texto)

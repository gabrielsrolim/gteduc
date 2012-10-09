# Create your views here.
from django.shortcuts import render_to_response
from django.conf import settings
from gteducsite.models import Informativos

def index(request):
	d = Informativos.objects.order_by('id')
	return render_to_response('gteducsite/index.html',{'dados' : d})

def empresa(request):
	d = Informativos.objects.order_by('id')
	return render_to_response('gteducsite/empresa.html',{'dados' : d})

def produtoservicos(request):
	d = Informativos.objects.order_by('id')
	return render_to_response('gteducsite/produtoservicos.html',{'dados' : d})

def suporte(request):
	d = Informativos.objects.order_by('id')
	return render_to_response('gteducsite/suporte.html',{'dados' : d})

def clientes(request):
	d = Informativos.objects.order_by('id')
	return render_to_response('gteducsite/clientes.html',{'dados' : d})

def parceiros(request):
	d = Informativos.objects.order_by('id')
	return render_to_response('gteducsite/parceiros.html',{'dados' : d})

def contatos(request):
	d = Informativos.objects.order_by('id')
	return render_to_response('gteducsite/contatos.html',{'dados' : d})

# Create your views here.
from django.shortcuts import render_to_response
from django.conf import settings
from gteducsite.models import Informativos

def index(request):
	return render_to_response('gteducsite/index.html')

def empresa(request):
	return render_to_response('gteducsite/empresa.html')

def produtoservicos(request):
	return render_to_response('gteducsite/produtoservicos.html')

def suporte(request):
	return render_to_response('gteducsite/suporte.html')

def clientes(request):
	d = Informativos.objects.all()
	return render_to_response('gteducsite/clientes.html',{'index' : d})

def parceiros(request):
	return render_to_response('gteducsite/parceiros.html')

def contatos(request):
	return render_to_response('gteducsite/contatos.html')

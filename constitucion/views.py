import hashlib
import os
import time
import hashlib

import email
import constitucion.spreadsheet as sp


from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils.encoding import smart_str

from constitucion.robin import roundrobin

template_acta_url = 'http://constitucionabierta.cl/acta/%s/'
template_direct_acta_url = 'http://constitucionabierta.cl/static/acta/%s/'
template_acta_modificar_url = 'http://constitucionabierta.cl/acta/modificar/%s/%s/'

def index(request):
    return render(request, 'index.html')

def mapa(request):
    return render(request, 'mapa.html')

def opendata(request):
    return render(request, 'opendata-cco.html')

def mosaico(request):
    return render(request, 'mosaico.html')

def random(request):
    url = sp.get_random_acta()
    return HttpResponseRedirect(url)

def get_filename(file_):
    name = file_.name
    extension = file_.name.split('.')
    extension = extension[-1]
    timestamp = time.time()
    filename = "%s%s" % (name, timestamp)
    filename = "%s.%s" % (hashlib.md5(filename).hexdigest(), extension)
    return filename

def subir(request):
	return render(request, 'upload.html')

def upload_file(request):
    if request.method == 'POST':
        if request.FILES['file'].size > 20*1024*1024 or not request.POST['g-recaptcha-response']:
        	return HttpResponseRedirect('/constitucion/subir')
        filename = get_filename(request.FILES['file'])
        handle_uploaded_file(request.FILES['file'], filename)

        acta_url = template_direct_acta_url % filename
        secret = hashlib.md5(str(time.time())).hexdigest()
        acta_modificar_url = template_acta_modificar_url % (filename, secret)

        acta_number = sp.get_last_acta_number()
        numero_encargado = acta_number % len(roundrobin)

        encargado = roundrobin[numero_encargado]
        mail_encargado = encargado[1]
        name_encargado = encargado[0]

        acta_number = sp.insert_new_acta(acta_url, acta_modificar_url, secret, name_encargado)

        name, extension = filename.split('.')
        filename = name+'.pdf'

        email.send_email('constitucionabierta@gmail.cl', mail_encargado, name_encargado, acta_number)
        return render(request, 'success.html', {'url': filename})
    else:
        return HttpResponseRedirect('/constitucion/subir')


def handle_uploaded_file(f, filename):
    with open(os.path.join(settings.ACTAS_DIRECTORY, filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def acta(request, name):
    acta_url = template_direct_acta_url % name
    valid = sp.is_valid_acta(acta_url)
    if valid:
        return HttpResponseRedirect('/static/acta/%s' % name)
    else:
        return render(request, 'not_yet.html')


def modify(request, filename, secret):
    acta_url = template_direct_acta_url % filename
    acta_number = sp.check_in_spreadsheet(acta_url, secret)
    if not acta_number:
        raise Http404
    else:
        return render(request, 'upload.html', {
            'modify': True, 'filename': filename, 'secret': secret, 'acta_number': acta_number-1,
        })


def upload_modify(request, filename, secret):
    if request.method == 'POST':
        acta_url = template_direct_acta_url % filename
        acta_number = sp.check_in_spreadsheet(acta_url, secret)
        if not acta_number:
            return render(request, '404.html')
        name, extension = filename.split('.')
        filename = name+'.pdf'

        acta_url = template_direct_acta_url % filename
        acta_modificar_url = template_acta_modificar_url % (filename,secret)

        sp.insert(acta_number, acta_url, acta_modificar_url)

        handle_uploaded_file(request.FILES['file'], filename)
        return render(request, 'success.html', {'url': filename, 'modify': True, "acta_number":acta_number-1})
    else:
        return HttpResponseRedirect('/constitucion/subir')


    return None

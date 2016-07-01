import hashlib
import os
import time
import hashlib
import datetime

import email
import constitucion.spreadsheet as sp

from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils.encoding import smart_str
from subprocess import call

from constitucion.models import Acta


def index(request):
    return render(request, 'index.html')

def mapa(request):
    return render(request, 'mapa.html')

def opendata(request):
    return render(request, 'opendata-cco.html')

def mosaico(request):
    actas = Acta.objects.filter(valid = True)

    thumbs = map(lambda a: a.get_thumbnail_url(), actas)
    files = map(lambda a: a.get_thumbnail_path(), actas)
    files = map(lambda u: os.path.isfile(u), files)
    urls = map(lambda a: a.get_url(), actas)

    pdfimg = "http://culturehive.co.uk/wp-content/themes/ama/images/backup-pdf.png"
    thumbs = map(lambda e: e[0] if e[1] else pdfimg, zip(thumbs, files))

    urls = map(lambda u: u.replace('static/',''), urls)
    data = zip(urls, thumbs)

    print data
    return render(request, 'mosaico.html', {'data': data})

def random(request):
    acta = Acta.get_random()
    return HttpResponseRedirect(acta.get_url())

def get_filename(file_):
    name = file_.name
    extension = file_.name.split('.')
    extension = extension[-1]
    timestamp = time.time()
    filename = "%s%s" % (name, timestamp)
    filename = "%s.%s" % (hashlib.md5(filename).hexdigest(), extension)
    return filename

def subir(request):
    comunas = range(300)
    return render(request, 'upload.html', {'comunas': comunas})

def upload_file(request):
    if request.method == 'POST':

        if request.FILES['file'].size > 20*1024*1024 or not request.POST['g-recaptcha-response']:
            return HttpResponseRedirect('/actas/subir')
        person_name = request.POST.get('person_name', '')
        comuna = request.POST.get('comuna', '')
        try:
            date = request.POST.get('date', '')
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            date = date.date()
        except Exception as e:
            date = None
    
        filename = get_filename(request.FILES['file'])
        handle_uploaded_file(request.FILES['file'], filename)

        name, extension = filename.split('.')

        acta = Acta(
            name = name,
            static = filename,
            secret = hashlib.md5(str(time.time())).hexdigest(),
            person_name = person_name,
            date = date,
            comuna = comuna
        )
        acta.save()

        return render(request, 'success.html', {'url': acta.get_url()})
    else:
        return HttpResponseRedirect('/actas/subir')


def handle_uploaded_file(f, filename):
    with open(os.path.join(settings.ACTAS_DIRECTORY, filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def acta(request, name):
    acta = Acta.objects.filter(static = name).first()
    direct_url = acta.get_direct_url()
    valid = acta.valid
    if valid:
        return HttpResponseRedirect(direct_url)
    else:
        return render(request, 'not_yet.html')


def modify(request, filename, secret):
    acta = Acta.objects.filter(static = filename, secret = secret).first()
    if acta is None:
        raise Http404
    else:
        acta_number = acta.id
        return render(request, 'upload.html', {
            'modify': True, 'filename': filename, 'secret': secret, 'acta_number': acta_number,
        })

def handle_thumbnail(filename):

    name, extension = filename.split('.')
    filename = os.path.join(settings.BASE_DIR, 'static', 'acta', filename)
    name = os.path.join(settings.BASE_DIR, 'static', 'acta', name)
    command = ["convert", "-thumbnail","180", "%s[0]" % filename, "%s.png" % name]
    #print command
    exit_code = call(command)
    #print exit_code
    return exit_code


def upload_modify(request, filename, secret):
    if request.method == 'POST':
        acta = Acta.objects.filter(static = filename, secret = secret).first()
        if acta is None:
            raise Http404
        acta_number = acta.id
        

        name, extension = filename.split('.')
        filename = name+'.pdf'
        acta.static = filename
        acta.save()

        handle_uploaded_file(request.FILES['file'], filename)
        acta.valid = True
        acta.save()
        sp.set_modified(acta.sheet_row, acta.get_direct_url(), acta.get_modify_url())
        handle_thumbnail(filename)
        return render(request, 'success.html', {'url': acta.get_url(), 'modify': True, "acta_number":acta_number})
    else:
        return HttpResponseRedirect('/actas/subir')


    return None

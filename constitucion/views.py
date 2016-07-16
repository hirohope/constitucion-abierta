# -*- coding: UTF-8 -*-.
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

def wc(request):
    return render(request, 'wc.html')

def opendata(request):
    return render(request, 'opendata-cco.html')

def cabildos(request):
    return render(request, 'elegir-tipo-cabildo.html')

def cabildos_mesa(request):
    return render(request, 'subir-mesa-cabildo.html')

def cabildos_acta(request):
    return render(request, 'index.html')

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
    comunas = ["Aisén", "Algarrobo", "Alhué", "Alto Biobío", "Alto del Carmen", "Alto Hospicio", "Ancud", "Andacollo", "Angol", "Antofagasta", "Antuco", "Antártica", "Arauco", "Arica", "Buin", "Bulnes", "Cabildo", "Cabo de Hornos", "Cabrero", "Calama", "Calbuco", "Caldera", "Calera de Tango", "Calle Larga", "Camarones", "Camiña", "Canela", "Carahue", "Cartagena", "Casablanca", "Castro", "Catemu", "Cauquenes", "Cañete", "Cerrillos", "Cerro Navia", "Chaitén", "Chanco", "Chañaral", "Chiguayante", "Chile Chico", "Chillán", "Chillán Viejo", "Chimbarongo", "Cholchol", "Chonchi", "Chépica", "Cisnes", "Cobquecura", "Cochamó", "Cochrane", "Codegua", "Coelemu", "Coihaique", "Coihueco", "Colbún", "Colchane", "Colina", "Collipulli", "Coltauco", "Combarbalá", "Concepción", "Conchalí", "Concón", "Constitución", "Contulmo", "Copiapó", "Coquimbo", "Coronel", "Corral", "Coínco", "Cunco", "Curacautín", "Curacaví", "Curaco de Vélez", "Curanilahue", "Curarrehue", "Curepto", "Curicó", "Dalcahue", "Diego de Almagro", "Doñihue", "El Bosque", "El Carmen", "El Monte", "El Quisco", "El Tabo", "Empedrado", "Ercilla", "Estación Central", "Extranjero", "Florida", "Freire", "Freirina", "Fresia", "Frutillar", "Futaleufú", "Futrono", "Galvarino", "General Lagos", "Gorbea", "Graneros", "Guaitecas", "Hijuelas", "Hualaihué", "Hualañé", "Hualpén", "Hualqui", "Huara", "Huasco", "Huechuraba", "Illapel", "Independencia", "Iquique", "Isla de Maipo", "Isla de Pascua", "Juan Fernández", "La Calera", "La Cisterna", "La Cruz", "La Estrella", "La Florida", "La Granja", "La Higuera", "La Ligua", "La Pintana", "La Reina", "La Serena", "La Unión", "Lago Ranco", "Lago Verde", "Laguna Blanca", "Laja", "Lampa", "Lanco", "Las Cabras", "Las Condes", "Lautaro", "Lebu", "Licantén", "Limache", "Linares", "Litueche", "Llaillay", "Llanquihue", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Lolol", "Loncoche", "Longaví", "Lonquimay", "Los Andes", "Los Lagos", "Los Muermos", "Los Sauces", "Los Vilos", "Los Álamos", "Los Ángeles", "Lota", "Lumaco", "Machalí", "Macul", "Maipú", "Malloa", "Marchihue", "Mariquina", "María Elena", "María Pinto", "Maule", "Maullín", "Mejillones", "Melipeuco", "Melipilla", "Molina", "Monte Patria", "Mostazal", "Mulchén", "Máfil", "Nacimiento", "Nancagua", "Natales", "Navidad", "Negrete", "Ninhue", "Nogales", "Nueva Imperial", "Ñiquen", "Ñuñoa", "O'higgins", "Olivar", "Ollague", "Olmué", "Osorno", "Ovalle", "Padre Hurtado", "Padre las Casas", "Paihuano", "Paillaco", "Paine", "Palena", "Palmilla", "Panguipulli", "Panquehue", "Papudo", "Paredones", "Parral", "Pedro Aguirre Cerda", "Pelarco", "Pelluhue", "Pemuco", "Pencahue", "Penco", "Peralillo", "Perquenco", "Petorca", "Peumo", "Peñaflor", "Peñalolén", "Pica", "Pichidegua", "Pichilemu", "Pinto", "Pirque", "Pitrufquén", "Placilla", "Portezuelo", "Porvenir", "Pozo Almonte", "Primavera", "Providencia", "Puchuncaví", "Pucón", "Pudahuel", "Puente Alto", "Puerto Montt", "Puerto Octay", "Puerto Varas", "Pumanque", "Punitaqui", "Punta Arenas", "Puqueldón", "Purranque", "Purén", "Putaendo", "Putre", "Puyehue", "Queilén", "Quellón", "Quemchi", "Quilaco", "Quilicura", "Quilleco", "Quillota", "Quillón", "Quilpué", "Quinchao", "Quinta de Tilcoco", "Quinta Normal", "Quintero", "Quirihue", "Rancagua", "Rauco", "Recoleta", "Renaico", "Renca", "Rengo", "Requínoa", "Retiro", "Rinconada", "Romeral", "Ránquil", "Río Bueno", "Río Claro", "Río Hurtado", "Río Ibáñez", "Río Negro", "Río Verde", "Saavedra", "Sagrada Familia", "Salamanca", "San Antonio", "San Bernardo", "San Carlos", "San Clemente", "San Esteban", "San Fabián", "San Felipe", "San Fernando", "San Gregorio", "San Ignacio", "San Javier", "San Joaquín", "San José de Maipo", "San Juan de la Costa", "San Miguel", "San Nicolás", "San Pablo", "San Pedro", "San Pedro de Atacama", "San Pedro de la Paz", "San Rafael", "San Ramón", "San Rosendo", "San Vicente de Tagua Tagua", "Santa Bárbara", "Santa Cruz", "Santa Juana", "Santa María", "Santiago", "Santo Domingo", "Sierra Gorda", "Talagante", "Talca", "Talcahuano", "Taltal", "Temuco", "Teno", "Teodoro Schmidt", "Tierra Amarilla", "Tiltil", "Timaukel", "Tirúa", "Tocopilla", "Toltén", "Tomé", "Torres del Paine", "Tortel", "Traiguén", "Treguaco", "Tucapel", "Valdivia", "Vallenar", "Valparaíso", "Vichuquén", "Victoria", "Vicuña", "Vilcún", "Villa Alegre", "Villa Alemana", "Villarrica", "Vitacura", "Viña del Mar", "Yerbas Buenas", "Yumbel", "Yungay", "Zapallar"]
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


def quienes(request):
    return render(request, 'quienes.html')



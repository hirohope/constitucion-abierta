from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^mapa/$', views.mapa),
    url(r'^opendata-cco/$', views.opendata),
    url(r'^constitucion/acta/aleatorio/$', views.random),
    url(r'^constitucion/subir/$', views.subir),
    url(r'^constitucion/upload_file/$', views.upload_file),
    url(r'^constitucion/upload_modify/(?P<filename>\w+\.\w+)/(?P<secret>\w+)/$', views.upload_modify),
    url(r'^acta/(?P<name>\w+\.\w+)/$', views.acta),
    url(r'^acta/modificar/(?P<filename>\w+\.\w+)/(?P<secret>\w+)/$', views.modify),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

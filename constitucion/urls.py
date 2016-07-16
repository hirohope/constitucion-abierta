from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^mapa/$', views.mapa),
    url(r'^wc/$', views.wc),
    url(r'^opendata-cco/$', views.opendata),
    url(r'^quienes/$', views.quienes),
    url(r'^actas/mosaico/$', views.mosaico),
    url(r'^actas/aleatorio/$', views.random),
    url(r'^actas/subir/$', views.subir),
    # cabildos
    url(r'^cabildos/$', views.cabildos),
    url(r'^cabildos/mesa/$', views.cabildos_mesa),
    url(r'^cabildos/acta/$', views.cabildos_acta),

    url(r'^acta/(?P<name>\w+\.\w+)/$', views.acta),
    url(r'^acta/modificar/(?P<filename>\w+\.\w+)/(?P<secret>\w+)/$', views.modify),
    url(r'^constitucion/upload_file/$', views.upload_file),
    url(r'^constitucion/upload_modify/(?P<filename>\w+\.\w+)/(?P<secret>\w+)/$', views.upload_modify),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

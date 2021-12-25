from django.urls import path
from . import views
from django.conf.urls import include
app_name = 'catalog'

urlpatterns = [
        path( '', views.index, name='index'),
#        path( 'translator/', include('translator.urls', namespace='translator')),
]

from django.urls import path
from django.conf import settings
#from django.conf.urls.static import static

from . import views

app_name = 'firstapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('second', views.second, name='second'),
    path('results', views.results, name='results')
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

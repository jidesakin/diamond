from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views
from .views import home, register


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^register/', views.register, name='register')
]
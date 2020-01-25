from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^contact/$', views.contact_view, name='contact'),
]
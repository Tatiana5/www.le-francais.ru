from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'verbs_autocomplete/.{0,50}?$', views.get_autocomplete_list, name='autocomplete'),
    url(r'search/$', views.search, name='search'),
    url(r'verb/(?P<feminin>feminin_)?(?P<se>se_)?(?P<verb>.{1,30})$', views.verb, name='verb'),
    url(r'$', views.index),
]



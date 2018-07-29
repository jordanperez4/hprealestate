from django.conf.urls import url

from . import views

app_name = 'PropertyFinder'
urlpatterns = [
    url(r'House/(?P<search_text>.+?)/$', views.house, name='house'),
    url(r'$', views.index, name='index')

]
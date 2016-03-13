from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^news/$', views.show_all_news, name='views.show_all_news'),
    url(r'^actors/$', views.actors_list, name='views.actors_list'),
    url(r'^$', views.film_list, name='film_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.film_list, name='film_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.film_detail, name='film_detail'),
    url(r'^actors/(?P<slug>[-\w]+)/$', views.actor_info, name='actor_info'),
    url(r'^news/(?P<slug>[-\w]+)/$', views.news_info, name='news_info'),
]

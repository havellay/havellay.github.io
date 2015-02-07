from django.conf.urls import patterns, url

from oldgold import views

urlpatterns = patterns('',
    # ex: /oldgold/
    url(r'^$', views.index, name='index'),
    # ex: /oldgold/5/
    url(r'^(?P<item_id>\d+)/$', views.detail, name='detail')

    # # ex: /oldgold/
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # # ex: /oldgold/5/
    # url(r'^(?P<item_id>\d+)/$', views.DetailView.as_view(), name='detail'),
)

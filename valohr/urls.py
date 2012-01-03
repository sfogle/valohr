from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('valohr.views',
    #url(r'^$', 'index'),
    #url(r'^(?P<poll_id>\d+)/$', 'detail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
    url(r'^$', 'index'),
    #url(r'^(?P<room_name>\d+', 'detail'),
    #url(r'^(?P<room_name>[0-9A-Za-z-_.//]+)$', 'detail'),
    url(r'^(?P<room_name>[0-9A-Za-z-_.//]+)$', 'detail'),
)

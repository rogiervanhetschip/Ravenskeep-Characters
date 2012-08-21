from django.conf.urls import patterns, include, url

urlpatterns = patterns('chars.views',
    url(r'^$', 'home'),
    url(r'^char/(?P<char_id>\d+)/$', 'char')
)


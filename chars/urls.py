from django.conf.urls import patterns, include, url

urlpatterns = patterns('chars.views',
    url(r'^$', 'home'),
    url(r'^char/(?P<char_id>\d+)/$', 'charRead'),
    url(r'^char/(?P<char_id>\d+)/create$', 'charCreate'),
    url(r'^char/(?P<char_id>\d+)/read$', 'charRead'),
    url(r'^char/(?P<char_id>\d+)/printpreview$', 'charPrintPreview'),
    url(r'^char/(?P<char_id>\d+)/edit$', 'charEdit'),
    url(r'^char/(?P<char_id>\d+)/delete$', 'charDelete'),

    # Logout
    (r'^logout/$', 'logout_user'),

)

urlpatterns += patterns('',
    # Login
    (r'^login/$', 'django.contrib.auth.views.login'),
)


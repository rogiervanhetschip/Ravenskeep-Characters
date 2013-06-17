from django.conf.urls import patterns, include, url

urlpatterns = patterns('chars.views',
    url(r'^$', 'home', name='home'),
    url(r'^char/(?P<char_id>\d+)/$', 'charRead', name='charRead'),
    # url(r'^char/(?P<char_id>\d+)/create$', 'charCreate', name='charCreate'),
    url(r'^char/(?P<char_id>\d+)/read/$', 'charRead', name='charRead'),
    url(r'^char/(?P<char_id>\d+)/printpreview/$', 'charPrintPreview', name='charPrintPreview'),
    # url(r'^char/(?P<char_id>\d+)/edit$', 'charEdit', name='charEdit'),
    # url(r'^char/(?P<char_id>\d+)/delete$', 'charDelete', name='charDelete'),

    # Logout
    url(r'^logout/$', 'logout_user', name='logout'),

)

urlpatterns += patterns('',
    # Login
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
)


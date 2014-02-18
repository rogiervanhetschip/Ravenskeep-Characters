from django.conf.urls import patterns, include, url

urlpatterns = patterns('chars.views',
    url(r'^$',                                    'home',              name='home'),
    url(r'^char/(?P<char_id>\d+)/$',              'charRead',          name='charRead'),
    url(r'^char/new$',                            'charNew',           name='charNew'),
    url(r'^char/(?P<char_id>\d+)/printpreview/$', 'charPrintPreview',  name='charPrintPreview'),
    url(r'^char/printpreview/$',                  'charsPrintPreview', name='charsPrintPreview'),
  # url(r'^char/(?P<char_id>\d+)/delete$',        'charDelete',        name='charDelete'),
    url(r'^char/(?P<char_id>\d+)/pdf/$',          'charPdf',           name='charPdf'),
    url(r'^char/pdf/$',                           'charsPdf',          name='charsPdf'),

    # Logout
    url(r'^logout/$', 'logout_user', name='logout'),

)

urlpatterns += patterns('',
    # Login
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
)


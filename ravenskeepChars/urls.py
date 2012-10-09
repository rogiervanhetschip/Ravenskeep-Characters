from django.conf.urls import patterns, include, url
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ravenskeepChars.views.home', name='home'),
    # url(r'^ravenskeepChars/', include('ravenskeepChars.foo.urls')),
    url(r'^ravenskeepChars/', include('chars.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Required to make static serving work
    # http://twigstechtips.blogspot.nl/2009/08/django-how-to-serve-media-files-css.html
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    # This is the entry you'd need if you just wanted to serve a proxy.
    # You'll need to create another site if you want to serve this alongside
    # other content.
    #(r'^', include('eve_proxy.urls')),
)

# If you'd like to serve media files via Django (strongly not recommended!),
# open up your settings.py file and set SERVE_MEDIA to True. This is
# appropriate on a developing site, or if you're running Django's built-in
# test server. Normally you want a webserver that is optimized for serving
# static content to handle media files (apache, lighttpd).
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT}),
    )
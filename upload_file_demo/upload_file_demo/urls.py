from django.conf.urls import patterns, include, url
from django.contrib import admin
import upload.views, settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upload_file_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', upload.views.upload),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)

from django.conf.urls import patterns, include, url

from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'egteduc.views.home', name='home'),
    # url(r'^egteduc/', include('egteduc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gteducsite.views.index'),
    url(r'^empresa/','gteducsite.views.empresa'),
    url(r'^produtoservicos/','gteducsite.views.produtoservicos'),
    url(r'^clientes/','gteducsite.views.clientes'),
    url(r'^suporte/','gteducsite.views.suporte'),
    url(r'^parceiros/','gteducsite.views.parceiros'),
    url(r'^contatos/','gteducsite.views.contatos'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static-egteduc/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )


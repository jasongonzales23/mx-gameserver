from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from gameserver.views import gameResults, teamResults, teamData, home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mxgameserver.views.home', name='home'),
    # url(r'^mxgameserver/', include('mxgameserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^game-results/$', gameResults),
    url(r'^game-results/(?P<slug>[^\.]+)$', teamResults),
    
    #this should be the real URL eventually
    #url(r'^team-data/(?<teamID>[^\.]+)$', teamData),
    
    #test URL
    url(r'^teamData/$', teamData),
    url(r'^test/$', direct_to_template, {'template': 'test.html'}),
    url(r'^clear/$', direct_to_template, {'template': 'clear.html'}),
    url(r'^accounts/', include('registration.urls')),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
    
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)
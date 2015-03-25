from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^update_stops/$', 'a2b.views.update_stops', name='update_stops'),
    url(r'^update_stops/success/$', 'a2b.views.update_success', name='update_stops_success'),
    url(r'^update_stops/error/$', 'a2b.views.update_error', name='update_stops_error'),

    url(r'^search_routes/$', 'a2b.views.search_routes', name='search_routes')
    # url(r'^blog/', include('blog.urls')),

    #url(r'^logPoint/', include(logPoint.urls)),
)


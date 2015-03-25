from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pointLog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^a2b/', include('a2b.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

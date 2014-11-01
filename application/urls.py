from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^api/', include('core.api_urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('uploads.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

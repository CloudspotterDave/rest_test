from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from uploads import views

urlpatterns = patterns('',
    url(r'^uploads/$', views.UploadList.as_view()),
    url(r'^uploads/(?P<pk>[0-9]+)/$', views.UploadDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)


from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^employee/', include('employee.urls')),
    url(r'^$', 'hello.views.home'),
    url(r'^dashboard', 'hello.views.dashboard'),
)

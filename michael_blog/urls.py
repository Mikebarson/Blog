from django.conf.urls import include, url
from django.contrib.auth import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'michael_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page' : '/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls')),
]

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'avto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'avto.views.Hararteristiki1'),
    url(r'^lol/', 'avto.views.Hararteristiki'),
    url(r'^engine/', 'avto.views.engine'),
    url(r'^base/', 'avto.views.base'),

]

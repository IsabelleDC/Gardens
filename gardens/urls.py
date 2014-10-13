from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from gardens import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gardens.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gardens_app.views.home', name='home'),

    # REGISTRATION
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^register/$', 'gardens_app.views.register', name='register'),


    url(r'^profile/$', 'gardens_app.views.profile', name='profile'),
    # url(r'^index/$', 'gardens_app.views.index', name='index'),

    url(r'^view_rss/$', 'gardens_app.views.view_rss', name='view_rss'),
    url(r'^add_rss/$', 'gardens_app.views.add_rss', name='add_rss'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
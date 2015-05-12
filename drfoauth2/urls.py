from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from .viewsets import UserViewSet, GroupViewSet
from .views import SignUp, Login

from .signals import Noop

from . import views

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'user')
router.register(r'groups', GroupViewSet, 'group')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^home/$', views.home, name='home'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),

    # from http://www.yeti.co/blog/oauth2-with-django-rest-framework/
    url(r'^sign_up/$', SignUp.as_view()),
    url(r'^login/$', Login.as_view(), name="login"),
)

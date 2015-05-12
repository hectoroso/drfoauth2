# from http://www.yeti.co/blog/oauth2-with-django-rest-framework/

from rest_framework import permissions

class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)
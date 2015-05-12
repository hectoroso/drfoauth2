# from http://www.yeti.co/blog/oauth2-with-django-rest-framework/
from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from .permissions import IsAuthenticatedOrCreate
from .serializers import SignUpSerializer, LoginSerializer

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class Login(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = (BasicAuthentication,)

    def get_object(self):
        return self.request.user

def profile(request):
    return render(request, 'profile.html', {})

import os
from django.http import HttpResponse

def home(request):
    output = '<html><body>'

    output += "<p>Hello from Django, try out <a href='/admin/'>/admin/</a></p>"
    output += "<h4>Environment Variables</h4>"

    output += "<table>"
    keys = list(os.environ.keys())
    keys.sort()
    for key in keys:
        output += "<tr><td>" + key + "</td><td>= " + os.environ[key] + "</td></tr>"
    output += "</table>"

    #if not environ['mod_wsgi.process_group']:
    #    output += '<p>EMBEDDED MODE</p>'
    #else:
    #    output += '<p>DAEMON MODE</p>'

    output += os.path.dirname(__file__) + "<br/>"
    output += os.path.dirname(os.path.dirname(__file__)) + "<br/>"
    output += os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "<br/>"
    output += '</body></html>'

    return HttpResponse(output)
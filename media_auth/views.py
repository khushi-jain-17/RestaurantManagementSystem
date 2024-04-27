from django.shortcuts import redirect, render
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.generics import GenericAPIView
from .serializers import GoogleSocialAuthSerializer
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from urllib.parse import urlencode
from django.contrib.auth import logout 
from django.http import HttpResponseBadRequest
import requests



class GoogleSocialAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)



def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("/")

# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.http import Http404
from .serializers import *

#Team
class TeamView(generics.ListCreateAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer

#School
class SchoolView(generics.ListCreateAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

#Kid
class KidView(generics.ListCreateAPIView):
	queryset = Kid.objects.all()
	serializer_class = KidSerializer

class KidDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Kid.objects.all()
	serializer_class = KidSerializer

#Bitacora
class BitacoraView(generics.ListCreateAPIView):
	queryset = Bitacora.objects.all()
	serializer_class = BitacoraSerializer

class BitacoraDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bitacora.objects.all()
	serializer_class = BitacoraSerializer
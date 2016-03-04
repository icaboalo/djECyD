# -*- encoding: utf-8 -*-
import django_filters
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, filters
from django.http import Http404
from .serializers import *


#Team
class TeamView(generics.ListCreateAPIView):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ('name', 'school__name', 'grade')
	ordering_fields = '__all__'
	ordering = ('name',)

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

#Leader
class LeaderView(generics.ListCreateAPIView):
	queryset = Leader.objects.all()
	serializer_class = LeaderSerializer

class LeaderDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Leader.objects.all()
	serializer_class = LeaderSerializer

#User
class UserView(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
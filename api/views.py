# -*- encoding: utf-8 -*-
import django_filters
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, filters, permissions
from django.http import Http404
from .serializers import *


#Team
class TeamView(generics.ListCreateAPIView):
	"""
	Listado de equipos y creacion de de objeto
	"""

	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ('name', 'grade')
	ordering_fields = '__all__'
	ordering = ('name',)

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Un equipo y actualizacion
	"""

	queryset = Team.objects.all()
	serializer_class = TeamSerializer

#School
class SchoolView(generics.ListCreateAPIView):
	"""
	Listado de escuelas y creacion de de objeto
	"""

	queryset = School.objects.all()
	serializer_class = SchoolSerializer
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ('name',)
	ordering_fields = '__all__'
	ordering = ('name',)

class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Una escuela y actualizacion
	"""

	queryset = School.objects.all()
	serializer_class = SchoolSerializer

#Kid
class KidView(generics.ListCreateAPIView):
	"""
	Listado de niños y creacion de de objeto
	"""

	queryset = Kid.objects.all()
	serializer_class = KidSerializer
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ('name', 'last_name', 'team__grade')
	ordering_fields = '__all__'
	ordering = ('name',)

class KidDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Un niño y actualizacion
	"""

	queryset = Kid.objects.all()
	serializer_class = KidSerializer

#Bitacora
class BitacoraView(generics.ListCreateAPIView):
	"""
	Listado de bitacoras y creacion de de objeto
	"""

	queryset = Bitacora.objects.all()
	serializer_class = BitacoraSerializer
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ('kid__name',)
	ordering_fields = ('date',)
	ordering = ('date',)

class BitacoraDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Una bitacora y actualizacion
	"""

	queryset = Bitacora.objects.all()
	serializer_class = BitacoraSerializer

#Leader
class LeaderView(generics.ListCreateAPIView):
	"""
	Listado de responsable y creacion de de objeto
	"""

	queryset = Leader.objects.all()
	serializer_class = LeaderSerializer
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ('name', 'last_name', 'grade', 'school__name', 'team__name')
	ordering_fields = '__all__'
	ordering = ('name',)

class LeaderDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Un responsable y actualizacion
	"""

	queryset = Leader.objects.all()
	serializer_class = LeaderSerializer

#User
class UserView(generics.ListCreateAPIView):
	"""
	Listado de usuarios y creacion de de objeto
	"""

	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
	search_fields = ('first_name', 'last_name', 'username')
	ordering_fields = '__all__'
	ordering = ('first_name',)
	# def get_queryset(self):
	# 	"""
	# 	This view should return only the user login.
	# 	"""
	# 	user = self.request.user
	# 	return User.objects.filter(id=user.id)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Un usuario y actualizacion
	"""

	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserRegister(generics.CreateAPIView):
	model = User
	permission_classes = [permissions.AllowAny]
	serializer_class = UserRegisterSerializer
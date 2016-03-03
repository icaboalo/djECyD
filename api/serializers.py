# -*- encoding:utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from team.models import *
from school.models import *

#DefaultSerializers
class DefaultUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DefaultBitacoraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bitacora
		fields = ['id', 'assistance', 'week_talk', 'date']

class DefaultKidSerializer(serializers.ModelSerializer):

	bitacora = DefaultBitacoraSerializer(many=True, read_only=True)

	class Meta:
		model = Kid
		fields = ['id', 'name', 'last_name', 'bitacora']

class DefaultSchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = ['id', 'name']

class DefaultLeaderSerializer(serializers.ModelSerializer):
	school = DefaultSchoolSerializer(many=False, read_only=True)

	class Meta:
		model = Leader
		fields = ['id', 'name', 'last_name', 'grade', 'school']

class DefaultTeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ['id', 'name', 'grade']

#Team Serializers
class TeamSerializer(serializers.ModelSerializer):
	school = DefaultSchoolSerializer(many=False, read_only=True)
	kids = DefaultKidSerializer(many=True, read_only=True)
	leaders = DefaultLeaderSerializer(many=True, read_only=True)
	user = DefaultUserSerializer(many=False, read_only=True)

	user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')
	school_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=School.objects.all(), source='school')
	class Meta:
		model = Team
		fields = ['id', 'name', 'grade', 'school', 'school_id', 'kids', 'user', 'user_id', 'leaders']

#School Serializers
class SchoolLeaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leader
		fields = ['id', 'name', 'last_name', 'grade']


class SchoolSerializer(serializers.ModelSerializer):
	teams = DefaultTeamSerializer(many=True, read_only=True)
	leaders = SchoolLeaderSerializer(many=True, read_only=True)
	class Meta:
		model = School
		fields = ['id', 'name', 'teams', 'leaders']

#Kid Serializers
class KidSerializer(serializers.ModelSerializer):
	bitacoras = DefaultBitacoraSerializer(many=True, read_only=True)
	team = DefaultTeamSerializer(many=False, read_only=True)

	team_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Team.objects.all(), source='team')
	class Meta:
		model = Kid
		fields = ['id', 'name', 'last_name', 'bitacoras', 'team', 'team_id']

#Bitacora Serializers
class BitacoraKidSerializer(serializers.ModelSerializer):
	class Meta:
		model = Kid
		fields = ['id', 'name', 'last_name']

class BitacoraSerializer(serializers.ModelSerializer):
	kid = BitacoraKidSerializer(many=False, read_only=True)

	kid_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Kid.objects.all(), source='kid')
	class Meta:
		model = Bitacora
		fields = ['id', 'assistance', 'week_talk', 'date', 'kid', 'kid_id']

#Leader Serializers
class LeaderSerializer(serializers.ModelSerializer):

	school = DefaultSchoolSerializer(many=False, read_only=True)
	team = DefaultTeamSerializer(many=False, read_only=True)

	school_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=School.objects.all(), source='school')
	team_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=School.objects.all(), source='team')

	class Meta:
		model = Leader
		fields = ['id', 'name', 'last_name', 'school', 'school_id', 'team', 'team_id']

#User Serializers
class UserTeamSerializer(serializers.ModelSerializer):
	kids = BitacoraKidSerializer(many=True, read_only=True)

	class Meta:
		model = Team
		fields = ['id', 'name', 'grade', 'kids']


class UserSerializer(serializers.ModelSerializer):
	teams = UserTeamSerializer(many=True, read_only=True)

	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'teams']
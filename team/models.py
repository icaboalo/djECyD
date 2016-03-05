from django.db import models
from django.template import defaultfilters
from utils.choices import GRADE_CHOICES
from school.models import *
from django.contrib.auth.models import User

#for auth_token
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

# Create your models here.
class Team(models.Model):

	class Meta:
		verbose_name = "Team"
		verbose_name_plural = "Teams"
	
	#Relations
	school = models.ForeignKey(School, related_name='teams')
	user = models.ForeignKey(User, related_name='teams')

	#Attributes
	name = models.CharField(max_length = 50, blank = False)
	grade = models.CharField(max_length =  50, blank = False, choices = GRADE_CHOICES)
	slug = models.SlugField(max_length=102, blank=True, unique=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.name + self.grade)
		super(Team, self).save(*args, **kwargs)

class Leader(models.Model):

	class Meta:
		verbose_name = "Leader"
		verbose_name_plural = "Leaders"

	#Attributes
	name = models.CharField(max_length = 50, blank = False)
	last_name = models.CharField(max_length=100, blank=False)
	grade = models.CharField(max_length = 50, blank=False, choices=GRADE_CHOICES)
	slug = models.SlugField(max_length=152, blank = True, unique=True)

	#Relations
	school = models.ForeignKey(School, blank = False, related_name='leaders')
	team = models.ForeignKey(Team, blank=False, related_name='leaders')

	def __str__(self):
		return (self.name)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.name + self.last_name)
		super(Leader, self).save(*args, **kwargs)

class Kid(models.Model):
	class Meta:
		verbose_name = "Kid"
		verbose_name_plural = "Kids"
	
	#Relations
	team = models.ForeignKey(Team, related_name='kids')

	#Attributes
	name = models.CharField(max_length = 50, blank = False)
	last_name = models.CharField(max_length = 100, blank = False)
	slug = models.SlugField(max_length=152, blank=True, unique=True)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.name + self.last_name)
		super(Kid, self).save(*args, **kwargs)


	def __str__(self):
		return (self.name)

class Bitacora(models.Model):

    class Meta:
        verbose_name = "Bitacora"
        verbose_name_plural = "Bitacoras"

    #Relations
    kid = models.ForeignKey(Kid, related_name='bitacoras')

    #Attributes
    assistance = models.BooleanField(blank=True)
    week_talk = models.BooleanField(blank=True)
    date = models.DateField(blank=False, auto_now=True)

    def __str__(self):
    	return (self.kid.name + " " + str(self.date))
    
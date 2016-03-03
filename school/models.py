from django.db import models
from django.template import defaultfilters

# Create your models here.
class School(models.Model):

	class Meta:
		verbose_name = "School"
		verbose_name_plural = "Schools"

	#Attributes
	name = models.CharField(max_length = 50, blank = False)
	slug = models.SlugField(max_length = 52, blank=True, unique=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.name)
		super(School, self).save(*args, **kwargs)

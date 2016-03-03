from django import forms
from .models import *

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'school', 'grade', 'user']
    
class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['name', 'last_name', 'team', 'assistance', 'week_talk']
    
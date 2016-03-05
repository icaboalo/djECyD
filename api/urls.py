from django.conf.urls import url
from . import views as api_view
from rest_framework.authtoken import views as token_view

urlpatterns = [
	
	#Token url
	url(r'register/', api_view.UserRegister.as_view(), name='register'),
	url(r'^login/', token_view.obtain_auth_token),

	#Team urls
	url(r'^team/$', api_view.TeamView.as_view(), name='team_api'),
	url(r'^team/(?P<pk>[0-9]+)/$', api_view.TeamDetailView.as_view(), name='team_api_detail'),

	#School urls
	url(r'^school/$', api_view.SchoolView.as_view(), name='school_api'),
	url(r'^school/(?P<pk>[0-9]+)/$', api_view.SchoolDetailView.as_view(), name='school_api_detail'),

	#Kid urls
	url(r'^kid/$', api_view.KidView.as_view(), name='kid_api'),
	url(r'^kid/(?P<pk>[0-9]+)/$', api_view.KidDetailView.as_view(), name='kid_api_detail'),

	#Bitacora urls
	url(r'bitacora/$', api_view.BitacoraView.as_view(), name='bitacora_api'),
	url(r'bitacora/(?P<pk>[0-9]+)/$', api_view.BitacoraDetailView.as_view(), name='bitacora_api_detail'),

	#Leader urls
	url(r'leader/$', api_view.LeaderView.as_view(), name='leader_api'),
	url(r'leader/(?P<pk>[0-9]+)/$', api_view.LeaderDetailView.as_view(), name='leader_api_detail'),

	#Leader urls
	url(r'user/$', api_view.UserView.as_view(), name='user_api'),
	url(r'user/(?P<pk>[0-9]+)/$', api_view.UserDetailView.as_view(), name='user_api_detail'),
]
from django.conf.urls import url
from . import views

urlpatterns = [
	#Team urls
	url(r'^team/$', views.TeamView.as_view(), name='team_api'),
	url(r'^team/(?P<pk>[0-9]+)/$', views.TeamDetailView.as_view(), name='team_api_detail'),

	#School urls
	url(r'^school/$', views.SchoolView.as_view(), name='school_api'),
	url(r'^school/(?P<pk>[0-9]+)/$', views.SchoolDetailView.as_view(), name='school_api_detail'),

	#Kid urls
	url(r'^kid/$', views.KidView.as_view(), name='kid_api'),
	url(r'^kid/(?P<pk>[0-9]+)/$', views.KidDetailView.as_view(), name='kid_api_detail'),

	#Bitacora urls
	url(r'bitacora/$', views.BitacoraView.as_view(), name='bitacora_api'),
	url(r'bitacora/(?P<pk>[0-9]+)/$', views.BitacoraDetailView.as_view(), name='bitacora_api_detail'),

	#Leader urls
	url(r'leader/$', views.LeaderView.as_view(), name='leader_api'),
	url(r'leader/(?P<pk>[0-9]+)/$', views.LeaderDetailView.as_view(), name='leader_api_detail'),

		#Leader urls
	url(r'user/$', views.UserView.as_view(), name='user_api'),
	url(r'user/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user_api_detail'),
]
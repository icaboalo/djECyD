"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from school.views import *
from team.views import *

urlpatterns = [
    #admin
    url(r'^admin/', admin.site.urls),

    #index
    url(r'^$', Index.as_view(), name = 'home'),
    
    #school
    url(r'^school/$', SchoolListView.as_view(), name = 'school_index'),
    url(r'^school/detail/(?P<slug>[-\w]+)/$', SchoolDetail.as_view(), name='school_detail'),
    url(r'^school/new/', SchoolCreate.as_view(), name = 'school_create'),
    url(r'^school/update/(?P<slug>[-\w]+)/$', SchoolUpdate.as_view(), name='school_update'),
    url(r'^school/delete/(?P<slug>[-\w]+)/$', SchoolDelete.as_view(), name='school_delete' ),
    
    #team
    url(r'^team/$', TeamListView.as_view(), name = 'team_index'),
    url(r'^team/detail/(?P<slug>[-\w]+)/$', TeamDetail.as_view(), name='team_detail'),
    url(r'^team/new/', TeamCreate.as_view(), name = 'team_create'),
    url(r'^team/update/(?P<slug>[-\w]+)/$', TeamUpdate.as_view(), name = 'team_update'),
    url(r'^team/delete/(?P<slug>[-\w]+)/$', TeamDelete.as_view(), name = 'team_delete'),
    
    #kid
    url(r'^kid/$', KidListView.as_view(), name = 'kid_index'),
    url(r'^kid/detail/(?P<slug>[-\w]+)/$', KidDetail.as_view(), name='kid_detail'),
    url(r'kid/new/', KidCreate.as_view(), name = 'kid_create'),
    url(r'^kid/update/(?P<slug>[-\w]+)/$', KidUpdate.as_view(), name='kid_update'),
    url(r'^kid/delete/(?P<slug>[-\w]+)/$', KidDelete.as_view(), name='kid_delete'),
    
    #leader
    url(r'^leader/$', LeaderListView.as_view(), name = 'leader_index'),
    url(r'^leader/detail/(?P<slug>[-\w]+)/$', LeaderDetail.as_view(), name = 'leader_detail'),
    url(r'^leader/new/', LeaderCreate.as_view(), name = 'leader_create'),
    url(r'^leader/update/(?P<slug>[-\w]+)/$', LeaderUpdate.as_view(), name = 'leader_update'),
    url(r'^leader/delete/(?P<slug>[-\w]+)/$', LeaderDelete.as_view(), name = 'leader_delete'),
]

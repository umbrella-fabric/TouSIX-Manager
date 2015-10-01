"""web_TouSIX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Statistics_Manager.views import StatsMembersList, RestrictedStats
from Rules_Generation.views import SelectionSwitchView
from Log_Controller.views import AsyncEventView, ShowEventView
from Log_Statistics.views import RecieveStatsForm
from Member_Manager import urls as members_urls
from Rules_Deployment.views import RulesDeploymentConfirmView, RulesRestorationView
from Authentication.views import RegisterView
from Administration.admin import admin_tousix
urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tousix/', include(admin_tousix.urls)),
    url(r'^members/stats/list', StatsMembersList.as_view(), name='charts'),
    url(r'^event/', AsyncEventView.as_view(), name='Async event log'),
    url(r'^member', include(members_urls)),
    url(r'^stats/reply', RecieveStatsForm.as_view(), name='Recieve stats'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^deployment/rules/confirm', RulesDeploymentConfirmView.as_view(), name='rules_confirm'),
    url(r'^deployment/rules/ask', RulesRestorationView.as_view(), name='rules_ask'),
    url(r'^', RestrictedStats.as_view(), name='restricted stats'),

]

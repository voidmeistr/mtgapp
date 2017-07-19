from django.conf.urls import url
from . import views

app_name = 'magic'

urlpatterns = [
	#home page
	url(r'^$', views.IndexView.as_view(), name='index'),
	#registration page
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	#logout
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	#login
    url(r'^login_user/$', views.login_user, name='login_user'),
	#Post detail , /1/ ,/123/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
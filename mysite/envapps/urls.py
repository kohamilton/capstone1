from django.urls import path
from . import views

app_name = 'envapps'
urlpatterns = [
    path('', views.storm_apps, name="storm_apps"),
    path('ossf_app/', views.ossf_app, name="ossf_app"),
	#path('/home/createaccount/', views.signup_view, name = "signup")
	#path('/accounts/login', views.login_view, name = "login")
	#path('/accounts/logout', views.logout_view, name = "logout")
]

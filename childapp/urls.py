from django.urls import path
from django.conf.urls import url
from . import views

app_name = "childapp"
urlpatterns = [
    path("", views.frontpage, name='frontpage'),
    path("about/", views.aboutapp, name='aboutapp'),
    path("contactUs/", views.contactus, name='contactUs'),
    path("services/", views.services, name='services'),
    path("carear/", views.carear, name='carear'),
    path("signup/", views.signUp, name='signUp'),
    path("logout/", views.logout_request, name='logout_request'),
    path("blog/", views.blog, name='blog'),
    path("<int:sno>/", views.single, name='single'),
    path("login/", views.login_request, name='login_request'),

    # path("signup2/", views.signUp2, name='signUp2'),
]

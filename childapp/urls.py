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
    # path("signup/", views.signUp, name='signUp'),
    path("logout/", views.logout_request, name='logout_request'),
    # path("blog/", views.blog, name='blog'),
    # path("<int:post_sno>/", views.single, name='single'),
    path("login/", views.login_request, name='login_request'),
    path("login2/", views.login_request2, name='login2'),
    path("eCategories/", views.emailCategories, name='eCategories'),
    path("eContactUs/", views.eContactUs, name='eContactUs'),
    path("email<int:contact_s_no>/", views.eCdetail, name='eCdetail'),
    path("eQuesAsked/", views.eQueAsked, name='eQuesAsked'),
    path("ques<int:que_s_no>/", views.eQuesdetails, name='eQdetails'),

    
]

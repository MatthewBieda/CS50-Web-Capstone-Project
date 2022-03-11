from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", views.lgin.as_view(), name="login"),
    path("logout/", views.lgout.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("articles/", views.listarticles.as_view(), name="articles"),
    path("articles/<pk>", views.detailarticle, name="article_detail"),
    path("newarticle/", views.newarticle.as_view(), name="newarticle"),
    path("readinglist/", views.readinglist, name="readinglist"),
]
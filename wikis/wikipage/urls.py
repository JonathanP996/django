from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("editpage/<str:title>", views.editPAGE, name="edit_page"),
    path("random_page", views.GETrandomPage, name="random_page"),
    path("searchpage", views.searchPAGE, name="search"),
    path("addpage", views.addPAGE, name="add_page"),


]
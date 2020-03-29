from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path("episode/", views.show_episode, name="show_episode"),
    path("character/", views.show_character, name="show_character"),
    path("location/", views.show_location, name="show_location"),
    path("search/", views.show_search, name="show_search"),
]

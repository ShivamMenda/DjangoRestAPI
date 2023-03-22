from . import views
from django.urls import path

urlpatterns = [
   path("home/",views.homepage,name="home") ,
   path("posts/",views.listPosts),
   path("create_post/",views.create_post)
]

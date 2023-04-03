from . import views
from django.urls import path

urlpatterns = [
   path("home/",views.homepage,name="home") ,
   path("posts/",views.listPosts),
   path("create_post/",views.create_post),
   path("post_by_id/<int:post_id>",views.post_by_id),
   path("update_post/<int:post_id>",views.update_post,name='update_post'),
   path("delete_post/<int:post_id>",views.delete_post)
]

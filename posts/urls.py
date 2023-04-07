from . import views
from django.urls import path

urlpatterns = [
   path("home/",views.homepage,name="home") ,
   path("create_or_list_posts/",views.PostListCreateView.as_view()),
   path("retrieve_update_delete_post_by_id/<int:post_id>",views.PostRetreiveUpdateDeleteView.as_view()),
]

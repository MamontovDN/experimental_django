from django.urls import path

from posts import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:category_id>/',
         views.PostByCategory.as_view(),
         name='category'
         ),
    path('post/<int:post_id>/', views.PostView.as_view(), name='single_post'),
    path('add-post/', views.CreatePost.as_view(), name='add_post'),
    path('delete-post/<int:pk>/', views.DeletePost.as_view(), name='del_post'),
    path('update-post/<int:pk>/', views.UpdatePost.as_view(), name='upd_post'),
]

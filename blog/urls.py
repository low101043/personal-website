from django.urls import path
from . import views
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_new, name='post_new'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/', views.post_list_new_to_old, name='post_list_new'),
    path('cv/', views.cv_page, name='cv_page'),
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('about/', views.info_page, name='about_me'),
    path('blog/old', views.post_list_old_to_new, name='post_list_old'),
    path('pdf/', views.pdf_view, name='pdf'),

]

#if settings.DEBUG:
#        urlpatterns += static(settings.MEDIA_URL,
#                              document_root=settings.MEDIA_ROOT)
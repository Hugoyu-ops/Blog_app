from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('all_post/', views.AllList.as_view(), name='all_post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

]
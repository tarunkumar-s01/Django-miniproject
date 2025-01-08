from django.urls import path,include
from .import views

app_name='blogs'
urlpatterns = [
    path('index',views.index,name='course'),
    path('path',views.page,name='home'),
    path('detail/<int:post_id>',views.detail,name='detail'),
    path('form',views.forms,name='form'),
    path('about',views.about,name='about')
]

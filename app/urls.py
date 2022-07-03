from . import views
from django.urls import path
urlpatterns = [
    path('base/',views.base),
    path('',views.home),
    path('blogs/',views.blogs),
    path('blog/',views.blog),
    path('footer/',views.footer),
    path('login/',views.login),
]

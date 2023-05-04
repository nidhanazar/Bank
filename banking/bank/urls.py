from django.urls import path

from bank import views
from .views import login, register



app_name = 'bank'

urlpatterns = [
    path('',views.HomeView,name='home'),
    path("login/", views.login,name="user_login"),
    path("register/", views.register,name="user_registration"),
    path("new/",views.new,name="new_page"),
    path("form/",views.form,name='form'),
    path('logout',views.logout,name='logout')
    # path("/", branches.as_view(),name="user_registration"),
]
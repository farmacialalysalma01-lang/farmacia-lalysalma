from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from farmacia import views

urlpatterns = [
    path('', views.home, name='home'),

    # LOGIN e LOGOUT
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ADMIN DJANGO
    path('admin/', admin.site.urls),
]


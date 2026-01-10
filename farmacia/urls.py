from .views import setup_admin
from .views import login_views

urlpatterns = [
    path("", views.home, name="home"),
    path("setup/", setup_admin),
    path("login/", login_views),
]

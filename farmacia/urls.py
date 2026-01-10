from .vews import setup_admin
from .views import login_view

urlpatterns = [
    path("", views.home, name="home"),
    path("setup/", setup_admin),
    path("login/", login_view),
]

from .vews import setup_admin

urlpatterns = [
    path("", views.home, name="home"),
    path("setup/", setup_admin),
]

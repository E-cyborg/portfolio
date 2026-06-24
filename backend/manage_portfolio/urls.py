from django.urls import path
from manage_portfolio import views as MV

urlpatterns = [
    path("<int:id>/", MV.home, name="home_view"),
    path("", MV.main_page, name="main"),
    path("<int:id>/projects", MV.project_view, name="projects"),
]
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("test/", views.TestPage.as_view(), name="test"),
    path("thanks/", views.ThanksPage.as_view(), name="thanks"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("posts/", include("posts.urls")),
    path("groups/", include("groups.urls")),
]

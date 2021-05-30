from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app.views import *

urlpatterns = [
    path("", main_page, name="home"),
    path("about/", about, name="about"),
    path("teams-stats/", teams_and_stats, name="teams-stats"),
    path("gallery/", gallery, name="gallery"),
    path("blog-posts/", blog_posts, name="blog-posts"),
    path("schedule/", schedule, name="schedule"),
    path("partners/", partners, name="partners"),
    path("contacts/", contacts, name="contacts"),
    path("blog-posts/blog_post/<int:pk>/", blog_post, name="blog-post"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

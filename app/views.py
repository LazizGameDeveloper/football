from django.shortcuts import render
from app.models import *


def main_page(request):
    news_list = News.objects.filter(is_active=True)
    coaches = Coach.objects.filter(is_active=True)
    gallery_photos = GalleryPhoto.objects.filter(is_active=True)[:6]

    for coach in coaches:
        coach.achievements = cut(coach.achievements, 90)

    return render(request, "index.html", {
        "news_list": news_list,
        "gallery_photos": gallery_photos,
        "coaches": coaches
    })


def about(request):
    return render(request, "about.html")


def teams_and_stats(request):
    return render(request, "teams-stats.html")


def gallery(request):
    return render(request, "gallery.html")


def news_and_blog(request):
    return render(request, "blog-posts.html")


def schedule(request):
    return render(request, "schedule.html")


def partners(request):
    return render(request, "partners.html")


def contacts(request):
    return render(request, "contacts.html")


def blog_post(request):
    return render(request, "blog-post.html")


def cut(variable, length):
    variable = variable[:length]
    variable = variable.rsplit(" ", 1)[0]

    if not variable[-1].isalnum():
        variable = variable[:-1]

    variable += "..."
    return variable

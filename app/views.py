from django.shortcuts import render
from app.models import *


def main_page(request):
    slides = MainSlide.objects.filter(is_active=True)
    news_list = News.objects.filter(is_active=True)
    gallery_photos = GalleryPhoto.objects.filter(is_active=True)[:6]
    coaches = Coach.objects.filter(is_active=True)

    for coach in coaches:
        coach.achievements = cut(coach.achievements, 90)

    partners_list = Partner.objects.filter(is_active=True)

    return render(request, "index.html", {
        "news_list": news_list,
        "gallery_photos": gallery_photos,
        "coaches": coaches,
        "partners": partners_list,
        "slides": slides,
    })


def about(request):
    team_members = TeamMembers.objects.filter(is_active=True)
    for member in team_members:
        member.biography = member.biography.split(".", 1)[0] + "."
        member.biography = cut(member.biography, 250)

    committee_list = Committee.objects.filter(is_active=True)

    return render(request, "about.html", {
        "team_members": team_members,
        "committee_list": committee_list,
    })


def teams_and_stats(request):
    coaches = Coach.objects.filter(is_active=True)
    for coach in coaches:
        coach.achievements = cut(coach.achievements, 90)

    return render(request, "teams-stats.html", {
        "coaches": coaches,
    })


def gallery(request):
    gallery_photos = GalleryPhoto.objects.filter(is_active=True)

    return render(request, "gallery.html", {
        "gallery_photos": gallery_photos,
    })


def news_and_blog(request):
    return render(request, "blog-posts.html")


def schedule(request):
    return render(request, "schedule.html")


def partners(request):
    general_partners = Partner.objects.filter(is_active=True)[:3]
    all_partners = Partner.objects.filter(is_active=True)

    return render(request, "partners.html", {
        "general_partners": general_partners,
        "all_partners": all_partners,
    })


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

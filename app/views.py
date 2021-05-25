from django.shortcuts import render
from django.db import models
from app.models import *


def main_page(request):
    news_list = News.objects.filter(is_active=True)

    # Короткое описание статьи
    check_short_description(news_list)

    return render(request, "index.html", {
        "news_list": news_list,
    })


def check_short_description(news_list):
    for news in news_list:
        if len(news.short_description) < 1:
            # берём первое предложение из news.content
            first_sentence = news.content.split(".")[0]
            split_sentence = first_sentence.split(" ")

            i = 0
            rendering_sentence = split_sentence[i] + " "
            # желательно чтобы длина описания была не больше 60 символов
            while len(rendering_sentence) < 50 and i+1 < len(split_sentence):
                i += 1
                rendering_sentence += split_sentence[i] + " "

            if not rendering_sentence[len(rendering_sentence)-2].isalnum():
                rendering_sentence = rendering_sentence[0:len(rendering_sentence)-2]

            news.short_description = rendering_sentence + "..."


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

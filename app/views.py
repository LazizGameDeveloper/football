from django.shortcuts import render


def main_page(request):
    return render(request, "index.html")


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

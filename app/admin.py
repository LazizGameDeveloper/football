from django.contrib import admin
from app.models import *


@admin.register(News)
class Admin(admin.ModelAdmin):
    list_display = [
        "title",
        "date",
        "is_active",
        "admin_content",
        "admin_image"
    ]

    list_per_page = 15


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = [
        "title",
        "image",
        "content",
        "date",
        "is_active",
    ]

    list_per_page = 15


@admin.register(GalleryPhoto)
class AdminGalleryPhoto(admin.ModelAdmin):
    list_display = [
        "title",
        "date",
        "is_active",
        "admin_image",
    ]

    list_per_page = 15


@admin.register(GalleryVideo)
class AdminGalleryVideo(admin.ModelAdmin):
    list_display = [
        "video",
        "description",
        "date",
        "is_active",
    ]

    list_per_page = 15


@admin.register(Coach)
class AdminCoach(admin.ModelAdmin):
    list_display = [
        "name",
        "last_name",
        "occupation",
        "achievements",
        "is_active",
        "admin_image",
    ]

    list_per_page = 15


@admin.register(MainSlide)
class AdminMainSlides(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "admin_image",
        "is_active",
    ]

    list_per_page = 15


@admin.register(Partner)
class AdminPartners(admin.ModelAdmin):
    list_display = [
        "name",
        "admin_image",
        "history",
        "is_active",
    ]

    list_per_page = 15


@admin.register(TeamMembers)
class AdminTeamMembers(admin.ModelAdmin):
    list_display = [
        "name",
        "last_name",
        "rank",
        "admin_biography",
        "is_active",
    ]

    list_per_page = 15


@admin.register(Committee)
class AdminCommittee(admin.ModelAdmin):
    list_display = [
        "name",
        "last_name",
        "occupation",
        "is_active",
    ]

    list_per_page = 15

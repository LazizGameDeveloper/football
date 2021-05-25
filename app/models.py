from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name="Title", max_length=70, default="")
    image = models.ImageField(
        verbose_name="Image 1x1",
        upload_to="img/news/",
        default="",
    )
    content = models.TextField(verbose_name="Content", default="")
    short_description = models.TextField(verbose_name="Short_description", max_length=70, blank=True, default="")
    date = models.DateTimeField(
        verbose_name="Creation date",
        editable=False,
        auto_now_add=True
    )
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="80" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:

        verbose_name = "news"
        verbose_name_plural = "news"

        ordering = ["date", "is_active"]


class Blog(models.Model):
    title = models.CharField(verbose_name="Title", max_length=120, default="")
    image = models.ImageField(
        verbose_name="Image 2x1",
        upload_to="img/blog/",
        default="",
        blank=True
    )
    content = models.TextField(verbose_name="Content")
    date = models.DateTimeField(
        verbose_name="Creation date",
        editable=False,
        auto_now_add=True
    )
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

        ordering = ["date", "is_active"]


class Merch(models.Model):
    # title
    # preview (size is unknown)
    # description (is not necessary)
    # cost
    pass


class GalleryPhoto(models.Model):
    image = models.ImageField(
        verbose_name="Photo 640x500",
        upload_to="img/clubGallery/",
        default=""
    )
    description = models.CharField(
        verbose_name="Short description",
        max_length=70,
        default="",
        blank=True
    )
    date = models.DateField(
        verbose_name="Creation date",
        editable=False,
        auto_now_add=True,
    )
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    class Meta:
        verbose_name = "photo"
        verbose_name_plural = "gallery photos"

        ordering = ["date", "is_active"]


class GalleryVideo(models.Model):
    video = models.FileField(
        verbose_name="Video",
        upload_to="video/clubGallery",
        default=""
    )
    description = models.CharField(verbose_name="Short description", max_length=70, default="")
    date = models.DateField(
        verbose_name="Creation date",
        editable=False,
        auto_now_add=True,
    )
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "gallery videos"

        ordering = ["date", "is_active"]


class Coach(models.Model):
    image = models.ImageField(
        verbose_name="Photo 1x1",
        upload_to="img/coaches/",
        default=""
    )
    name = models.CharField(verbose_name="Name", max_length=30, default="")
    last_name = models.CharField(verbose_name="Last name", max_length=30, default="")
    occupation = models.CharField(verbose_name="Occupation", max_length=50, default="")

    # also you can use TextField
    achievements = models.CharField(verbose_name="Achieves", max_length=225, default="")
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    class Meta:
        verbose_name = "coach"
        verbose_name_plural = "coaches"

        ordering = ["name", "is_active"]


class MainSlides(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, default="")
    description = models.CharField(verbose_name="Short description", max_length=50, default="")
    image = models.ImageField(
        verbose_name="Slide image",
        upload_to="img/slides/",
        default="",
    )
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    class Meta:
        verbose_name = "slide"
        verbose_name_plural = "main menu slides"

        ordering = ["title", "is_active"]


class Partners(models.Model):
    name = models.CharField(verbose_name="Partner name", max_length=50, default="")
    image = models.ImageField(
        verbose_name="Logo",
        upload_to="img/partners/",
        default="",
    )
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    class Meta:
        verbose_name = "partner"
        verbose_name_plural = "partners"

        ordering = ["name", "is_active"]


class TeamMembers(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30, default="")
    last_name = models.CharField(verbose_name="Last name", max_length=30, default="")
    rank = models.CharField(verbose_name="Rank", max_length=50, default="")
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    class Meta:
        verbose_name = "member"
        verbose_name_plural = "team members"

        ordering = ["name", "is_active"]

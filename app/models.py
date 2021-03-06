from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name="Title", max_length=70, default="")
    image = models.ImageField(
        verbose_name="Image 1x1",
        upload_to="img/news/",
        default="",
    )
    content = models.TextField(verbose_name="Content", default="")
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

    # Чтобы сократить выводимый текст в админке
    def admin_content(self):
        short_description = self.content[:200]
        # убираем последнее слово т.к. оно может мы разрезанным
        return f"{short_description.rsplit(' ', 1)[0]}"

    admin_content.short_description = "Desc"
    admin_content.allow_tags = True

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
    date = models.DateField(
        verbose_name="Creation date",
        editable=False,
        auto_now_add=True
    )
    author = models.CharField(verbose_name="Created by", max_length=20, default="")
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="200" /></a>'
            )
        else:
            return 'Image does not exist'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    def admin_content(self):
        short_description = self.content[:300]
        # убираем последнее слово т.к. оно может мы разрезанным
        return f"{short_description.rsplit(' ', 1)[0]}"

    admin_content.short_description = "Desc"
    admin_content.allow_tags = True

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
    title = models.CharField(
        verbose_name="Title",
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

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

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

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "coach"
        verbose_name_plural = "coaches"

        ordering = ["name", "is_active"]


class MainSlide(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, default="")
    description = models.CharField(verbose_name="Short description", max_length=50, default="")
    image = models.ImageField(
        verbose_name="Slide image",
        upload_to="img/slides/",
        default="",
    )
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="200" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "slide"
        verbose_name_plural = "main menu slides"

        ordering = ["title", "is_active"]


class Partner(models.Model):
    name = models.CharField(verbose_name="Partner name", max_length=50, default="")
    image = models.ImageField(
        verbose_name="Logo",
        upload_to="img/partners/",
        default="",
    )
    history = models.TextField(verbose_name="History", default="")
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
        verbose_name = "partner"
        verbose_name_plural = "partners"

        ordering = ["name", "is_active"]


class TeamMembers(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30, default="")
    last_name = models.CharField(verbose_name="Last name", max_length=30, default="")
    rank = models.CharField(verbose_name="Rank", max_length=50, default="")
    biography = models.TextField(verbose_name="Biography", default="")
    image = models.ImageField(
        verbose_name="Photo",
        upload_to="img/team members/",
        default="",
    )
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    def admin_image(self):

        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="200" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    def admin_biography(self):
        short_description = self.biography[:200]
        # убираем последнее слово т.к. оно может мы разрезанным
        return f"{short_description.rsplit(' ', 1)[0]}"

    admin_biography.short_description = "Desc"
    admin_biography.allow_tags = True

    class Meta:
        verbose_name = "member"
        verbose_name_plural = "team members"

        ordering = ["name", "is_active"]


class Committee(models.Model):
    name = models.CharField(verbose_name="Name", max_length=40, default="")
    last_name = models.CharField(verbose_name="Last_name", max_length=40, default="")
    occupation = models.CharField(verbose_name="Occupation", max_length=50, default="")
    is_active = models.BooleanField(verbose_name="Is active", default=False)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Committee"

        ordering = ["name", "last_name"]


class Contact(models.Model):
    first_name = models.CharField(verbose_name="First name", max_length=50, default="")
    last_name = models.CharField(verbose_name="Last name", max_length=60, default="")
    email = models.CharField(verbose_name="E-mail", max_length=100, default="")
    message = models.TextField(verbose_name="Message", default="")
    send_data = models.DateField(verbose_name="Data", auto_now_add=True, editable=False)

    def short_message(self):
        if len(self.message) > 200:
            return self.message[200].rsplit(" ", 1)[0]
        else:
            return self.message
    class Meta:

        verbose_name = "contact"
        verbose_name_plural = "contacts"

        ordering = ["-send_data"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}."

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import (
    RichTextUploadingField,
)
from django.utils.safestring import mark_safe

STATUS = ((0, "Draft"), (1, "Publish"))

CATEGORIES = (
    ("template", "Template"),
    ("article", "Article"),
    ("blog", "Blog"),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)

    # Main image for cards/featured preview
    main_image = models.ImageField(
        upload_to="blog/main_images/",
        blank=True,
        null=True,
        default="Summary",
        help_text="Featured image for cards and previews (Recommended: 1200x630px).",
    )

    summary = models.CharField(
        null=True,
        max_length=500,
        help_text="Insert summary of article for SEO purposes."
    )
    # Rich text with upload capability
    content = RichTextUploadingField(
        config_name="default",
        extra_plugins=["uploadimage"],  # Enable image upload
        external_plugin_resources=[
            ("uploadimage", "/static/ckeditor/uploadimage/", "plugin.js")
        ],
    )

    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default="Article")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    def short_description(self):
        import re

        clean_text = re.sub("<[^<]+?>", "", self.content)
        words = clean_text.split()
        return " ".join(words[:30]) + "..." if len(words) > 30 else clean_text

    @property
    def main_image_preview(self):
        if self.main_image:
            return mark_safe(f'<img src="{self.main_image.url}" width="150" />')
        return "No Image"

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    """Модель публикации"""

    title = models.CharField(verbose_name="Заголовок", max_length=50)
    text = models.TextField(verbose_name="Текст", blank=True)
    img = models.ImageField(
        verbose_name="Фото", upload_to="posts/images/%Y/%m/%d", blank=True
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True
    )
    upd_date = models.DateTimeField(
        verbose_name="Дата обновления", auto_now=True
    )
    author = models.ForeignKey(
        to=User,
        verbose_name="Автор",
        related_name="posts",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        to="Category",
        verbose_name="Категория",
        related_name="posts",
        on_delete=models.CASCADE,
    )
    views = models.IntegerField("Просмотры", default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single_post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ["-pub_date", "title"]


class Category(models.Model):
    """Модель категорий"""

    title = models.CharField(verbose_name="Заголовок", max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]

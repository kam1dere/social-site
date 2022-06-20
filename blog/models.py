from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from pytils.translit import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Наименование',
                             help_text='Не более 200 символов')
    content = RichTextField(max_length=5000, blank=True, null=True, help_text="Не более 5000 символов")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор')  # null=True дает возможность публиковать посты не
    # зарегестрированным пользователям
    slug = models.SlugField(max_length=200, db_index=True)  # Для большого проекта уникальный слаг не
    # подойдет, из-за большого количества пользователей, но для данных задач - подходит
    likes_post = models.ManyToManyField(User, related_name='like_post', blank=True, verbose_name='Лайкнутые посты')
    # reply = models.ForeignKey('self', null=True, blank=True, related_name='reply_ok', on_delete=models.CASCADE)
    saved_post = models.ManyToManyField(User, related_name='saved_post', blank=True, verbose_name='Сохраненные посты')

    def total_likes_post(self):
        return self.likes_post.count()

    def total_saved_posts(self):
        return self.saved_post.count()

    def get_absolute_url(self):
        return reverse('user_detail_post', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'


@receiver(pre_save, sender=Post)
def prepopulated_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)

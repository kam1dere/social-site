from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# slugifay из Джанго почему-то не видит русские буквы и не заполняет, хотя в админке все хорошо(prepopy..),
# надо потом глянуть.
from django.template.defaultfilters import slugify as django_slugify
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):

    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Discussion(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Наименование',
                             help_text='Не более 200 символов')
    content = RichTextField(max_length=5000, blank=True, null=True, help_text="Не более 5000 символов")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор')  # null=True дает возможность публиковать посты не зарегестрированным пользователям
    slug = models.SlugField(max_length=200, db_index=True)  # Для большого проекта уникальный слаг не
    # подойдет, из-за большого количества пользователей, но для данных задач - подходит
    likes_discussion = models.ManyToManyField(User, related_name='like_discussion', blank=True, verbose_name='Лайкнутые дискуссии')
    # reply = models.ForeignKey('self', null=True, blank=True, related_name='reply_ok', on_delete=models.CASCADE)
    saved_discussion = models.ManyToManyField(User, related_name='saved_discussion', blank=True, verbose_name='Сохраненные дискуссии')

    def total_likes_post(self):
        return self.likes_discussion.count()

    def total_saved_posts(self):
        return self.saved_discussion.count()

    def get_absolute_url(self):
        return reverse('user_detail_discussion', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Создать дискусию'
        verbose_name_plural = 'Создать дискусии'


@receiver(pre_save, sender=Discussion)
def prepopulated_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)

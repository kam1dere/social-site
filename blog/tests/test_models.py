from blog.models import Post
import pytest

# class Post(models.Model):
#     title = models.CharField(max_length=200, db_index=True, verbose_name='Наименование',
#                              help_text='Не более 200 символов')
#     content = RichTextField(max_length=5000, blank=True, null=True, help_text="Не более 5000 символов")
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
#     slug = models.SlugField(max_length=200, unique=True, db_index=True)  # Для большого проекта уникальный слаг не
#     # подойдет, из-за большого количества пользователей, но для данных задач - подходит
#     likes_post = models.ManyToManyField(User, related_name='like_post', blank=True, verbose_name='Лайкнутые посты')
#     # reply = models.ForeignKey('self', null=True, blank=True, related_name='reply_ok', on_delete=models.CASCADE)
#     saved_post = models.ManyToManyField(User, related_name='saved_post', blank=True, verbose_name='Сохраненные посты')
from django.shortcuts import get_object_or_404


@pytest.mark.django_db
def test_title_create():
    article = Post.objects.create(title='article1', content='srgsgs')
    assert article.title == 'article1'

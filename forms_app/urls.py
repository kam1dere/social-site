from django.urls import path, re_path
from .views import manage_authors


# path('form/', include('forms_app.urls')),
urlpatterns = [
    path('', manage_authors, name='create')
]

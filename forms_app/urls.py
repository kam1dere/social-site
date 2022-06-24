from django.urls import path
from .views import contact_send


# path('form/', include('forms_app.urls')),
urlpatterns = [
    path('contact/', contact_send, name='contact'),
]
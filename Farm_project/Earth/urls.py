from django.urls import path
from .views import *
from django.conf.urls.static import static
app_name = "Earth"

urlpatterns = [
    path('profile', show_profile, name='profile'),
    path('', MainPage.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
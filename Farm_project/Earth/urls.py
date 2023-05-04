from django.urls import path
from .views import *
from django.conf.urls.static import static
app_name = "Earth"

urlpatterns = [
    path('', MainPage.as_view()),
    path('product/<int:prod_id>',test_show_product, name='prod'),
    
    path('api/', APIAllProducts, name='allapi'),
    path('api/<int:pk>', APIProduct),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
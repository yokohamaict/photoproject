from django.urls import path
from .views import IndexView, CreatePhotoView, PostSuccessView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'photo'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/', CreatePhotoView.as_view(), name='post'),
    path('post_done/', PostSuccessView.as_view(), name='post_done'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT,
)
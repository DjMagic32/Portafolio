from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


urlpatterns = [
	path('', views.index, name='index'),
    path('Messagesend.html', views.Messagesend, name='Messagesend.html'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
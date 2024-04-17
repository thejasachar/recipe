
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',home,name="home"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('success-page/',success_page,name="success_page"),
    path('delete_recipe/<id>/',delete_recipe,name="delete_recipe"),
    # path('login/',login_page,name="login_page"),
    # path('register/',register,name="register"),
    # path('logout/',logout_page,name="logout_page"),
    path('update_recipe/<id>/',update_recipe,name="update_recipe"),
    path('recipes/',recipes,name="recipes"),
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()
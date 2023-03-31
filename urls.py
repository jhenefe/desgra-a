from django.contrib import admin
from django.urls import path, include, re_path

#from rest_framework.authtoken import views
from django.urls import include, path
from rest_framework import routers
from horadopao.api import viewsets 
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'Users', viewsets.UserViewSet)
router.register(r'Padarias', viewsets.PadariaViewSet)
router.register(r'Cliente', viewsets.ClienteViewSet)
router.register(r'PadariaFav', viewsets.PadariaFavViewSet)
router.register(r'FornadaPlan', viewsets.FornadaPlanViewSet)
router.register(r'FornadaAt', viewsets.FornadaAtViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',include('tasks.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    re_path(r'^favicon\.ico$', favicon_view),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




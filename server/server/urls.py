"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

# import for the swagger Ui
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


from api import views

schema_view = get_schema_view(title='Django Rest Framework Backend', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'wishlist', views.WishListViewSet)


urlpatterns = [
    url(r'^', schema_view, name="docs"), # used for the swagger
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    # path('', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import include, path
from core.views.livro import LivroViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, EditoraViewSet, UserViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"users", UserViewSet, basename="users")
router.register(r"editoras", EditoraViewSet)
router.register(r"autores", AutorViewSet)
router.register(r"livros", LivroViewSet)
router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
    path("api/media/", include(uploader_router.urls)),  

]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)


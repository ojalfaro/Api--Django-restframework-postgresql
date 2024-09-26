from rest_framework.routers import DefaultRouter
from inventarios.api.views import ProductViewSet

router = DefaultRouter()

router.register('product',ProductViewSet,basename='producto')
urlpatterns = router.urls


from django.conf.urls import include, url

from rest_framework_tus.views import UploadViewSet

from .routers import TusAPIRouter

router = TusAPIRouter()
router.register(r'files', UploadViewSet, base_name='upload')

urlpatterns = [
    url(r'', include(router.urls, namespace='api'))
]

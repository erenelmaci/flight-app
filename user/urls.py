from .views import UserView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

urlpatterns = [
     path('auth/', include('dj_rest_auth.urls'))
]

#  ---------- Router ----------

router = DefaultRouter()
router.register('', UserView)
urlpatterns += router.urls

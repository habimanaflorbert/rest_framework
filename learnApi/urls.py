from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('home.urls')),
    path('',include('accounts.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('login-1/', obtain_auth_token, name='api_token_auth'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
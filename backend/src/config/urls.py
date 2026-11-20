from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import RegisterView, UserDetailView, CreateStaffView # <--- Yahan import karein

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth Endpoints
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/me/', UserDetailView.as_view(), name='user_detail'),
    
    # Sirf Admin ke liye (Faculty/Admin banane ke liye)
    path('api/staff/create/', CreateStaffView.as_view(), name='create_staff'), # <--- Ye add karein
]
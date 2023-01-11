from django.urls import path,include

from . import views
# from ...baseregister import views as regviews

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

# from login import baseregister

urlpatterns = [
    path('', views.MyTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    # path('login/register/',regviews.register_request, name="register"),
    # path('login/register/',include('...baseregister.urls'))
    path('register/',views.register_request)
]
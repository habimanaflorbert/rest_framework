from django.urls import path,include
from home.views import MyTokenObtainPairView,CustomAuthToken,MyAuthenticationView, StudentViews,SchoolViewset
from rest_framework import routers

route=routers.DefaultRouter()
route.register('students',SchoolViewset)



urlpatterns = [
    path('student/',StudentViews.as_view(),name="student"),
    path('',include(route.urls)),
    path('my-auth/',MyAuthenticationView.as_view()),
    # path('login/',CustomAuthToken.as_view())
    path('login/',MyTokenObtainPairView.as_view())
]

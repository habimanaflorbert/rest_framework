from django.urls import path,include
from home.views import StudentViews,SchoolViewset
from rest_framework import routers

route=routers.DefaultRouter()
route.register('students',SchoolViewset)



urlpatterns = [
    path('student/',StudentViews.as_view(),name="student"),
    path('',include(route.urls)),
]

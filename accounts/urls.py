from django.urls import path,include
from accounts.views import RegisterViewset
from rest_framework import routers

route=routers.DefaultRouter()
route.register('user',RegisterViewset)




urlpatterns = [
    path('',include(route.urls)),
]

"""usingBerearTokeninApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myApp.views import PersonViewSet, ObtainTokenPairView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
]



# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTE2OTQ2NiwiaWF0IjoxNjc5MDgzMDY2LCJqdGkiOiI4OWIyYzYwZGRkZmM0YWJhOGMzZDA1NGZiODMzNmRhMCIsInVzZXJfaWQiOjEsIm5hbWUiOiIgIn0.He7ltaQwgYS_eLGvTbdI9Ipmp0cJx1m-Gpj9qjQt3qs",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5MDgzOTY2LCJpYXQiOjE2NzkwODMwNjYsImp0aSI6IjU3Y2QyMzY0MjE4YTQxMDM5ZmIwZGI3MWNiMTM1OTYwIiwidXNlcl9pZCI6MSwibmFtZSI6IiAifQ.ssADudoHYZg5SM5iBgB2xw8Ng6dkHRLhyK1SX2ffzLs"
# }
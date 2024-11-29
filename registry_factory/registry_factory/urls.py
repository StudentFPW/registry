"""
URL configuration for registry_factory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .routers import CustomRouter
from . import views

from links.views import LinksViewset, LinkViewset
from ratings.views import RatingsViewset, RatingViewset
from achievements.views import AchievementsViewset, AchievementViewset
from results.views import ResultsViewset, ResultViewset

router = CustomRouter()
router.register(r'links', LinksViewset, basename='links')
router.register(r'link', LinkViewset, basename='link')

router.register(r'achievements', AchievementsViewset, basename='achievements')
router.register(r'achievement', AchievementViewset, basename='achievement')

router.register(r'ratings', RatingsViewset, basename='ratings')
router.register(r'rating', RatingViewset, basename='rating')

router.register(r'results', ResultsViewset, basename='results')
router.register(r'result', ResultViewset, basename='result')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('info/', views.info),
]
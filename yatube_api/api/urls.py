from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken import views

from . import views as v

router_v1 = routers.DefaultRouter()
router_v1.register('posts', v.PostViewSet, basename='posts')
router_v1.register('groups', v.GroupViewSet, basename='groups')
router_v1.register(r'posts/(?P<id>[^/.]+)/comments', v.CommentViewSet,
                   basename='comments')
router_v1.register('follow', v.FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

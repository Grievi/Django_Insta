from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.save_image, name='save_img'),
    path('like/<int:id>/', views.like_image, name='like'),
    path('picture/<int:id>/', views.single_image, name='single_img'),
    path('comment/add', views.save_comment, name='comment.add'),
    path('user/<int:id>/', views.user_profile, name='user.profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
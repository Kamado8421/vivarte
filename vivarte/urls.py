from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.profile.urls')), 
]

handler404 = 'apps.profile_user.views.page_not_found'

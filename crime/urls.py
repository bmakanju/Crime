from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("door", admin.site.urls),
    #path('tinymce/', include('tinymce.urls')),
    path("", include("crimepost.urls", namespace="crimepost")),
    path("", include("account.urls", namespace='account')),
    path("", include("blog.urls", namespace='blog')),
    #path("", include("entertain.urls", namespace='entertain')),
    path("", include("sport.urls", namespace='sport')),
    #path("", include("dashboard.urls", namespace="dashboard")),
    path("", include("subscribers.urls", namespace="subscribers")),
]


from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
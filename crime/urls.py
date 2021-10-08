from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='Reset/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='Reset/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Reset/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Reset/password_reset_complete.html')),
    path("door", admin.site.urls),
    #path('tinymce/', include('tinymce.urls')),
    path("", include("crimepost.urls", namespace="crimepost")),
    path("", include("account.urls", namespace='account')),
    path("", include("blog.urls", namespace='blog')),
    path("", include("beauty.urls", namespace='beauty')),
    path("", include("entertain.urls", namespace='entertain')),
    path("", include("fashion.urls", namespace="fashion")),
    path("", include("sport.urls", namespace='sport')),
    #path("", include("dashboard.urls", namespace="dashboard")),
    path("", include("subscribers.urls", namespace="subscribers")),
]

handler404 = "crime.views.page_not_found_view"
#handler500 = "crime.views.page_not_found"

from django.conf.urls.static import static
from django.conf import settings

#urlpatterns +=  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
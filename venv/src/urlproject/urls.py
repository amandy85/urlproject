
from django.contrib import admin
from django.urls import path,re_path
from shortner.views import HomeView, URLRedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    re_path(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(),name = 'scode'),


]
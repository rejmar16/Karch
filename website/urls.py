from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('filter/<str:type>/', views.RD_filter, name='RD_filter'),
    path('contact/', views.contact_list, name='contact_list'),
    path('project/<int:pk>/<int:ip>/', views.RD_detail, name='RD_detail')
    #path('projects/(?P<pk>[0-9]+)/(?P<ip>[0-9]+)/', views.RD_detail, name='RD_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 
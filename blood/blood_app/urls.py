from django.urls import path
from .import views
from blood import settings
from django.conf.urls.static import static


urlpatterns=[
    
    path('show',views.new),
    path('create',views.old),
    path('del/<rid>',views.deletepost),
    path('edit/<pid>',views.edit),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
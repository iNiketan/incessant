
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.index_title = "Incessant Admin Panel"
admin.site.site_header = "Incessant Admin"

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('childapp.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

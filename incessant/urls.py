
from django.contrib import admin
from django.urls import path, include

admin.site.index_title = "Incessant Admin Panel"
admin.site.site_header = "Incessant Admin"




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('childapp.urls'))
]

from django.urls import path
from .views import index, GeneratePdf

urlpatterns = [
	path('', index, name = 'index'),
	path('pdf', GeneratePdf.as_view(), name = 'pdf'),
    # path('admin/', admin.site.urls),
    # path('', include('app.example.urls')),
]

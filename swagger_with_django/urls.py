from django.conf.urls import url, include
from django.contrib import admin

from swagger_with_django.swagger_schema import SwaggerSchemaView

urlpatterns = [
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^cbv/', include('cbv.urls')),
        url(r'^fbv/', include('fbv.urls')),
        url(r'^admin/', admin.site.urls),
        url(r'^', SwaggerSchemaView.as_view()),
]

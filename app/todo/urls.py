from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('api/', include('todo.api.urls'))
]
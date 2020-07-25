from django.urls import path

from frontend.views.home import index

urlpatterns = [
    path('', index, name='home'),
]
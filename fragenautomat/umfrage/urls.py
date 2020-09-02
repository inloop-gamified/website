from django.urls import path

from . import views

app_name = 'umfrage'

urlpatterns = [
    path('<slug:umfrage_key>/', views.UmfrageView.as_view(), name='umfrage'),
]

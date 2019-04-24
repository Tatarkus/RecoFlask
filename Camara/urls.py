from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^entrenamiento/', views.entrenamiento, name='entrenamiento'),
	url(r'^entrenar/',views.entrenar, name='entrenar'),

]
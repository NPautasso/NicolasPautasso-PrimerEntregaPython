from django.urls import path
from . import views


urlpatterns = [
    path('cerrajero/crear/', views.crear_cerrajero, name="crear_cerrajero"),
    path('futbolista/crear/', views.crear_futbolista, name="crear_futbolista"),
    path('ingeniero/crear/', views.crear_ingeniero, name="crear_ingeniero"),
    path('cerrajeros/', views.lista_cerrajeros, name='lista_cerrajeros'),
]
 
from django.urls import path

#importar da pasta atual o arquivo views.py
from polls import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name='sobre'),
    path('pergunta/<int:question_id>', views.exibe_questao, name='exibe_questao'),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas')
]
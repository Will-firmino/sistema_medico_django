from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', preciso mostrar a página cadastro.html),
]


# Verbos HTTPs - FRONTEND <-> BACKEND
#  GET -> www.vollmed.com -> Exiba a página home da vollmed.
#  POST -> www.vollmed.com/cadastro -> Cadastrado um novo usuário.
#  PUT -> www.vollmed.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE  -> www.vollmed.com/logado/deletar/1 -> Deletando um usuário.


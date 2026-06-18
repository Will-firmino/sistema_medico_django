from django.contrib import admin
from django.urls import path

# Urls que podem ser acessadas por todos
urlpatterns = [
    path('admin/', admin.site.urls), # Chamando o /admin e mostrando a página inicial do logi do portal do django.
    path('cadastro/', preciso mostrar a página cadastro.html),
    path('login/', preciso mostrar a página login.html),
    path('home/', preciso mostrar a página home.html),
    path('esqueci-senha/', preciso mostrar a página esqueci-senha.html),
    
]



# Verbos HTTPs - FRONTEND <-> BACKEND
#  GET -> www.vollmed.com -> Exiba a página home da vollmed.
#  POST -> www.vollmed.com/cadastro -> Cadastrado um novo usuário.
#  PUT -> www.vollmed.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE  -> www.vollmed.com/logado/deletar/1 -> Deletando um usuário.


from django.db import models

# Criar um modelo do médico, com nome, email, telefone, crm, especialidade
class Medico(models.Model):
    # Atributos = características = variáveis
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=20)

    # Métodos = ações = funções
    def __str__(self):
        return f'{self.nome}'
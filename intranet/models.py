from django.db import models

# Criar um modelo do médico, com nome, email, telefone, crm, especialidade
class Medico(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    crm
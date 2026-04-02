from django.utils import timezone # Importação do módulo timezone que traz datas e horários. 

from django.db import models 

# Criar um modelo do médico, com nome, email, telefone, crm, especialidade
class Medico(models.Model):
    # Atributos = características = variáveis
    nome = models.CharField(max_length=30) 
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
    crm = models.CharField(max_length=6)
    especialidade = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    mensagem = models.TextField(blank=True) 

    # Métodos = ações = funções
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

# Criar um modelo do paciente, com nome, email, telefone, cpf
class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.nome}'
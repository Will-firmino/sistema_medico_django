from django.contrib import admin
from intranet import models

@admin.register(models.Medico) # Registrando a classe Médico do Portal do python
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'crm', 'especialidade',)

@admin.register(models.Paciente) # Registando a classe Paciente do Portal do python
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'cpf',)


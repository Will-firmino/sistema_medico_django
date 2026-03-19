from django.contrib import admin
from intranet import models

@admin.register(models.Medico) # Registrando a classe Médico do Portal do python
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'crm', 'especialidade',)


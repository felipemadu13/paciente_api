from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return (f'id: {self.id}, nome: {self.nome}, sexo: {self.sexo}, '
                f'data_nascimento: {self.data_nascimento}, cpf: {self.cpf}, '
                f'telefone: {self.telefone}')

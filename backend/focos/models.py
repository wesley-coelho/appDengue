from django.db import models

class Foco(models.Model):
    bairro = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    cep = models.CharField(max_length=9)
    foto = models.ImageField(upload_to='focos_fotos/', blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.endereco}, {self.numero} - {self.bairro}'
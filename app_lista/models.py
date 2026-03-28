from django.db import models

class lista(models.Model):
    titulo = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)
    deletada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
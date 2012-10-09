from django.db import models

# Create your models here.


class Informativos(models.Model):
	cabecalho = models.CharField(max_length=20)
	descricao = models.CharField(max_length=300)
	link = models.CharField(max_length=200)

	def __unicode__(self):
		return self.cabecalho
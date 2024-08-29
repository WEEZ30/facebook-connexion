from django.db import models

# Create your models here.

class Client(models.Model):
	"""docstring for CLient"""
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField('Créé le', auto_now_add=True, editable=False)

	def __str__(self):
		return f"username:{self.username} password:{self.password}"

	class META:
		ordering ='-created_at'
		
		
from django.contrib import admin
from .models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'password', 'created_at')
	list_filter = ['created_at']
	search_fields = ('username', 'created_at')
		

admin.site.register(Client, ClientAdmin)
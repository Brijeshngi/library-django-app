from django.contrib import admin
from .models import bookDetails
# Register your models here.
@admin.register(bookDetails)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','author','ISBN')

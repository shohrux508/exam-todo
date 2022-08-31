from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


# Register your models here.
@admin.register(Student)
class UserAdmin(ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)
    list_filter = ('level', 'age')


@admin.register(Plan)
class UserAdmin(ModelAdmin):
    list_display = ('title', 'date', 'status')
    list_filter = ('date',)
    list_editable = ('status',)
    search_fields = ('student',)


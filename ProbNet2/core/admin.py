from django.contrib import admin

from .models import *


@admin.register(Customer_Data)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('company_name', 'initial_ip_range')
    ordering = ('company_name', )
    search_fields = ('company_name', )
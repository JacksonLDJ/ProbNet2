from django.contrib import admin

from .models import *


@admin.register(Customer_Data)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('company_name', 'initial_ip_range')
    ordering = ('company_name', )
    search_fields = ('company_name', )


@admin.register(Netsweeper_Result)
class NetsweperAdmin(admin.ModelAdmin):

    list_display = ('ip_address', )
    ordering = ('ip_address', )
    search_fields = ('ip_address', )

@admin.register(Device_Data)
class DeviceAdmin(admin.ModelAdmin):

    list_display = ('IP_Address', )
    ordering = ('IP_Address', )
    search_fields = ('IP_Address', )
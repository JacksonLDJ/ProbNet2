# models.py
from django.db import models

class Device_Data(models.Model):
    Device_ID = models.CharField(max_length=256, primary_key=True)
    IP_Address = models.GenericIPAddressField()
    Port = models.IntegerField(null=True)
    Service = models.CharField(max_length=256, null = True)
    Operating_Sytem = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now=True, help_text="Time and date this was created")
    updated_on = models.DateTimeField(auto_now=True, help_text="Time and date this was updated")
    MAC_Address = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.IP_Address}"

# models.py
from django.db import models

class OS_Info(models.Model):
    type = models.CharField(max_length=256)
    vendor = models.CharField(max_length=256)
    osfamily = models.CharField(max_length=256)
    osgen = models.CharField(max_length=256)
    accuracy = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.vendor} {self.type}"

class Device_Data(models.Model):
    Device_ID = models.CharField(max_length=256, primary_key=True)
    IP_Address = models.GenericIPAddressField()
    Operating_System = models.OneToOneField(OS_Info, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True, help_text="Time and date this was created")
    updated_on = models.DateTimeField(auto_now=True, help_text="Time and date this was updated")
    MAC_Address = models.CharField(max_length=256)
    Hardware_Details = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.IP_Address}"

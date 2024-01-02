# models.py
from django.db import models

#id fields are automatically generated by Django

class OS_Info(models.Model):

    type = models.CharField(max_length=256)
    vendor = models.CharField(max_length=256)
    osfamily = models.CharField(max_length=256)
    osgen = models.CharField(max_length=256)
    accuracy = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.vendor} {self.type}"

class Device_Data(models.Model):

    IP_Address = models.GenericIPAddressField()
    Operating_System = models.OneToOneField(OS_Info, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True, help_text="Time and date this was created")
    updated_on = models.DateTimeField(auto_now=True, help_text="Time and date this was updated")
    MAC_Address = models.CharField(max_length=256)
    Hardware_Details = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.IP_Address}"


class Port(models.Model):
    protocol = models.CharField(max_length = 256)
    portid = models.PositiveSmallIntegerField()
    Reason = models.CharField(max_length = 256)
    reason_ttl = models.CharField(max_length = 256)
    device_data = models.ForeignKey(Device_Data, on_delete=models.CASCADE, related_name='ports')
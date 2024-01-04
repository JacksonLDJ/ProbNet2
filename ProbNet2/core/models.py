# models.py
#Resources used: https://docs.djangoproject.com/en/5.0/topics/db/models/
from django.db import models

#Models used for the SQLWorkbench Database.
#id fields are automatically generated by Django so are not written here.

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

    


class Port(models.Model):
    protocol = models.CharField(max_length = 256)
    portid = models.PositiveSmallIntegerField()
    reason = models.CharField(max_length = 256)
    reason_ttl = models.CharField(max_length = 256)
    device_data = models.ForeignKey(Device_Data, on_delete=models.CASCADE, related_name='ports')
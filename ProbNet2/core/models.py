from django.db import models

class Customer_data(models.Model):

    Customer_ID = models.CharField(max_length=256, primary_key=True)
    Customer_Name = models.CharField(max_length=30)
    Customer_Contact = models.CharField(max_length=12)
    Company_Name = models.CharField(max_length=30)


class Device_Data(models.Model):
    Device_ID = models.CharField(max_length=256, primary_key=True)
    IP_Address = models.GenericIPAddressField()
    MAC_Address = models.CharField(max_length=20)
    Operating_Sytem = models.CharField(max_length=256)
    customer_data = models.ForeignKey(Customer_data, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True, help_text="Time and date this was created")
    updated_on = models.DateTimeField(auto_now=True, help_text="Time and date this was updated")

    class Meta:
        ordering = ['-created_on']

class Vulnerability_Data(models.Model):
    Vuln_ID = models.CharField(max_length=256, primary_key=True)
    Vuln_Name = models.CharField(max_length=256)
    Vuln_Desc = models.CharField(max_length=256)
    Vuln_Severity = models.DecimalField(max_digits=3, decimal_places=1, validators=[models.MinValueValidator(1.0), models.MaxValueValidtator(10.0)])

class Network_Services(models.Model):
    Service_ID = models.CharField(max_length=256, primary_key=True)
    Service_Name = models.CharField(max_length=True)
    Port_Number = models.CharField(max_length=True)

class Scan_History():

    target = models.GenericIPAddressField()
    hosts = models.ManyToManyField(Device_Data)

     # Choices for field type
    QUICK = 'QS'
    FULL = 'FS'
    TYPE_CHOICES = [
        (QUICK, 'Quick scan'),
        (FULL, 'Full scan'),
    ]

    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=QUICK,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    updated_on = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )

    class Meta:
        ordering = ['-id']




from django.db import models

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.vendor_name

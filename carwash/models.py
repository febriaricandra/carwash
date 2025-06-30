from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    vehicle_plate = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()

class Payment(models.Model):
    booking = models.ForeignKey("Booking", on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=[("cash", "Cash"), ("transfer", "Transfer")])
    is_paid = models.BooleanField(default=False)
    proof = models.ImageField(upload_to='payment_proofs/', null=True, blank=True)
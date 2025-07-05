from django.db import models

class Conditioners(models.Model):
    name = models.CharField(max_length=100)  # Model nomi (masalan: LG DualCool)
    brand = models.CharField(max_length=50)  # Brendi (masalan: LG, Samsung)
    cooling_capacity = models.CharField(max_length=20, blank=True, null=True)  # Sovutish quvvati (masalan: 2.0HP yoki 18000 BTU)
    power_consumption = models.CharField(max_length=50, blank=True, null=True)  # Quvvat sarfi (masalan: 220V/50Hz)
    inverter = models.BooleanField(default=False)  # Inverter bormi yo'qmi
    room_size = models.CharField(max_length=50, blank=True, null=True)  # Qaysi xona o'lchami uchun (masalan: 20-25 m²)
    noise_level = models.CharField(max_length=20, blank=True, null=True)  # Shovqin darajasi (masalan: 36 dB)
    functions = models.TextField(blank=True, null=True)  # Qo'shimcha funksiyalar (masalan: Wi-Fi, qizitish, avto tozalash)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narxi
    image = models.ImageField(upload_to='conditioners/', blank=True, null=True, default='default/conditioner.png')  # Rasm
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

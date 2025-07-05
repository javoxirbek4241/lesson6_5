from django.db import models

class Cameras(models.Model):
    name = models.CharField(max_length=100)  # Kamera nomi (masalan: Hikvision DS-2CE70DF0T)
    brand = models.CharField(max_length=50)  # Brend (masalan: Hikvision, Dahua)
    resolution = models.CharField(max_length=30, blank=True, null=True)  # Ruxsat (masalan: 1080p, 4K)
    lens = models.CharField(max_length=50, blank=True, null=True)  # Ob'ektiv (masalan: 2.8mm)
    night_vision = models.BooleanField(default=False)  # Tungi ko‘rish funksiyasi bormi
    connectivity = models.CharField(max_length=50, blank=True, null=True)  # Ulanish turi (masalan: Wi-Fi, LAN, PoE)
    power = models.CharField(max_length=30, blank=True, null=True)  # Quvvat manbai (masalan: 12V DC)
    features = models.TextField(blank=True, null=True)  # Qo‘shimcha funksiyalar (masalan: harakat aniqlash, ovoz yozish)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narxi
    image = models.ImageField(upload_to='cameras/', blank=True, null=True, default='default/cam.png')  # Kamera rasmi
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name}"


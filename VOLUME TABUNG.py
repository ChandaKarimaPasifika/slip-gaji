# Program 3: Menghitung Volume Tabung
# Menggunakan class dan method
import math

class Tabung:
    def __init__(self, radius, tinggi):
        self.radius = radius
        self.tinggi = tinggi
    
    def hitung_volume(self):
        return math.pi * self.radius ** 2 * self.tinggi

tabung1 = Tabung(7, 10)
print(f"Volume tabung adalah: {tabung1.hitung_volume()}")

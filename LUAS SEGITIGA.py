# Program 1: Menghitung Luas Segitiga
# Menggunakan input langsung dari pengguna
def luas_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga adalah: {luas}")

luas_segitiga()
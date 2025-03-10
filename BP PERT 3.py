umur = int(input("Masukkan umur: "))

if umur <= 5:
    print("Balita")
elif umur > 5 and umur <= 13:
    print("Anak-anak")
elif umur > 13 and umur <= 25:
    print("Remaja")
elif umur > 5 and umur <= 35:
    print("Dewasa")
elif umur > 35 and umur <= 55:
    print("Orang Tua")
else:
    print("Lansia")



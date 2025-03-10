nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")


gaji = 0
bonus = 0


if status.lower() == "pegawai tetap":
    gaji = 1000000
    if golongan.lower() == "a":
        bonus = 200000
    elif golongan.lower() == "b":
        bonus = 400000
    elif golongan.lower() == "c":
        bonus = 550000
elif status.lower() == "honor":
    gaji = 750000
    if golongan.lower() == "a":
        bonus = 150000
    elif golongan.lower() == "b":
        bonus = 275000
    elif golongan.lower() == "c":
        bonus = 480000
else:
    print("Status yang dimasukkan tidak valid.")
    exit()


gaji_total = gaji + bonus


print("\n===== Slip Gaji =====")
print(f"Nama: {nama}")
print(f"NIK: {nik}")
print(f"Status: {status}")
print(f"Golongan: {golongan}")
print(f"Gaji Pokok: Rp {gaji:,}")
print(f"Bonus: Rp {bonus:,}")
print(f"Gaji Total: Rp {gaji_total:,}")
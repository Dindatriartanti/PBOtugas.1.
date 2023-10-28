print("Program menghitung luas dan keliling Belah ketupat")
"""
Programmer: Dinda Tri Artanti
pertemuan:1
Tanggal : 22 Oktober 2023
"""
 

def keliling():
    sisi = int(raw_input("Masukkan Nilai Sisi: "))

    # Masukkan ke dalam rumus
    keliling = 4 * sisi
    #hasil
    print("Keliling Belah Ketupat adalah: %d" %keliling)

def luas():
    diagonal_1 = int(raw_input("Masukkan Nilai Sisi Diagonal 1: "))
    diagonal_2 = int(raw_input("Masukkan Nilai Sisi Diagonal 2: "))

    #masukkan ke dalam rumus
    luas = (diagonal_1 * diagonal_2) / 2

    #hasil
    print("Luas Belah Ketupat adalah: %d" %luas)

print,"MENU PILIHAN",
print,"============",
print,"1. Keliling",
print,"2. Luas",
print,"3. Keluar",
print,"============",
print,"",

masukkan = int(raw_input("masukkan menu: "))
if masukkan == 1:
    keliling()
elif masukkan == 2:
    luas()
else:
    print("Terima Kasih")
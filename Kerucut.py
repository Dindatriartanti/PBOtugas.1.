print("Aplikasi Menghitung Luas dan volume kerucut")
"""
Nama  : Dinda Tri Artanti
NIM   : 220511036
Kelas : TI22K
PBO   : Tugas Pertemuan 1

Keterangan:
L = Luas permukaan kerucut
r = Jari-jari
T = Tinggi
s = Garis pelukis
phi = 3,14
"""

phi = 3.14
r = 7
s = 8
T = 9


luas_selimut = phi * r * s
luas_permukaan = (phi * r * s) + (phi * r**2)
volume = 1/3 * phi * r**2 * T


print("Phi:", phi)
print("Jari-Jari:", r)
print("Tinggi:", T)
print("Garis Pelukis:", s)
print("Luas Selimut:", luas_selimut)
print("Luas Permukaan:", luas_permukaan)
print("Volume:", volume)
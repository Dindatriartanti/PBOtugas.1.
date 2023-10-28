print("Program menghitung luas dan keliling silinder tabung")
"""
Programmer:Dinda Tri Artanti
NIM : 220511036
Kelas : T122K
pertemuan:1
Tanggal : 22 

Keterangan:
L = Luas permukaan tabung
r = Jari - jari lingkaran tabung
T = Tinggi
phi = 3.14
"""

# Atur Nilai
phi = 3.14
r = 22
T = 50

# Rumus
luas_selimut = 2 * phi * r * T
luas_permukaan = (2 * phi * r * T) + (2 * phi * r**2)
volume = phi * r**2 * T

# output
print("Phi:", phi)
print("Jari - Jari Lingkaran Tabung:", r)
print("Tinggi:", T)
print("Luas Selimut:", luas_selimut)
print("Luas Permukaan:", luas_permukaan)
print("Volume:", volume)
import math

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

r = float(input("Masukkan jari-jari lingkaran: "))
luas = luas_lingkaran(r)
print(f"Luas lingkaran adalah: {luas:.2f}")

import math

def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari ** 2 * tinggi

r=float(input("Masukkan jari-jari tabung: "))
t=float(input("Masukkan tinggi tabung: "))

volume = volume_tabung(r,t)
print(f"Volume tabung adalah: {volume:.2f}")
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

alas = float(input("Masukkan panjang alas: "))
tinggi = float(input("Masukkan tinggi: "))

luas = luas_segitiga(alas, tinggi)
print(f"Luas segitiga adalah: {luas}")
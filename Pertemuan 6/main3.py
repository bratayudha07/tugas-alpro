angka_genap = 0
angka_ganjil = 0

angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

while angka != 0:
    if angka % 2 == 1:
        angka_ganjil += 1
    else:
        angka_genap += 1

    angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

print("Jumlah Angka Ganjil:", angka_ganjil)
print("Jumlah Angka Genap:", angka_genap)

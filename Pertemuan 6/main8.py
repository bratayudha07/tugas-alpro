angka_rahasia = 7

print("Tebak angka rahasia pesulap (1-10)!")

while True:
    tebak = int(input("Masukkan tebakanmu: "))

    if tebak == angka_rahasia:
        print("Hebat! Tebakanmu benar.")
        break
    elif tebak < angka_rahasia:
        print("Terlalu kecil, coba lagi.")
    else:
        print("Terlalu besar, coba lagi.")

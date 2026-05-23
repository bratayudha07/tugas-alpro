def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n - 1)


angka = 5
hasil = faktorial(angka)
print(f"Faktorial dari {angka} adalah {hasil}")

menu = {1: "Tambah data", 2: "Lihat data", 3: "Keluar"}

try:
    pilihan = int(input("Pilih menu (1-3): "))
    if pilihan not in menu:
        raise ValueError("Menu tidak tersedia")
    print(f"Kamu memilih: {menu[pilihan]}")

except ValueError as e:
    print(f"Error: {e}")

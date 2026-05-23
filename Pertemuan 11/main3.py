def tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 100 == 0:
        return False
    elif tahun % 4 == 0:
        return True
    else:
        return False


def hari_didalam_bulan(tahun, bulan):
    if bulan < 1 or bulan > 12:
        return None

    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28

    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    return 30


def hari_pada_tahun(tahun, bulan, hari):
    maks_hari = hari_didalam_bulan(tahun, bulan)
    if maks_hari is None or hari < 1 or hari > maks_hari:
        return None

    total = 0
    for m in range(1, bulan):
        jumlah_hari_bulan_ini = hari_didalam_bulan(tahun, m)
        if jumlah_hari_bulan_ini is not None:
            total += jumlah_hari_bulan_ini

    return total + hari


data_uji_thn = [2000, 2016, 1987, 2023]
data_uji_bln = [12, 2, 11, 2]
data_uji_hr = [31, 29, 30, 29]
data_hasil = [366, 60, 334, None]

for i in range(len(data_uji_thn)):
    thn = data_uji_thn[i]
    bln = data_uji_bln[i]
    hr = data_uji_hr[i]
    print(thn, bln, hr, "->", end=" ")
    hasil = hari_pada_tahun(thn, bln, hr)
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")

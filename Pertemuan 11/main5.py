def Liter100km_ke_mpg(liter):
    mil = 100000 / 1609.344
    galon = liter / 3.785411784
    return mil / galon


def mpg_ke_Liter100km(mil):
    km100 = 100000 / 1609.344
    liter = (km100 / mil) * 3.785411784
    return liter


print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))

print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))

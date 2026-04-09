def kareleri_bul(sayilar):
    sonuc = []
    for x in sayilar:
        if x not in sonuc:
            sonuc.append(x * x)
    return sonuc
def rate_calculation(sum,rate,time):
    rate_calculation = sum*(rate/100)*time 
    return rate_calculation 
rate1 = rate_calculation(10000, 5, 3)
rate2 = rate_calculation(25000, 7, 5)
print(f"Простий відсоток для першого випадку: {rate1}")
print(f"Простий відсоток для другого випадку: {rate2}")

def maibutnya_vartist(potribna_suma, richna_stavka, kilkist_rokiv):
    maibutnya_vartist = potribna_suma*(1+richna_stavka/100)**kilkist_rokiv
    return round(maibutnya_vartist)

maibutnya_vartist1 = maibutnya_vartist(5000, 6, 10)
maibutnya_vartist2 = maibutnya_vartist(12000, 4.5, 7)
print(f"Майбутня вартість першої інвестиції: {maibutnya_vartist1}")
print(f"Майбутня вартість другої інвестиції: {maibutnya_vartist2}")

def podatok(dokhid):
    if dokhid < 20000:
        return 0
    elif dokhid <= 50000:
        return dokhid*0.1
    else:
        return dokhid*0.15
print (podatok(40000))

def roz_zag_vitrat(kilkist_produktu, vartist_odunici):
    return kilkist_produktu*vartist_odunici

def roz_zag_dohodu(kilkist_productu, cina_odunici ):
    return kilkist_productu*cina_odunici
def analiz_prinutku(kilkist, vartist, cina):
    zagvit = roz_zag_vitrat
    return zagvit
    zagdokh = roz_zag_dohodu
    prybutok = zagdokh - zagvit

print(f"Загальні витрати: {roz_zag_vitrat}")
print(f"Загальний дохід: {roz_zag_dohodu}")
print(f"Прибуток: {prybutok}")


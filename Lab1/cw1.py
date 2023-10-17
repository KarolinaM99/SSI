import pandas as pd

def wczytaj_plik(plik_probki, plik_typy,separator):
    try: 
        probki = pd.read_csv(plik_probki, sep=separator, header=None)
        probki_typ = pd.read_csv(plik_typy, sep=separator, header=None)
        return probki, probki_typ
    except FileNotFoundError:
        raise Exception('Nie znaleziono pliki z próbkami i/lub pliku z typami próbek')

def sprawdz_atrybuty(probki_type):
    czy_atr_symb = []
    nazwa_atr = []
    for i in probki_type.index:
        nazwa_atr.append(probki_type.iloc[i,0])
        znak = probki_type.iloc[i, 1]
        if znak == 's':
            czy_atr_symb.append(True)
        else:
            czy_atr_symb.append(False)
    return czy_atr_symb, nazwa_atr


probki, probki_typ = wczytaj_plik('iris.txt','iris-type.txt','\t')
print(probki)
print(probki[2][4])
czy_atr_symb, nazwa_atr = sprawdz_atrybuty(probki_typ)
print(czy_atr_symb)
print(nazwa_atr)
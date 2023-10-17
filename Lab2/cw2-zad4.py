import pandas as pd
import matplotlib.pyplot as plt

def wczytaj_plik(probki ,sep):
    probki = pd.read_csv(probki, sep=sep, header=None)
    return probki

def podzial_na_klasy(probki):
    class1 = probki[probki.iloc[:, -1] == 1]
    class2 = probki[probki.iloc[:, -1] == 2]
    class3 = probki[probki.iloc[:, -1] == 3]
    return class1, class2, class3

def stworz_wykres(class1, class2, class3):
    pary_atrybutow = [(2,3),(1,3),(0,3),(1,2)]
    for i in range(4):
        
        x1 = class1.iloc[pary_atrybutow[i][0]]
        y1 = class1.iloc[pary_atrybutow[i][1]]
        
        x2 = class2.iloc[pary_atrybutow[i][0]]
        y2 = class2.iloc[pary_atrybutow[i][1]]
        
        x3 = class3.iloc[pary_atrybutow[i][0]]
        y3 = class3.iloc[pary_atrybutow[i][1]]
        
        plt.subplot(2,2,i+1)
        plt.xlabel(f'Atrybut {pary_atrybutow[i][0]+1}')
        plt.ylabel(f'Atrybut {pary_atrybutow[i][1]+1}')
        plt.scatter(x1,y1,label="Klasa 1", color='orange')
        plt.scatter(x2,y2,label="Klasa 2", color='green')
        plt.scatter(x3,y3,label="Klasa 3", color='blue')
        plt.legend(loc='lower right', fontsize="8")
    
    plt.show()

probki = wczytaj_plik('iris.txt', sep='\t')
class1, class2, class3 = podzial_na_klasy(probki)
stworz_wykres(class1, class2, class3)
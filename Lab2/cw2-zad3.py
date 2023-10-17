import matplotlib.pyplot as plt
import numpy as np

def punkty_przeciwne(punkty):
    return [-x for x in punkty]

def rysuj_obrys_buzi(punkty):
    odwrotnie = list(reversed(punkty))
    przeciwne = punkty_przeciwne(punkty)
    odwrotnie_przeciwne = list(reversed(przeciwne))

    punkty_x = punkty + odwrotnie_przeciwne + przeciwne + odwrotnie
    punkty_y = odwrotnie + punkty + odwrotnie_przeciwne + przeciwne
    return punkty_x, punkty_y

def rysuj_wykres():
    
    punkt_x=[-1,0,1]
    punkt_y=[1,0,1]
    
    x = np.linspace(-1,1)
    #np.pi/2*x - odpowiada za rozciąganie lub zwężanie funkcji sin, im większy x tym staje się bardziej falowana
    #np.p/2 - przesuwa sinusoidę w lewo lub prawo, gdy - w lewo o jeden okres
    #sin(pi/2) = 1
    y = np.sin(np.pi/2*x - np.pi/2)
    
    punkty_x, punkty_y = rysuj_obrys_buzi([-2,-1.8,-1.4,-0.8,0])
    
    plt.ylim(-3,3)
    plt.xlim(-2,2)
    plt.xticks(np.arange(-2,3,1))
    plt.grid(color="black", linewidth=1.5)
    plt.plot(punkty_x,punkty_y, color="red", linewidth=3, label="lamana")
    plt.scatter(punkt_x,punkt_y, color='blue', marker='D', zorder=2, s=100)
    plt.scatter([], [], label="punkty", color="blue", marker="D")
    plt.plot(x,y, color='yellow', linewidth=2, label="sinus") # mnożymy przez -1, ponieważ chcemu uzyskać odwrotność łuku
    plt.legend(loc='upper right', bbox_to_anchor=(1.3,1.05), frameon=False)
    plt.show()
    
print(rysuj_wykres())
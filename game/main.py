import random
from game.p_s_s import Schere,Stein,Papier
from game.menu import menu
def main():
    nrc=0
    nrm=0
    while nrc<3 and nrm<3:
        list = [Schere, Papier, Stein]
        calculator = random.choice(list)
        mensch = input("wahlen sie :Papier ,Stein oder Schere:=")
        if mensch == 'Papier':
            func = Papier
        if mensch == 'Schere':
            func = Schere
        if mensch == 'Stein':
            func = Stein

        print("Meine Entscheidung :")
        calculator()
        print("Deine Entscheidung")
        func()

        if calculator==Stein and func==Schere:
            nrc+=1
        if calculator==Schere and func==Stein:
            nrm+=1
        if calculator==Stein and func==Papier:
            nrm+=1
        if calculator==Papier and func==Stein:
            nrc+=1
        if calculator==Schere and func==Papier:
            nrc+=1
        if calculator==Papier and func==Schere:
            nrm+=1
        print(f' Ich habe {nrc} Punkte und du hast {nrm} Punkten')
    if nrm==3:
        print('iuhuuu,du hast gewonnen ! Herzlichen Gluckwunsch!')
    if nrc==3:
        print('Schade aber du hast verloren!Konnen wir nochmal spielen')
print(menu())
main()
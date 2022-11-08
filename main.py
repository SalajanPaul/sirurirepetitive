
def sir5():
    print("Introduceti un sir de numere naturale:")
    contor = 0
    sir = input()
    for index in range(0,len(sir), 1):
        if sir[index] == "5":
            contor += 1
    print("Numarul de aparitii a cifrei 5 este:", contor)


def incadrare():
    print("Introduceti un numar natural intre 0 si 10000 ", end="")
    nr = int(input())
    if nr < 4000:
        print("mic")
    else:
        if nr < 8000:
            print("mediu")
        else:
            print("mare")


def adunare():
    print("a= ", end="")
    a = int(input())
    print("b= ", end="")
    b = int(input())
    print("a+b=", a + b)

def scadere():
    print("a= ", end="")
    a = int(input())
    print("b= ", end="")
    b = int(input())
    print("a-b=", a - b)

def inmultire():
    print("a= ", end="")
    a = int(input())
    print("b= ", end="")
    b = int(input())
    print("a*b=", a * b)

def impartire():
    print("a= ", end="")
    a = int(input())
    print("b= ", end="")
    b = int(input())
    print("a//b=", a // b)

def meniu():
    print("Meniu: 1 - adunare, 2 - scadere, 3 - inmultire, 4 - impartire.")
    opt = input().strip()
    if opt == "1":
        print("adunare")
        adunare()
    else:
        if opt == "2":
            print("scadere")
            scadere()
        else:
            if opt == "3":
                print("inmultire")
                inmultire()
            else:
                if opt == "4":
                    print("impartire")
                    impartire()
                else:
                    print("Va rog folositi doar cifrele 1, 2, 3, 4")


if __name__ == '__main__':
    e = ""
    while e != "0":
        meniu()
        print("Daca doriti sa iesiti, apasati tasta 0, daca nu orice alta cifra")
        e = input()



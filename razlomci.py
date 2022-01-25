# Напиши програм који сабира и множи разломке.
#
# Улаз: Са стандардног улаза се уносе два разломка, сваки у посебном реду. Сваки разломак је записан тако
# што је су записани његов бројилац и именилац, раздвојени карактером /.
#
# Излаз: На стандардни излаз исписати у првом реду збир, а у другом производ разломака. Разломци се
# исписују у истом формату у ком су учитани, максимално скраћени (бројилац и именилац су узајамно прости).
#
# Пример
# Улаз
# 2/3
# 1/4
# Излаз
# 11/12
# 1/6

def NZD(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def Skrati(r):
    (brojilac, imenilac) = r
    nzd = NZD(brojilac, imenilac)
    brojilac //= nzd
    imenilac //= nzd
    return (brojilac, imenilac)

def Saberi(a, b):
    (a_brojilac, a_imenilac) = a
    (b_brojilac, b_imenilac) = b
    brojilac = a_brojilac*b_imenilac + a_imenilac*b_brojilac
    imenilac = a_imenilac*b_imenilac;
    return Skrati((brojilac, imenilac))

def Mnozi(a, b):
    (a_brojilac, a_imenilac) = a
    (b_brojilac, b_imenilac) = b
    brojilac = a_brojilac * b_brojilac
    imenilac = a_imenilac * b_imenilac;
    return Skrati((brojilac, imenilac))

def Ucitaj():
    (brojilac, imenilac) = map(int, input().split("/"))
    return (brojilac, imenilac)

def Ispisi(razlomak):
    (brojilac, imenilac) = razlomak
    print(brojilac, "/", imenilac, sep="")


a = Ucitaj()
b = Ucitaj()
Ispisi(Saberi(a, b))
Ispisi(Mnozi(a, b))

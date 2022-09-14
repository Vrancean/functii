a=int(input('dati numaratorul primei fractie:'))
b=int(input('dati numitorul primei fractie:'))
x=int(input('dati numaratorul 2 fractie:'))
y=int(input('dati numitorul 2 fractie:'))
from fractions import Fraction
def sumafractiilor():
    s=Fraction(a,b)+Fraction(x,y)
    return s
def produsfractiilor():
    p=Fraction(a,b) * Fraction(x,y)
    return p
print('suma=', sumafractiilor())
print('produsul=', produsfractiilor())
#!/usr/bin/python

a = input("Quantidade total de VG?: ")
b = input("Quantidade total de PG?: ")
c = input("Tamanho de cada frasco?: ")
d = input("Porcentagem da essencia?: ")
e = input("Porcentagem de vg?: ")
f = input("Porcentagem de pg?: ")

vgml = c * e / 100
eml = c * d / 100
pgml = c * f / 100 - eml

print 'VG=', vgml, 'ml '
print 'PG=', pgml, 'ml'
print 'Essencia=', eml, 'ml'

assert isinstance(b, object)
if a >= b:
    frasco = a / vgml
else:
    frasco = b / pgml

print 'Numero de frascos que voce fara=', frasco,

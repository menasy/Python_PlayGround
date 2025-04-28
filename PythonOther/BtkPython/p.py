# -*- coding: utf-8 -*-
a = 4
b = 20

a, b = b,a
print(a,b)

print(a//b)

print(a, '+', b, '=', a + b)
print(a, "bolu", b, '=', a / b)
print(a, 'ussu', b, '=', a ** b)


c = (4>3)
d = (8 == 7)
print(c)
print(d)



x = 53.5
print('Float x: {}'.format(x))
print(type(x))

x = (int)(x) # inte cevirdik
print("int x :", x)
print(type(x))
print('int x toplami : ', x+x)

x = (str)(x) # stringe cevirdik
print(type(x))
print('str x toplami : ',x + x) # x lerı yan yana yazdi toplama yapmadi str oldugu icin

import keyword
print(keyword.kwlist) #anahtar kelimeleri listeledik

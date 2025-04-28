# -*- coding: utf-8 -*-
#								input() fonksiyonu

ad = input("isminiz:")
print("isim: ",ad)
print("-	-	input -	-	-\n")

#							print() fonksiyonu
#sep() fonksiyonu ayracı belirtir aralarına hangi ayracı koyacağını belirtiyorsun
print('a','b','c')
print('a','b','c', sep = '/')
print("FB"*3) #toplama ve çarpma işlemleri sitringlerde de olabiliyor.
print("memo",end = ('\n')) #end komutunu printimizin alt satıra geçmesini istemiyorsak ya da hangi karakterle bitmesini istiyorsak onu girmek için kullanırız
print("-	-	sep,end -	-	-\n")

# 							format()
print("ad = {}".format(ad)) #bu dört kullanım da doğrudur hepsi aynı işlevi gorur
print(f"ad = {ad}")
print("ad =",ad)
print("ad = "+ad)
print("-	-	format -	-	-\n")

print(" ___","\n""/* *\\\n","\\./")

#			ortalama

s1 = int(input("sinav1 = "))
s2 = int(input("sinav2 = "))

print("Ortalama = {}".format((s1+s2)/2))

# 		yas hesaplama

dtarih = int(input("dogum tarihiniz = "))
yas = 2023 - dtarih
print("yaşınız : ",yas)

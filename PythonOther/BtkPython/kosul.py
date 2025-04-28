# -*- coding: utf-8 -*-
#			if:

if (3<5) and (4<7):
	print("True")
if (3<5) & (8>7):
	print("folse")
print("-	-	if else syntax -	-	-\n")

#			ortalama hesabı

s1 = int(input("1. sinav: "))
s2 = int(input("2. sinav : "))
ortalama = (s1+s2)/2

if ortalama >= 80:
	print(f"Ortalmaniz: {ortalama} Takdir belgesi aldınız")
elif ortalama >= 70:
	print(f"Ortalmaniz: {ortalama} Teşekkür blgesi aldınız")
else:
	print(f"Ortalmaniz: {ortalama} belge alamadınız :( ")
print("-	-	ortalama hesabı -	-	-\n")

#			sifre/kullanıcı adı

rad = "Menasy"
rsifre = "Mm7347"
k_ad = str(input("kullanıcı adınızı giriniz : "))

if k_ad == rad:
	k_sifre = str(input("Sifrenizi giriniz : "))
	if k_sifre == rsifre:
		print("Giriş başarılı")
	else:
		print("sifreniz yanlış, lutfen tekrar deneyiniz")
else:
	print("kullanıcı adınız hatalı, lutfen tekrar deneyiniz")


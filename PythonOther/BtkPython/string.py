# -*- coding: utf-8 -*-
# ctrl ö satır açıklamsı aç kapat

#				index

string = "Fener Bahce"
print(string[-2]) # - deger girince sondan başlayarak indeksliyor -1 en son olmak uzere

print("-	-	İndex	-	-	-\n")

#				String birleştirme

# string birleştirme işlemi + operatoru ile yapılır.abs

a = "FENER"
A = "BAHCE"
b = a+A
B = a[2] + A[-4]
print(b)
print(B)
print("-	-	String birleştirme	-	-	-\n")

#					String bölme

# : nokta işareti ile yapılır

s = "DusanTadic"
print(s[:]) # herhangi bir bolme yapmadığımız için tum stringi verir

print("baş : ",s[3:]) # İndisten itibaren olan stringi verir
print("son : ",s[:3]) # Bir değer girilmediği için en baştan başlayarak girilen indise kadar yazdırır 3 dahil değil
print("aralıklı : ",s[5:8]) # 5 değerinden başlayarak 8 indisine kadar yazdırır 8 dahil edilmez
print("artışlı : ",s[1::2]) # 1. indisten başlayarak 2 şer artıp denk gelen karaktrleri yazdırır
print("aralıklı artışlı : ",s[1:8:3]) # 1. indisten 8 e kadar ucer ucer artar. artışta denk gelenleri yazdırır.
print("eksili artışlı : ",s[::-2]) # sondan başlayarak ikişer ilerler denk gelen indisi yazdıır
print("eksili baş : ",s[-3:]) # sitringin sonundan başlayıp indis kadar yazdırır
print("eksili son : ",s[:-3]) # sondan başlayrak bu indisten itibaren yazdırır

print("-	-	String bölme	-	-	-\n")

#				String Değiştirme

ns = s[:5] + ' FERDİ' + s[-4:]
print("New string : ",ns)

adres = "Temel Mahallesi-Sultangazi-İstanbul" # mahalle = Ziya Gökalp Mahallesi, Başakşehir
nwadres = "Ziya Gökalp " + adres[6:16] + "Başakşehir" + adres[-9:]
print("New Adres : ",nwadres)

# Yukkardaki kullanıma gerek kalmadan bunu yapan replace(old str,new str,count) fonksiyonu var

adres1 = "Şırnak-idil-karalar"
nwadres1 = adres1.replace("karalar","araban")
print("Replace adres : ",nwadres1)

print("-	-	String Değiştirme	-	-	-\n")

#				String Silme

yazi = "FenerBahce"
i = 0
j = -1

#	PROGRAM 1

#sil = int(input("Sondan silmek için '9' yi, baştan silmek için '1' yi tuşlayınız: "))
#while True:
#	if sil == 0:
#		break
#	elif (sil == 1) and (i < len(yazi)):
#		basyazi = yazi[i:]
#		print(basyazi)
#		i += 1
#	elif (sil == 9) and (j > ( -len(yazi))):
#		sonyazi = yazi[:j]
#		print(sonyazi)
#		j -= 1
#	else:
#		break

# PROGRAM 2

# print("Programı sonlandırmak için 0 tuşlayın")
# while True:
# 	control = str(input("Baştan silmek için 'b' yi sondan silmek için 's' yi tuşlayınız : "))
# 	if (control == 'b') or (control == 's'):
# 		sil = int(input("Silmek istediğiniz karakter adedini girin : "))
# 		if	sil == 0:
# 			break
# 		elif sil < len(yazi):
# 			if control == 's':
# 				nwyazi = yazi[:-sil]
# 				print("New string : ",nwyazi)
# 			elif control == 'b':
# 				nwyazi = yazi[sil:]
# 				print("New string : ",nwyazi)
# 		else:
# 			print("Geçersiz bir değer girdiniz")
# 			break
# 	else:
# 		print("Geçersiz bir tuşlama yaptınız")

for	x in range(0,8):
	print(yazi[x:])
for	x in range(1,5):
	print(yazi[:-x])

print("-	-	String silme	-	-	-\n")

#				for ile string elemanlarına erişme

dizi = "FerdiKadıoğlu"

for x in dizi:
	print(x, end = ' ')
print("\n")
print("-	-	for ile string elemanlarına erişme	-	-	-\n")

#				stringi listeye çevirme

# split fonksiyonu stringi listeye cevirmeye yarıyor
ad = "Mehmet_Nasim_Yılmaz_Menasy"

print(ad.split('_'))

print("-	-	stringi listeye çevirme	-	-	-\n")

#			stringin karakterlerini sayma

# len() uzunluğunu ölçer
# count() girilen karakterden kaç tane olduğunu sayar

print("stringin uzunluğu : ",len(ad))
print("stringin içinde geçen 'm' karakter adedi : ",ad.count('m'))

print("-	-	stringin karakterlerini sayma	-	-	-\n")

#			string ifadeleri karşılaştırma
# is komutu == gibi true kontrolu yapabiliyor ama aşağıdaki kodda çalışmadı.
print("memo" == "memo")
print("memo" is "memo")

kul ="menasy"
sifre = "7347"

k_giris = input("kullanıcı adınızı giriniz: ")
if k_giris == kul:
	s_giris = input("Sifrenizi giriniz : ")
	if sifre == s_giris:
		print("Giriş başarılı")
	else:
		print("Şifreyi yanlış girdiniz")
else:
	print("Kullanıcı adınızı yanlış girdiniz")

print("-	-	string ifadeleri karşılaştırma	-	-	-\n")

#				stringi ters cevirme

print(kul[::-1])
print('/'.join(reversed(kul))) # '' içine ters cevirirken aralara ne koymasını istiyorsak onu yazarız
print("-	-	stringi ters cevirme	-	-	-\n")

#				string içersinde string kontrolu

# aranan kısım aynı şekilde varsa true dondurur
isim = "mehmet nasim yılmaz"
print("mehmet"in isim)
print("nas" in isim)
print("AAASADDnasADFFFWF" in isim)
print("-	-	string içersinde string kontrolu	-	-	-\n")

# 			bolum sonu programı
# polindrom uygulaması (terten ve normal okunuşu aynı olan string)

deger = input("Polindrom kontrolu yapılacak bir yazı yazınız: ")

revdeger = ''.join(reversed(deger))

if deger == revdeger:
	print("Girdiğiniz yazı polindromik bir yazıdır. ")
else:
	print("Girdiğiniz yazı polindromik yazı değildir")

# -*- coding: utf-8 -*-

#				liste(c deki dizi mantığı)
# listeler çift boyutlu dizi gibidir. pyt da hem string hem de integer dğer alailir.
liste = ['her','zaman','her','yerde','en buyuk','FENER',1907,7347]
print(liste)
print(liste[5])
liste1 = "Dusan tadic" #boyle de tek boyutlu dizi oluyor
print(liste1)
print("-	-	liste	-	-	-\n")

#				in / not in

print('FENER' in liste) # eğerki aradığımız değer varsa true yoksa folse dondurur
print('FENER' not in liste)
#Rezarvasyon programı

rezerv = ['mehmet','fatih','kadir','nemli']
isim = input("Rezarvasyon kontrolu için isminizi giriniz: ")
if isim in rezerv:
	print("rezarvasyonunuz mevcuttur. '{}' numaralı masaya geçebilirsiniz".format(rezerv.index(isim) + 1))
elif isim not in rezerv:
	print("Rezarvasyonunuz bulunamadı")
print("-	-	in/not in	-	-	-\n")

#				range() fonksiyonu

# belirledğimiz aralıkta ya da girdiğimiz tek değer adedi kadar ilerler
#for dongusu içinde kullanılır ve for un ne kadar donecğini belirtir.
range(2,5) 		#ikisi arasında birer birer artarak ilerler
range(3) 		# 0 dan başlar 3 ya kadar birer birer artarak ilerler.
range(1,10,2) 	# 1 den başlayıp 10 a kadar 2 şer artarak ilerler.
range (15,3,-4)	#15 ten 3 e kadar 4 er azalarak ilerler

for a in range(2, 5): #ikili kullandığımızda son sayı dahil ediliyor
	print(a)
print("-------")

for a in range(3):
	print(a)
print("-------")

for a in range(8,0,-2):
	print(a)
print("-------")

for a in range(2,10,2): #ortada yazdığımızda dahil olmuyor son sayı.
	print(a)
print("-------")
print("-	-	range	-	-	-\n")

#					for

# for un şartı ve nekadar sureceği bellidir.
#tek sayılar

for a in range(1,30,2):
	print(a,end = ' ')
print("\n")
print("-	-	for	-	-	-\n")

#					while

# while ın sonlanması bir şarta bağlıdır. ne zaman biteceğine koşullar karar verir
x = 5
y = 5
while (x > 1):
	y *= (x - 1)
	x -= 1
print(f"x in faktoryeli : {y}\n")

#					break

print("---Çıkmak için 0 ı tuşlayınız---")
while True:
	nb = int(input("Bir sayı giriniz : "))
	print("sayının karesi", nb*nb)
	if nb == 0:
		break
#				continue

# bir sonraki bloğa geçmesini soyler atlıyor yani
for a in range(100):
	if (a % 7 == 0):
		continue
	print(a,end = ' ')
print("\n")

# çarpım tablosu

for a in range(1,11):
	for b in range(1,11):
		print(a,'*',b,'=',a*b)
	print("\n")

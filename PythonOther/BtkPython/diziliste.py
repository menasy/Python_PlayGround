# -*- coding: utf-8 -*-

#				liste

#listeler çift pointerli dizi gibidir ve her turden değer alabilir. ve turu 'list' dir

liste = ['mehmet','N',73,'y','FB',47]

print(liste)
print(type(liste))

print("-	-	liste tanımı	-	-	-\n")

#			listedeki elemanın indisini oğrenme index()

print("karakterin indis numarası : ",liste.index('y'))
print("")
print("-	-	index()	-	-	-\n")

#			liste dilimleme

print(liste[2:5]) # 2 den 5 e
print(liste[1:5:2]) # 1 den 5 e ikişer
print(liste[::2]) # ikişer
print(liste[-3:])
print(liste[:-3])
print(liste[:])
print("")
print("-	-	liste dilimleme	-	-	-\n")

#			listeye eleman ekleme
# append(eleman) fonksiyonu lullanılarak eklenir en sona ekleme yapar
# insert(indis,eleman) fonksiyonu ile istediğimiz yere ekleme yaparız

# nwlist = [liste[:1] + 'Nasim' + liste[2:]]
# print("New list : ",nwlist)

liste.append('Mn')
print("New list append : ",liste)

liste.insert(3,"yılmaz") # istenilen indise değeri atar ve sonrasındakileri bir kaydırır
print("New list insert : ",liste)

a = [7,3]
i = 1
for x in range(2):
	sayi = input(f"Eklemek istediğiniz {i}. elemanı giriniz : ")
	a.append(sayi)
	i += 1
print("New a :",a)
x = 0
for x in range(i+1):
	print(f"a[{x}] = {a[x]} ",end = ' ')
	x+=1
print("")
print("-	-	-	listeye eleman ekleme	-	-	-\n")
i =1
x = 0
#				liste birleştirme

b = ['dusan','tadic',10]
print("Birleştirilmiş L Listesi : ",b + a)

# extend() fonksiyonu en başta girilen listeye bir sonrakini ekler
# yukarıdakinden farkı ekleme oluyor yanı a mız değişiyor

a.extend(b) # b listesini a listesine ekliyor
print("Extend birleştirme a : ",a)

b.extend(a) # a listesini b listesine ekliyor
print("Extend birleştirme b : ",b)
print("")
print("-	-	-	liste birleştirme	-	-	-\n")

#				listeyi tersten yazma

print("Değişiklik olmadan ters : ",a[::-1]) # burda sadece ters dondurup çıktı verir liste değişmez
print("Değişiklik kontrolu : ",a)
a.reverse() # burda ise listeyi ters cevirir ve bundan sonra liste ters olarak kalır
print("Reverse : ",a)
print("")
print("-	-	-	listeyi tersten yazma	-	-	-\n")

#				Listenin max min değerlrini bulma

lint = [73,47,34,882,271]
print("Min : ",min(lint))
print("Max : ",max(lint))

lgiris = []
toplam = 0
for x in range(2):
	nb = int(input(f"{i}. Değer : "))
	toplam += nb
	lgiris.append(nb)
	i += 1
print("Kullanıcıdan alınan değerler : ",lgiris)
print("Max değeri : ",max(lgiris))
print("Min değeri : ",min(lgiris))
print("Max + Min = ",min(lgiris) + max(lgiris))
ao = toplam/(i-1)
print("Aritmetik ortalaması = ",ao)
print("")
print("-	-	-	Listenin max min değerlrini bulma	-	-	-\n")
i = 0
#					stringi listeye çevirme
string = "Freedd"
print("String :",string)
string = list(string)
print("Dönüştürülmüş string : ",string)
print("")
print("-	-	-	stringi listeye çevirme	-	-	-\n")

#					listeden eleman kaldırma
string.remove('e') # listeden bir tane e yi siliyor iki tane silmek istersek ikinci kez çağırcaz
print("Remove : ",string)
string.pop(4) # girdi olarak indis alıyor ve o indisteki elemanı siliyor
print("Pop : ",string)
string.clear() # stringin içindeki tum değerleri siliyor
print("Clear : ",string)
print("")
print("-	-	-	listeden eleman kaldırma	-	-	-\n")

#					listede arama yapma

l = [8,73,85,10,53,35]
print(8 in l)
print(20 in l)

#					liste elemanlarını sıralama

l.sort() # kuçukten buyuğe sıralamaya yarar
print("kucukten buyuğe sıralama : ",l)
l.reverse()
print("Buyukten kuçuğe sıralama : ",l)
boltek = (len(l)-1)/2
bolcift = int(boltek)
if len(l) % 2 != 0:
	tek = int(boltek + 0.5)
	print("Listenin medyanı : ",l[tek])
else:
	cift = (l[bolcift] + l[bolcift + 1]) / 2
	print("Listenin medyanı : ",cift)
print("")
print("-	-	-	liste elemanlarını sıralama	-	-	-\n")

#					liste elemanları numaralandırma

gun = ["pazartesi","salı","carsamba","persembe","cuma"]

for i, j in enumerate(gun): # j liste içersinde gezmene yarıyor i ise ayrı bir işlevde kullanılıyor
	print((i+1) , '. gün = ' , j)
	i += 1

print("")
print("-	-	-	liste elemanları numaralandırma	-	-	-\n")

#				Listeden yığın (stack) oluşturma

# listeye son giren ilk çıkar (last in - first out)
gun.append(5)
gun.append(3)
print("eklenmiş : ",gun)
gun.pop() # en son giren ilk çıkar popun içine bir değer girmediğimizde son elemanı alır
print("Çıkarılmış : ",gun)
print("")
print("-	-	-	Listeden yığın (stack) oluşturma	-	-	-\n")

#				listeden kuyruk (queue) oluşturma

# elelman ekleme işlemini listenin sonundan eleman çıkarma işlemini listenin başından yapar

gun.append(7) # en sona eleman ekledik
print("append : ",gun)
gun.pop(0) # en baştan eleman çıkardık eleman sayısı hala aynı ve bu şekilde kuyruk oluşuyor
print("pop : ",gun)
# bir restoran onundeki kuyruk gibi duşunebiliriz restoran kuyrukta her bir kişi arttığında içeri bir kişi alıyor ve kuyruk bir azalıyor
print("------------------------------------")
print("Memo kliniğe hoşgeldiniz")
print("Sıradaki hastayı öğrenmek için 'n' yi sistemden çıkmak için 'q' tuşlayınız")
print("")
while True:
	tc = input("Tc' nizin son 3 rakamını giriniz : ")

	if tc == 'n':
		print("Sıradaki hasta: ",string.pop(0))
	elif tc == 'q':
		break
	elif len(tc) != 3:
		print("Lutfen 3 hane olacak şekilde tuşlayın")
	elif tc in string:
		print(f"{string.index(tc) + 1}. Sıradasınız.")

	else:
		string.append(tc)
		print("Sırada bekleyen hastalar : ",string)

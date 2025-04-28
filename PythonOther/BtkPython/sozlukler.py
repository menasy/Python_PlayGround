# -*- coding: utf-8 -*-
#							Dictionary
# anahtar ve değerden oluşur
# ilk yazılan anahtar ikinci yazılan değerdir
print("\n\n-	-	-	Dictionary tanımlama	-	-	-\n\n")
mevsim = {"ilkbahar" : 1, "yaz" : 2, "sonbahar":3, "kış" : 4}
# burda anahtarımız stringler değerlerimiz ise 1 2 3 ve 4 tur
# anahtarlar benzersiz olmalıdır iki tane yaz mevsimi olamaz.
print("mevsim : ",mevsim)
okulno = dict([("memo",473),("eto",31),("musti",73)])
print("okul no : ",okulno)
s = {} # burda anahtarlar stringler değerler ise sayılardır
s['bir'] = "Fenerbahce"
s["iki"] = 2
s["uc"] = 3
s["uc"] = 5 # burda anahtarımı var olan bir anahtara eşitlediğim için onceki değer kaybolur artık buna eşitlenir
print("s sozluğu : ",s)
#print(mevsim["kış"])
# print(mevsim[4]) bu kullanım hatalıdır çunku 4 bir değerdir. key in yazılması lazım

print("\n\n-	-	-	Kullanılacak fonksiyonlar	-	-	-\n\n")

#	get(key,olmaması durumunda gosterilecek mesaj) fonksiyonu

print("s[bir] = ",s.get("bir","Bulunamadı"))
print("s[iki] = ",s.get("iki","Bulunamadı"))
print("s[olmayan key] = ",s.get("none","Bulunamadı"))

#	keys(none) fonksiyonu

# sozcuğun anahtarlarını verir
print("Keys : ",s.keys())

#	values(none) fonksiyonu
# sozcuğun değerlerini verir
print("values : ",s.values())

#	items(none) fonksiyonu
# sozcuğun dict() fonksiyonuyla oluşturulmuş halini verir.
print("items : ",s.items())

#						kume/set veri tipi

print("\n\n-	-	-	küme/set	-	-	-\n\n")
# küme oluşturuyoruz aynı mattaki gibi
k = {1,"FB",53,"memo"}
print("k kumesi : ",k)# rastgele olarak yazdı sıralama yok cunku her biri de bi eleman
k = set("TADİC")
print("veri tipi : ",type(k))
print("k set kumesi : ",k) # rastgele olarak yazdı sıralama yok cunku her biri de bi eleman
k1 ={1, 3, 5, 7, 2}
k2 = {5,6,8,2,2,7}
print("Birleşim : ",k1 | k2)	# '|' birleşim işareti
print("Kesişim : ",k1 & k2)		# '&' Kesişim işareti
print("fark : ",k1 - k2)		# '-' fark işareti. k1 de olup da k2 de olmayan
print("fark 2 : ",k2 - k1)		# '-' fark işareti. k2 de olup da k1 de olmayan

#					Touple/Demet veri tipi

print("\n\n-	-	-	Tuple/Demet	-	-	-\n\n")

# listelerle hemen hemen aynıdır.
# Tuple () ile tanımlanır ve Touple değiştirilemezdir.
# Tuple listeye gore hafıza da daha az yer kaplar
# değiştirilemez oldukları için sozluklerde key olarak kullanılabilirler

liste = ["memo",73,"nasim"]
top = ("memo",73,"nasim")
print("Liste : ",liste)
print("Tuple : ",top)
liste[1] = 47
# top [1] = 47 boyle bir kullanım yok touple değiştirilemez olduğu için hata verir
print("New liste : ",liste)	#değişti
print("New Top : ",top)		#değişmedi

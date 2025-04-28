# -*- coding: utf-8 -*-

print("\n\n-	-	-	Veri Tipleri Özet	-	-	-\n\n")

a = 3							# integar (int)
b = 3.14						# float
c = "abc"						# string (str)
d = [1,2,'memo',3]				# Liste (list)
e = {"bir":1,"iki":2,"uc":3}	# Sözlük (dict)
f = {"memo",1,2,"uc"}			#Küme (set)
g = ("memo",1,2,"uc")			#Demet (tuple)
print(type(a),type(b),type(c),type(d),type(e),type(f))

print("\n\n-	-	-	Sınıf Tanımlama	-	-	-\n\n")
# self, class içersindeki  elemanlara erişmek için kullanılır.
# nesneyi belirtmek için kullanılır
class ogr:
	pass		# pass komutu es geçmek için kullanılır sonradan kullanmak için

# class araba (model):
# 	marka = model
# 	def metot(self):
# 		self.model = "Tofas"

# class hayvan (cins):
# 	tur = cins
# 	def hetot(self):
# 		self.cins = "Balıklar"

mehmet = ogr() # Nesne tanımlama mehmeti tanımladık oğrenci kısmına
# init başlangiç
class araba (): # bir fonksiyon class ın altında tanımlanırsa o metot olur artık
	def __init__(self,model,marka,renk): # self bir parametre değil. işaretçi, ona dışardan değer gonderilmez
		self.model = model
		self.marka = marka
		self.renk = renk
	def aracbilgisi(self): # self her zaman yazılmalı bu kısmı sonradan ekledik
		print("Marka = ",self.marka)
		print("model = ",self.model)
		print("renk = ",self.renk)

taksi = araba(2020,"fiat","yeşil")
print("Taksi modeli : ",taksi.model)
print("Taksi rengi : ",taksi.renk)
taksi.model = 2022
print("Taksi modeli update : ",taksi.model)

print("\nclass içindeki 2. fonksiyon\n")
kamyon = araba(2005,"ford","kırmızı")
kamyon.aracbilgisi()

print("Type : ",type(kamyon)) # clas ile kendi veri tipimizi oluşturduk bir nevi

# Sınıf metodları/fonksiyonları ile normal fonksiyonlar hemen hemen aynıdır
# farkı fonksiyon içindeki self değeri ile fonksiyonun çağrılma şeklidir kamyon.arababilgisi gibi

#					__init__  metodu
# sınıf tanımlarken sınıfın başlangıç değerlerini tanımlarken __init__ kullanılmalı
# init ten sonra da mutlaka self gelmeli
# init ile tanımlanan fonksiyonda return değeri kullanılmaz

#					dir() fonksiyonu

# clasımızda kullandığımız metotları listeler

print("Metotlar : ",dir(kamyon)) # başında ve sonunda '__' olanlar pythonun kendi gomulu metotları
								 # başında onlar olmayanlar ise bizim oluşturduğumuz metotlar


#					kalıtım (sınıf içinde sınıf oluşturma)
print("\n\n-	-	-	Kalıtım/miras	-	-	-\n\n")

# ust sınıfa ait olan ozellikler alt sınıflarda da kullanılabilir
import	datetime
class ogrenci:
	def __init__(self,isim,soyisim):
		self.isim = isim
		self.soyisim = soyisim
	def ogrencibilgi(self):	#105. satırdan sonra burayı ekldeim ve import datetime yaptım
		print("isim : ",self.isim)
		print("soyisim : ",self.soyisim)
		return(datetime.datetime.now())

class altogrenci (ogrenci): # ogrenci değerini parametre olarak girerel bir subclass/alt sınıf oluşturduk
	pass				#boylelikle altogrenci classını kullanarak ust sınıf ozelliklerini de kullanabiliriz

ogr1 = altogrenci("eto","kose")
print("İsim : ",ogr1.isim)
print("soyisim : ",ogr1.soyisim)

class subogrenci(ogrenci):
	def __init__(self,isim,soyisim,numara):
		ogrenci.__init__(self,isim,soyisim) #self.isim = isim
		self.numara = numara			#self.soyisim = soyisim

# 88. satırda sağda yorum satırında yazdığım gibi tek tek bir daha tanımlamak yerine
# bir onceki ana classımı oluşturdğum bu yeni subclasımda tanımladım ve ordaki değerleri kullanabildim

print("\nOgrenci 2\n")
ogr2 = subogrenci("furkan","yılmaz",73)
print("isim : ",ogr2.isim)
print("Soyisim : ",ogr2.soyisim)
print("Numara : ",ogr2.numara)

# clasımıza bir tane daha sınıf ekleyeceğiz yukarıya çıkıp
print("\nogrencibilgi fonksiyonu\n")
print(ogr2.ogrencibilgi()) # printsiz de yazdırır fakat return değerini vermez.

#						modul kavramı
print("\n\n-	-	-	modul kavramı	-	-	-\n\n")

# c deki kutuphane mantığı gibi başka bir dosyadaki veriyi kullanmak için o veriyi import etmemiz gerek

# 1
# import ft
# boyle tanımladığımda fonksiyon isimli dosyamdaki tum parametreleri çekiyorum
# ve orneğin bu dosyamdaki bir parametreyi kullanacağim zaman da ft.ustel() şeklinde bir tanımlama yapmak zorundayım

# 2
# from ft import ustel
# boyle tanımladığımda ft den ustel fonksiyonunu tanımla diyorum
# bu tanımlamada ft dosyasındaki ustel fonksiyonunu kullanabilirim sadece diğerleri tanımlanmaz
# kullanırken de dosyanın isminin yazılmasına gerek kalmaz direkt ustel() yazılabilir

# 3
from ft import *
# bu kullanımda ise dosya yani modul içindeki tum fonksiyonları import etmiş oluruz
# ve kullanımda modul ismini girmemize gerek kalmaz yine ustel() şeklinde kullanılabilir
print("Ustel : ",ustel(2,5))

# 4 import ft, fonksiyon
# şeklinde iki modulu ya da daha fazlasını import edebiliriz

# 5
#import ft as f
# bu tanımlama da ise uzun isimli bir modulun ismini kısaltamak için yapabiliriz
# ft.ustel() yerine f.ustel() şeklinde tanımlanabilir. as = gibi anlamında ft yi f ye donuşturur

# import kullanım şekillerini hafızada daha az yer kaplamak için en uygun şekilde kullanmalıyız
#						__name__
print("\n\n-	-	-	__name__	-	-	-\n\n")
# ana program olup oladığını kontrol eder. ana programsa true değilse folse doner
# ft yi çalıştırdığımda bana true doner çunku bir yerden import edilmedi ana program çunku
# sinif ı çalıştırdığımda ise ft nin name kontrol değeri folse olur çunku o artık ana program değil
# sinif içersinde kullandığım bir modul oluyor bu yuzden folse değeri dondur

print("Name kontrolu Sınıf : ",__name__ == '__main__')

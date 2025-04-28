# -*- coding: utf-8 -*-

#				fonksiyon

def selamlama(isim):
	print(f"Restoranımıza hoşgeldiniz {isim} ")
selamlama(input(("isminiz nedir : ")))
def selam(isim = "Mehmet"): #eğer dışardan veri girilmezse varsayılan olarak mehmeti alır
	print(f"Restoranımıza hoşgeldiniz {isim} ")
selam()
print("-	-	void fonksiyon -	-	-\n")
# Return değeri olan fonksiyon
def	cevre(uz,gen):
	cev = (uz + gen)*2
	return cev
def	alan (uz,gen):
	al = uz*gen
	return al

uz = int(input("Digdortgenin uzun kenarını giriniz : "))
gen = int(input("Dikdortgenin genişliği giriniz : "))
print(f"Cevre : {cevre (uz,gen)}")
print(f"Alan : {alan(uz,gen)}")
print("-	-	returnlu fonksiyon -	-	-\n")

# global local kavramı

def	topla():
	a = 5
	b = 6
	return (a+b)
print("toplam : ",topla())
#print(a) # a local değişken olduğu için burda çağıramadık

def	cikar():
	global x
	global y
	x = 5
	y = 6
	return (x-y)
print("cıkarma : ",cikar())
print("global değişken : ",x) # x ve y global olarak tanımlandığı için bunu diğer fonksiyonlarda da kullanabilirim

def	carpma():
	return(x*y)
def	bolme():
	pass	#pass yaptığımızda pas gec diyoruz bunun için bir hata verme diyorsun

print("carpma : ",carpma())
print("Bolme : ",bolme())
print("-	-	Global/Local Değişken -	-	-\n")

# fonksiyon kısaltma Lambda
# tek satırlık bir fonksiyon yazacaksak kullanabiliriz

def	dolar(tl):
	return(tl/28)
euro = lambda TL: TL/30  # bu ile yukardaki aynı işlevi goruyor tek satırda fonksiyon
#fonk adı -> lambda -> parametre -> işlem
print("Dolar : ",dolar(100))
print("Euro : ",euro(100))
print("-	-	Lambda -	-	-\n")

# özyinelemeli fonksiyon (recursive fonksiyon)

def ustel(a,b):
	if b == 0:
		return 1
	else:
		return a*ustel(a,b-1) # 2
print("ustel : ",ustel(2,5))

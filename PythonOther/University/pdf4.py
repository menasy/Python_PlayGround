
from math import log

def log_ret(P0,P1):
	ret = log(P1/P0)*100
	ret = round(ret,2)
	return ret
print("Log_ret : ",log_ret(27,31))

hisseportfoy = { 'hisseadi': ['doas','kocaer','THYAO','IEHYO'],
				'fiyat': [[338.54,160.03],[170.40,108.92],[181.26,136.53],[597.37,174.87],[145.07,109.37]],
				'tarih':['01-03-2022','06-30-2022']}

for i,j in zip(hisseportfoy['hisseadi'], hisseportfoy['fiyat']):
	print(f"{i} hisse senedinin getirisi = {round(log(j[0],j[1]),2)}")

# dog.py
class Dog:
	species = "Canis familiaris"
	def __init__(self, name, age):
		self.name = name
		self.age = age

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)

print("age : ",miles.name,miles.age)
print(buddy.name,buddy.age)
print(miles.species)
print(buddy.species)
# vars ile değişkenin tamamen ne tuttuğunu goruntuleyebiliriz
print("vars : ",vars(miles))

buddy.name = "kangal" # değeri boyle de değiştirebiliriz
print("yeni ad : ",buddy.name)

#__str__() işlevi, sınıf nesnesi bir dize olarak temsil edildiğinde neyin çıktı olarak verilmesi gerektiğini kontrol eder.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return ('Kişi ismi {} ve yaşı {} dir.'.format(self.name,self.age))

p1 = Person("John", 36)
print(p1) # normalde p1.name falan diye yazdırırız ama __str__ yi kullandığımız için bir return değeri girdik
# ve p1.name diye tanımlamaya gerek kalmadan __str__ içindeki değeri printle direkt yazdırdı

print("dict version : ", miles.__dict__) # dict tum değerleri gormemize yarar
print("dict item version  : ", miles.__dict__.items()) # bu da farklı bir formatta veriyor çıktıyı değerler ayrı bir parante de keyler ayrı bir parantezde
print(dir(miles)) # dir komutu ise tanımlı methodlarımızı gosterir __*__ başında ve sonunda bunlar olmayanlar bizim tanımladıklarımız olanlr ise sistem varsayılanı

class kişi:
	def __init__ (self,isim,soy_isim):
		self.isim = isim
		self.soy_isim = soy_isim
	def print_isim_soy_isim(self):
		print(self.isim,self.soy_isim)

x = kişi("Ali", "Veli")
x.print_isim_soy_isim()
class öğrenci (kişi):
	def __init__ (self,isim,soy_isim):
		super().__init__(isim,soy_isim)
		self.soy_isim = self.soy_isim.upper()

y = öğrenci("Ali", "Veli")
y.print_isim_soy_isim()

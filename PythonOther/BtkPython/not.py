# python da değişken adı rakamla, nokta işareti başlayamaz.
# keywordlar da değişken olarak kullanılmaz
# python turkce kabul etse de kullanmamak daha iyi.
# buyuk harf ile kucuk harf ayrımı vardır python da A ve a ayrı birer değişkendir
# değişken ismi içersinde '_' den başka bir karakter olamaz sonunda başında her yerde '_' olabilir,

##tanımlamayı direkt olarak boyle de atayabiliriz satir 5
a, b = b,a
print(a,b)

#işlem onceliği
#parantez içi () -> us alma ** -> çarpma * -> bolme / -> mod % -> toplama + -> çıkarma -
#BOLLEAN veri tipi true ya da folse tutar
c = (4>3)

#bir değişkenin tipipni oğrenmek için type() fonksiyonu kullanılır
type (a)

#veri donuşumleri:
x = 53.5
x = 53.5
print("Float x:",x)
print(type(x))

x = (int)(x) # inte cevirdik
print("Int x: ",x)
print(type(x))
print('int x toplami : ', x+x) # x integer deger oldugu icin toplama islemi oldu

x = (str)(x) # stringe cevirdik
print(type(x))
print('str x toplami : ',x + x) # x leri yan yana yazdi toplama yapmadi str oldugu icin

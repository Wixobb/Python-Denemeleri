x = int(1)
y = int(2.8)
z = int("3")
#int sadece başındaki sayıyı yazar. Yukarısı 1,2,3

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
#float noktalı şekilde yazar. Yukarısı 1.0, 2.8, 3.0, 4.2

x = str("sad3")
y = str(2)
z = str(3.0)
#string ne varsa yazar.

a = "Hello, World!"
print(a.replace("H", "J"))
#replace yer değiştirir. Yukarısı "Jello World" olur.

thislist = ["apple", "banana", "cherry"]
print(thislist[2])
#thislist liste yapar. 2 yazan yere ne gelirse oradaki kelimeyi printler.

thislist = ["apple", "banana", "cherry", "annen"]
print(len(thislist))

cars = ["Ford", "Volvo", "BMW", "Pejo"]

x = len(cars)

print(x)
#len listedeki eleman sayısını söyler. İkiside print=4. İki farklı len kullanımı(Aşağıdaki array)

thislist = ["apple", "banana", "cherry"]

thislist.append("orange")
#append listeye orange ekler ve öyle printler.pop listeden bir şeyi kaldırır.(thislist.pop(1))

thisset = {"apple", "banana", "cherry"}

print("annen" in thisset)
#in Eğer yazdığım şey listedeyse True print, listede yoksa False print.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#sözlük Print denince "{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}"

a = 33
b = 32
if b < a :
    print("a is greater than b") #Öğrendiğim ilk komut bu olabilir.
elif a == b :
    print("a and b are equal") 
else:
    print("b is greater than a") #Eğer b büyükse ilki, eşitlerse ikincisi, hiçbiri değilse sonuncusu printlenir.

a = 2
b = 330

print("A") if a > b else print("B") #a b'den büyükse A printler değilse B printler.

a = 200
b = 33
c = 500
if a > b or a > c:
  print("Biri doğru") #or herhangi biri doğruysa "Biri doğru" printler.


i = 1
while i < 6:
  print(i)
  i = i+1
#while i=1 olarak başlıyor ve 6'dan küçük olduğu sürece i'ye 1 ekleyip devam ediyor.

a,b = 1,1
while a < 22:
   print(a)
   a,b=b, a+b #fibonacci sayılarını böyle bulursun.

#break döngüyü kırar.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) #continue devam ettirir veya atlar. 

#range sıralama yapar.Printten sonra else yazarak döngü bittiğinde mesaj konulabilir.
for x in range(6):
    print(x) #Burada print = (0,1,2,3,4,5)


for x in range(2, 30 ,3):
  print(x) #Burada 2'den 30'a 3'er atlayarak gider. (2,5,8,11,14...)


def f(x):
    return x+10
print(f(8)) #Fonksiyonlar: x'e 8 değerini verdi ve cevabı 18 bulup return sayesinde 18 printledi."def" fonksiyon tanımlar.


def fib(n):
  a,b =0,1
  while a<n:
    print(a)
    a,b=b,a+b
fib(20) #Fonksiyon kullanarak fibonacci sayıları böyle bulunur.


def fact(n):
    a=1
    sonuc=1
    while (a <= n):
        sonuc = sonuc * a
        a = a + 1
    return sonuc
print(fact(5)) #Faktöriyel böyle hesaplanır.

def facto(n):
  if (n==0):
    return 1
  return n*facto(n-1)
print(facto(5)) #Böyle de hesaplanır.


import json

# Bunlar JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse ayrıştırmak demekmiş.
y = json.loads(x)

print(y["age"]) #Burada JSON to Python. Tam tersi için "loads" yerinde "dumps" yazmalı.


#regex arama için kullanılır.
import re
#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")



canimList = ["Ben", "Anam", "Babam", "Eben", "Anam"]
print(canimList)
#canımList.clear()
#print(canımList) #Önce tüm listeyi basar sonra hepsini silip boş basar.


canimListYeni = canimList.copy()
print(canimListYeni) #yeni liste oluşturup eskisinden kopyalar.

print(len(canimList)) #Kaç elemanlı olduğunu söyler.

print(canimList.count("Anam")) #Sorduğun ifadenin kaç kez tekrar ettiğini söyler.

canimList.append("ble") #listeye yazdığın şeyi ekler.
print(canimList)

canimList.insert(2, "asdf") #yazdığın şeyi yazdığın sıraya ekler.
print(canimList)

canimlist2 = ["123", "qwer"] 
canimList.extend(canimlist2) #diğer listedekileri istediğin listeye ekler.
print(canimList)

#del ve pop siler, pop sildiğin şeyi başka bir listeye ekleyebilirsin, remove yazdığın şeyi siler.

canimList.sort() #harflere göre sıralar.

canimList.reverse() #tam ters sıralar.
print(canimList)


#String komutu ile şöyle şeyler yaparsın: https://prnt.sc/_K8wN7QOTjGK ilk harf 0, son harf -1 olarak nitelenir.

String1 = "GeeksForGeeks"
 
# İlk karakteri yazar
print("\nFirst character of String is: ")
print(String1[0])
 
# Son karakteri yazar
print("\nLast character of String is: ")
print(String1[-1])

#String dilimleme de var

String1 = "Anan"
print("\nSlicing characters from 3-12: ")
print(String1[3:12])


#Sayılarla oynarken "format" kullanarak yuvarlama falan yaparsın

String1 = "{0:b}".format(16) #16'nın binary gösterimi
print("\nBinary representation of 16 is ")
print(String1)
 
String1 = "{0:e}".format(165.6458) #bunun üssel gösterimi
print("\nExponent representation of 165.6458 is ")
print(String1)
 
String1 = "{0:.2f}".format(1/6) #noktalı gösterim
print("\none-sixth is : ")
print(String1)


#try ve except, kullanıcı malca bişey yaptığında kafasına pythonca uyarı yemesin de benim yazdığım uyarıyı yesin.

ilk_sayı    = input("ilk sayı: ")
ikinci_sayi = input("ikinci sayı: ")

try:
    sayi1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayi)
    print(sayi1, "/", sayı2, "=", sayi1 / sayı2)
except ValueError:
    print("Lütfen sadece sayı girin!")  #finally bloğu da eklersen, hata olsa da olmasa da mutlaka o işlemi yapar


#raise; hata mesajı ile birlikte senin göstermek istediğin mesajı da printler.
x = 2

if x < 0:
  raise Exception("Sorry, no numbers below zero")
else:
  print("aferin 0'dan büyük sayı girdin.")


#split; karakter dizilerini belli noktalardan böler
kardiz = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin: ")

for x in kardiz.split():
    print(x[0], end="") #istanbul büyükşehir belediyesi girersen sana ibb printler











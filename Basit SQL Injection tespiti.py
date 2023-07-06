import requests

url = input("Web site URL'sini giriniz: ")
response = requests.get(url + "'") # URL'nin sonuna tek tırnak ekleyerek istek gönderiyoruz, Blind SQL Injection varsa error dönmez aklınızda bulunsun.

if "error" in response.text.lower(): # Yanıt metninde "error" kelimesi varsa
    print("Bu web sitesinde SQL Injection var !")
else:
    print("Bu web sitesinde SQL Injection bulunamadi.")

#SQL Injection ile ilgili güzel bir yazı : https://yakupseker.medium.com/sql-injection-nedir-nas%C4%B1l-bulunur-mutillidea-sql-injection-cevaplar%C4%B1-level-low-c6eff4e1e09
#Üstat olarak gördüğüm insanlar arasında yer alan Mehmet "MDISEC" İnce'den SQL Injection : https://www.youtube.com/watch?v=WtHnT73NaaQ&t=3s&pp=ygULbWRpc2VjIHNxbCA%3D 
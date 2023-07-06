import requests
import socket
import whois

url = input("Web sitesinin URL'sini giriniz: ") # Kullanıcıdan web sitesinin URL'sini al
ip = socket.gethostbyname(url) # Web sitesinin IP adresini al
domain = whois.query(url) # Web sitesinin domain bilgilerini al

with open("web_site_info.txt", "w") as file: # Yazma modunda bir TXT dosyası aç
    file.write(f"Web site URL: {url}\n") # Dosyaya web site URL'sini yaz
    file.write(f"IP address: {ip}\n") # Dosyaya IP adresini yaz
    file.write(f"Domain name: {domain.name}\n") # Dosyaya domain adını yaz
    file.write(f"Creation date: {domain.creation_date}\n") # Dosyaya oluşturulma tarihini yaz
    file.write(f"Expiration date: {domain.expiration_date}\n") # Dosyaya bitiş tarihini yaz
    file.write(f"Registrar: {domain.registrar}\n") # Dosyaya kayıt eden kurumu yaz
    file.write(f"Name servers: {', '.join(domain.name_servers)}\n") # Dosyaya isim sunucularını yaz

print("Web sitesinin IP adresi ve domain bilgileri web_site_info.txt dosyasına kaydedildi.") # Ekrana mesaj yaz
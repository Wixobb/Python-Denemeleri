import requests
from bs4 import BeautifulSoup
import os

def download_video(url):
    # url alıyoruz.
    response = requests.get(url)
    html = response.text
    # HTML ayrıştırıyoruz
    soup = BeautifulSoup(html, "html.parser")
    # Video başlığını alıyoruz.
    title = soup.find("meta", property="og:title")["content"]
    # Videonun url'sini buluyor.
    video_url = soup.find("meta", property="og:video:url")["content"]
    # Video dosyayı çağırıyoruz.
    response = requests.get(video_url, stream=True)
    # Masaüstü yolunu alıyor.
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    # Videoya tam path oluştur.
    file_path = os.path.join(desktop_path, title + ".mp4")
    with open(file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f"Video {title} indirme işlemi başarıyla tamamlandı.")

while True: # sonsuz döngüye soktum ki arka arkaya video indirmek için tekrar tekrar çalıştırmanıza gerek olmasın.
    link = input("Videonun URL'sini giriniz: ")
    download_video(link)
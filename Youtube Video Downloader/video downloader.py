from pytube import YouTube
import os

def video_downloader(video_url):
    my_video = YouTube(video_url)
    my_video.streams.filter(res=resolution).first().download() # şurayı yazana kadar alnımdan sular aktı
    return my_video.title

# masaüstüne kayıt
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# sonsuz döngü
while True:
    try:
        # userdan url alma
        video_url = input('URL giriniz:')
        if not video_url:
            break
        resolution = input("Çözünürlük giriniz: ")
        # çözünürlük ayarı
        if not resolution:
            resolution = "Çözünürlüğünüz"
        print(f'Video İndiriliyor....')
        video = video_downloader(video_url)
        print(f'"{video}" videosu indirildi!')
    # hata mesajı
    except Exception as e:
        print(f'Video indirilemedi\nSebepleri şunlar olabilir\n->İnternet bağlantısı yok.\n->Kaldırılmış video\n{e}')

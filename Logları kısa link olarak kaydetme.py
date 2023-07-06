import os
import requests

# Dosya adı ve yolu
FILE_NAME = "ipler.txt"
FILE_PATH = os.path.join(os.getcwd(), FILE_NAME)

# Link dosyasının adı ve açma modu.
LINK_FILE = "link_log.txt"
LINK_MODE = "a"

# Link oluşturma sitesinin URL'si
UPLOAD_URL = "https://file.io"

# IP'lerin olduğu dosyayı siteye yükleyip linki aldık. 
def upload_file():
    files = {"file": open(FILE_PATH, "rb")}
    response = requests.post(UPLOAD_URL, files=files)
    data = response.json()
    if data["success"]:
        link = data["link"]
        return link
    else:
        return None

# Linki başka bir dosyaya kaydedin
def save_link(link):
    with open(LINK_FILE, LINK_MODE) as f:
        f.write(f"{link}\n")

#Bunu otomasyona dökmek isterseniz; bu yorum satırını silip basit bir while(True) döngüsü eklerseniz kodu çalışır bırakıp belirli aralıklar (import time) ile siteden linkleri alabilirsiniz. 
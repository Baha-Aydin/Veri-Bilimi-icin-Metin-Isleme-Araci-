import subprocess
import sys
import os
import time



def update_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("pip başarıyla güncellendi.")
        time.sleep(3)
    except subprocess.CalledProcessError as e:
        print(f"pip güncellenirken bir hata oluştu: {e}")
        time.sleep(3)
        sys.exit(1)

def install_packages():
    packages = [
        'json',
        'random',
        'scikit-learn'
    ]

    def install(package):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} başarıyla yüklendi.")
            time.sleep(3)
        except subprocess.CalledProcessError as e:
            print(f"{package} yüklenirken bir hata oluştu: {e}")
            time.sleep(3)
            sys.exit(1)

    for package in packages:
        install(package)

if __name__ == "__main__":
        update_pip()              # pip güncelle
        install_packages()       # Paketleri yükle

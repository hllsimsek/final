from datetime import datetime
from veri_kaynagi import bilgileri_yukle
import yaml

def yas_hesaplama():
    print("Yas Hesaplama Uygulamasi")
    satirlar = bilgileri_yukle()  # Bilgiler veri_kaynagi.py'den geliyor

    if not satirlar:
        print("İslenecek veri bulunamadi!")
        return

    mevcut_yil = datetime.now().year

    try:
        with open("cikti.txt", "w") as cikti_dosya:
            for satir in satirlar:
                ad, dogum_yili = satir.strip().split(",")  # Ad ve doğum yılı ayrıştırılır
                yas = mevcut_yil - int(dogum_yili)
                sonuc = f"{ad} su an {yas} yasinda."
                print(sonuc)  # Konsola yazdır
                cikti_dosya.write(sonuc + "\n")  # Dosyaya yazdır
    except Exception as e:
        print(f"Bir hata olustu: {e}")

def yaml_dosyasina_yaz():
    # cikti.txt dosyasını açıp içeriğini oku
    try:
        with open('cikti.txt', 'r') as file:
            cikti_verileri = file.readlines()

        # Veriyi işleyip bir listeye dönüştürme
        cikti_listesi = [satir.strip() for satir in cikti_verileri]

        # YAML dosyasına yazma işlemi
        yaml_veri = {'cikti': cikti_listesi}

        # YAML dosyasına yazma
        with open('output.yml', 'w') as yaml_file:
            yaml.dump(yaml_veri, yaml_file, default_flow_style=False)

        print("YAML dosyasına yazıldı.")
    except Exception as e:
        print(f"YAML yazma hatası: {e}")

# Yas hesaplama işlemi
yas_hesaplama()

# YAML dosyasına yazma işlemi
yaml_dosyasina_yaz()

from datetime import datetime
from veri_kaynagi import bilgileri_yukle


def yas_hesaplama():
    print("Yaş Hesaplama Uygulaması")
    satirlar = bilgileri_yukle()  # Bilgiler veri_kaynagi.py'den geliyor

    if not satirlar:
        print("İşlenecek veri bulunamadı!")
        return

    mevcut_yil = datetime.now().year

    try:
        with open("cikti.txt", "w") as cikti_dosya:
            for satir in satirlar:
                ad, dogum_yili = satir.strip().split(",")  # Ad ve doğum yılı ayrıştırılır
                yas = mevcut_yil - int(dogum_yili)
                sonuc = f"{ad} şu an {yas} yaşında."
                print(sonuc)  # Konsola yazdır
                cikti_dosya.write(sonuc + "\n")  # Dosyaya yazdır
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


# Uygulamayı çalıştır
yas_hesaplama()


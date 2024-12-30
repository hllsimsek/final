from datetime import datetime
from veri_kaynagi import bilgileri_yukle


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
                dogum_yili = int(dogum_yili)
                if dogum_yili > mevcut_yil:
                    sonuc = f"{ad} icin gecersiz dogum yili: {dogum_yili}. Yas hesaplanamadi."
                    print(sonuc)  # Geçersiz yaş mesajını konsola yazdır
                    cikti_dosya.write(sonuc + "\n")  # Geçersiz yaş mesajını dosyaya yazdır
                else:
                    yas = mevcut_yil - dogum_yili
                    sonuc = f"{ad} su an {yas} yasinda."
                    print(sonuc)  # Konsola yazdır
                    cikti_dosya.write(sonuc + "\n")  # Dosyaya yazdır
    except Exception as e:
        print(f"Bir hata olustu: {e}")


# Uygulamayı çalıştır
yas_hesaplama()

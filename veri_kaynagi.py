def bilgileri_yukle(dosya_adi="bilgiler.txt"):
    try:
        with open(dosya_adi, "r") as dosya:
            return dosya.readlines()
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyasi bulunamadi!")
        return []
    except Exception as e:
        print(f"Bir hata olustu: {e}")
        return []

from datetime import datetime
class FileHandler:
    @staticmethod
    def analiz_icin_dosya_oku(dosya_adi):
        try:
            with open(dosya_adi, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Hata: {dosya_adi} dosyası bulunamadı!")
            return None

    @staticmethod
    def raporu_kaydet(icerik, kaynak_dosya):
        zaman= datetime.now().strftime("%Y%m%d_%H%M")
        dosya_ismi = kaynak_dosya.split('.')[0]

        yeni_dosya_adi = f"rapor_{dosya_ismi}_{zaman}.md"

        with open(yeni_dosya_adi,"w", encoding="utf-8") as f:
            f.write(str(icerik))
        print(f"\n✅ Rapor '{yeni_dosya_adi}' adıyla kaydedildi.")

       
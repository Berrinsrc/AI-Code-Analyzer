from crewai import Crew
from utils.path_reader import FileHandler
from agents.manager import AnalysisManager


def kod_analiz_servisi(analiz_edilecek_metin):
    if not analiz_edilecek_metin:
        return "Analiz edilecek metin bulunamadı"
    
    manager = AnalysisManager(analiz_edilecek_metin)
    analiz_ajani, editor_ajani = manager.ajanlari_olustur()
    analiz_gorevi, editor_gorevi = manager.gorevleri_olustur(analiz_ajani, editor_ajani)

    
    ekip = Crew(
        agents=[analiz_ajani, editor_ajani],
        tasks=[analiz_gorevi, editor_gorevi],
        verbose=True
    )
    
    
    rapor_sonucu = ekip.kickoff()
    return rapor_sonucu


def main():
    hedef_dosya = "analiz_edilecek.py"
    
    
    kod_icerigi = FileHandler.analiz_icin_dosya_oku(hedef_dosya)

    if kod_icerigi:
        print("--- Analiz Başlıyor, Lütfen Bekleyin ---")
        
        
        sonuc = kod_analiz_servisi(kod_icerigi)

        
        print("\n" + "*"*30 + "\nPERFORMANS ANALİZ RAPORU:\n" + "*"*30)
        print(sonuc)
        
        FileHandler.raporu_kaydet(sonuc, hedef_dosya)

if __name__ == "__main__":
    main()
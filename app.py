import streamlit as st
from main import kod_analiz_servisi

st.set_page_config(page_title="AI Code Analyzer", page_icon="🚀")

st.title("🚀 Yapay Zeka Destekli Kod Analizi")

st.write("Analiz etmek istediğiniz Python kodunu aşağıya yapıştırın veya dosya olarak yükleyin")

kod_girisi = st.text_area("Python kodunuzu buraya yapıştırın:", height=300, placeholder="def example(): ...")

yuklenen_dosya = st.file_uploader("Veya bir .py dosyası yükleyin", type=["py"])


if st.button("Analizi Başlat"):
    final_kod =""
    if yuklenen_dosya is not None:
        final_kod = yuklenen_dosya.read().decode("utf-8")
    elif kod_girisi:
        final_kod=kod_girisi

    if final_kod:
        with st.spinner("Ajanlar kodu inceliyor lütfen bekleyin..."):
            rapor= kod_analiz_servisi(final_kod)

            st.success("Analiz tamamlandı.")
            st.markdown("---")
            st.subheader("📊 Analiz Raporu")
            st.markdown(rapor)


    else:
        st.warning("Lütfen analiz yapılması için bir kod girin veya dosya yükleyin.")

################### KÜTÜPHANELER ###################
import yfinance as yf
import streamlit as st
from datetime import datetime
import datetime as d

################### SAYFA AYARLARI ###################
st.set_page_config(
  page_title = 'Hisse Senedi Uygulaması',
  page_icon = '✅',
  layout="wide")

################### SIDEBAR ###################
my_page = st.sidebar.radio('Sayfalar', ['Analiz', 'Haberler', 'Bilgiler', 'Öneriler'])

################### ANALİZ SAYFASI ###################
if my_page == 'Analiz':
    st.write(
        """
        ## Hisse Senedi Uygulaması

        Hisse senedinin kapanış fiyatını ve hacmini gösterir.
        """
    )

    stock = st.text_input('Hisse Adı', 'GOOGL')
    st.write('Şu anki hisse: ', stock.upper())

    tickerData = yf.Ticker(stock)

    start_date = st.date_input(
        "Başlangıç Tarihi",
        d.date(2019, 7, 6))
    st.write('Başlangıç Tarihi: {} olarak ayarlandı.'.format(start_date))

    tickerDf = tickerData.history(period="1d", start=start_date, end=datetime.date(datetime.now()))  # period max

    st.write("""
    ## Kapanış Fiyatı
    """)
    st.line_chart(tickerDf.Close)

    st.write("""
    ## Fiyat Hacmi
    """)
    st.line_chart(tickerDf.Volume)

################### HABERLER SAYFASI ###################
elif my_page == 'Haberler':
    stock = st.text_input('Hisse Adı', 'GOOGL')

    tickerData = yf.Ticker(stock)

    st.write("""
    ## Haberler
    """)
    news = tickerData.news #tickerData.newss -> Liste formatında

#    tickerData.news(değişkende verdiğimiz ismiyle news) içersinde kullanmayacağımız parametreler içeriyordu.
#    Aşağıda sadece kullanacağımız 3 bilgiyi çekiyoruz:
#    Haberi başlığı(title), Haberin kaynağı(publisher), Haberin Linki(link)

    # Get Title
    a_key = "title"
    values_of_title = [a_dict[a_key] for a_dict in news]
    # print(values_of_title) #test

    # Get Publisher
    a_key = "publisher"
    values_of_publisher = [a_dict[a_key] for a_dict in news]
    # print(values_of_publisher) #test

    # Get Link
    a_key = "link"
    values_of_link = [a_dict[a_key] for a_dict in news]
    # print(values_of_link) #test

    #Öncelikle haber ile haberin kaynağını zipliyoruz.
    #Elimizde birleşmiş halleriniz var. Liste formatına çevirip bir değişkene atıyoruz.
    
    #Daha sonra ikinci zip işlemize geçiyoruz.
    #Bu sefer ilk başta zipleyip bir değişkene atadığımız değer ile linki zipliyoruz.
    #Oluşan zipi yine liste formatına çevirip bir değişkene atıyoruz.

    zip1 = zip(values_of_title, values_of_publisher)
    content = (list(zip1))

    zip2 = zip(content, values_of_link)
    content2 = (list(zip2))

    st.write(content2)

################### BİLGİLER SAYFASI ###################
elif my_page == 'Bilgiler':
    stock = st.text_input('Hisse Adı', 'GOOGL')

    tickerData = yf.Ticker(stock)

    st.write("""
    ## Bilgiler
    """)

    info = tickerData.info
    for key, value in info.items():
        st.write(key, ":", value)

################### ÖNERİLER SAYFASI ###################
elif my_page == "Öneriler":
    stock = st.text_input('Hisse Adı', 'GOOGL')

    tickerData = yf.Ticker(stock)

    st.write("""
    ## Öneriler
    """)
    st.write(tickerData.recommendations)
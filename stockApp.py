################### LIBRARIES ###################
import yfinance as yf
import streamlit as st
from datetime import datetime
import datetime as d

################### PAGE SETTINGS ###################
st.set_page_config(
  page_title = 'Hisse Senedi Uygulaması',
  page_icon = '✅',
  layout="wide")

################### SIDEBAR ###################
my_page = st.sidebar.radio('Sayfalar', ['Analiz', 'Haberler', 'Bilgiler', 'Öneriler'])

################### ANALYSIS PAGE ###################
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

################### NEWS PAGE ###################
elif my_page == 'Haberler':
    stock = st.text_input('Hisse Adı', 'GOOGL')

    tickerData = yf.Ticker(stock)

    st.write("""
    ## Haberler
    """)
    news = tickerData.news #tickerData.newss -> list type


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
    

    zip1 = zip(values_of_title, values_of_publisher)
    content = (list(zip1))

    zip2 = zip(content, values_of_link)
    content2 = (list(zip2))

    st.write(content2)

################### INFORMATION PAGE ###################
elif my_page == 'Bilgiler':
    stock = st.text_input('Hisse Adı', 'GOOGL')

    tickerData = yf.Ticker(stock)

    st.write("""
    ## Bilgiler
    """)

    info = tickerData.info
    for key, value in info.items():
        st.write(key, ":", value)

################### SUGGESTION PAGE ###################
elif my_page == "Öneriler":
    stock = st.text_input('Hisse Adı', 'GOOGL')

    tickerData = yf.Ticker(stock)

    st.write("""
    ## Öneriler
    """)
    st.write(tickerData.recommendations)

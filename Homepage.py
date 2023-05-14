import yfinance as yf
import streamlit as st
import pandas
import numpy
import altair
from functions.css import local_css

st.set_page_config(page_title="Visualization of Big Company", page_icon=None, layout="wide")

# j'appel la fonction pour prendre un fichier css
# local_css("css/style.css")

#Header 
with st.container():
    st.header("Visualization of Big Company Data")
    st.write("Hello there :wave:,")
    st.write("""
        my name is **Jiek** and this page is to gives you some readable date of big companies :office:.
    """)
    st.write("Before you watch the informations yfinance is not affiliated, endorsed, or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes.")
    st.write("""
        The period I take is between 2019-5-06 and 2023-5-06 for all graphs.
    """)
st.markdown("#")

# with st.container():
#     appleHistory = tickers.tickers['AAPL'].history(period='1d', start='2019-5-06', end='2023-5-06')
#     metaHistory = tickers.tickers['META'].history(period='1d', start='2019-5-06', end='2023-5-06')
#     googleHistory = tickers.tickers['GOOG'].history(period='1d', start='2019-5-06', end='2023-5-06')

#     chart_data = pandas.DataFrame(
#         {
#             'date': appleHistory,
#             'apple': appleHistory.Volume,
#             'meta': metaHistory.Volume,
#             'google': googleHistory.Volume
#         }
#     )
#     st.write(chart_data)
#     chart = altair.Chart(chart_data).mark_line().encode(
#         x=altair.X('date:T'),
#         y=altair.Y('value:Q'),
#         color=altair.Color("name:N")
#     ).properties(title="company")
#     st.altair_chart(chart, use_container_width=True)

# dat = tickers.tickers['AAPL'].info['averageVolume']
# st.write(dat)
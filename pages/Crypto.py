import yfinance as yf
import streamlit as st
import pandas
import numpy
import altair
from functions.css import local_css

token = yf.Tickers('btc-eur eth-eur')

#bitcoin section 

with st.container():
    bitcoin = token.tickers['BTC-EUR'].history(period='1d', start='2020-01-01', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of bitcoin </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(bitcoin.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(bitcoin.Volume)

#etherium section 

with st.container():
    etherium = token.tickers['ETH-EUR'].history(period='1d', start='2020-01-01', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of etherium </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(etherium.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(etherium.Volume)

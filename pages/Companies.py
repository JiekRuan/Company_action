import yfinance as yf
import streamlit as st
import pandas
import numpy
import altair
from functions import local_css

# j'appel la fonction pour prendre un fichier css
local_css("css/style.css")

# get les differentes données sur les entreprises 
tickers = yf.Tickers('msft aapl goog amzn tsla meta nflx')

#sidebar

menu = st.sidebar.selectbox(
    "Choose the company you want to see the action :point_down:",
    ("Apple", "Microsoft", "Google", "Tesla", "Meta(Facebook)", "Amazon", "Netflix")
)

#apple section 

with st.container():
    appleHistory_per_day = tickers.tickers['AAPL'].history(period='1d', start='2019-5-06', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of Apple </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(appleHistory_per_day.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(appleHistory_per_day.Volume)

#microsoft section 

with st.container():
    msftHistory_per_day = tickers.tickers['MSFT'].history(period='1d', start='2019-5-06', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of Microsoft </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(msftHistory_per_day.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(msftHistory_per_day.Volume)

#google section 

with st.container():
    googleHistory_per_day = tickers.tickers['GOOG'].history(period='1d', start='2019-5-06', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of Google </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(googleHistory_per_day.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(googleHistory_per_day.Volume)

#Tesla section 

with st.container():
    teslaHistory_per_day = tickers.tickers['TSLA'].history(period='1d', start='2019-5-06', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of Tesla </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(teslaHistory_per_day.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(teslaHistory_per_day.Volume)

#meta section 

with st.container():
    metaHistory_per_day = tickers.tickers['META'].history(period='1d', start='2019-5-06', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of Meta(Facebook) </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(metaHistory_per_day.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(metaHistory_per_day.Volume)

#amazon section 

with st.container():
    amazonHistory_per_day = tickers.tickers['AMZN'].history(period='1d', start='2019-5-06', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of Amazon </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(amazonHistory_per_day.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(amazonHistory_per_day.Volume)

#netflix section 

with st.container():
    netflixHistory_per_day = tickers.tickers['NFLX'].history(period='1d', start='2019-5-06', end=None)
    title = """
                <h2 class="title"> Those graphs show the action of Netflix </h2>
             """    
    st.markdown(title, unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        subtitle = """
            <p class="subtitle"> The closing price per day </p>
        """
        st.markdown(subtitle, unsafe_allow_html=True)
        st.line_chart(netflixHistory_per_day.Close)
    with right_column:
        subtitle2 = """
            <p class="subtitle"> The total actions exchanges of the last negociation (Volume / duration) </p>
        """  
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.bar_chart(netflixHistory_per_day.Volume)

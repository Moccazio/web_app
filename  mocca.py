# ========================================
# Setup & Design
# ========================================
import os
import time
import numpy as np
from PIL import  Image
import streamlit as st 
import sqlite3
from sqlite3 import Error
# ========================================   
# Custom imports 
# ========================================   
from multipage import MultiPage
from pages import ticker, snp
# ========================================
# Main App
# ========================================
def main():
    
    app = MultiPage()

    display = Image.open('Logo.png')
    display = np.array(display)
    col1, col2 = st.beta_columns(2)
    col1.image(display, width = 300)
    col2.subheader("Mocca Application")
    
    app.add_page("Company Ticker", ticker.app)
    #app.add_page("S&P 500 Ticker", snp.app)

    app.run()
    app.sync()

if __name__ == '__main__':
    main()    
import streamlit as st
from image1 import main
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4
from page5 import page_5
#import pandas as pd
# st.write("Anime Favorit")
# df = pd.DataFrame({
#     'No' : [1,2,3,4,5],
#     'Judul' : ['Boku no Hero','Inuyasha','Jujutsu Kaisen','Kimetsu no Yaiba','Hunter x Hunter'],
#     'Rating' : [9,8.5,9.2,10,9]
# })

# df 
    
PAGES = {
    "Image Processing" : main,
    "Page 1" : page_1,
    "Page 2" : page_2,
    "Page 3" : page_3,
    "Page 4" : page_4,
    "Kalkulator Luas" : page_5
}

st.sidebar.image("nadiaalya.jpeg", width=200)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()
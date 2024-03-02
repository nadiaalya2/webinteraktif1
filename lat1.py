import streamlit as st
import pandas as pd
# st.write("Anime Favorit")
# df = pd.DataFrame({
#     'No' : [1,2,3,4,5],
#     'Judul' : ['Boku no Hero','Inuyasha','Jujutsu Kaisen','Kimetsu no Yaiba','Hunter x Hunter'],
#     'Rating' : [9,8.5,9.2,10,9]
# })

# df 

def page_1():
    st.title("Halaman 1")
    st.write("Halaman ini digunakan untuk Intro")
def page_2():
    st.title("Halaman 2")
    st.write("Halaman ini digunakan untuk Youtube")
def page_3():
    st.title("Halaman 3")
    st.write("Halaman ini digunakan untuk Rumus MTK")
    
PAGES = {
    "Page 1" : page_1,
    "Page 2" : page_3,
    "Page 3" : page_3
}

st.sidebar.image("nadiaalya.jpeg",width = 200)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()
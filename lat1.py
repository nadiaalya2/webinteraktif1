import streamlit as st
import pandas as pd
st.write("Anime Favorit")
df = pd.DataFrame({
    'No' : [1,2,3,4],
    'Judul' : ['Boku no Hero','Inuyasha','Jujutsu Kaisen','Kimetsu no Yaiba'],
    'Rating' : [9,8.5,9.2,10]
})

df 
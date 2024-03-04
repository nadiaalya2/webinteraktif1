import streamlit as st
def page_4():
    st.title("Hayoloooo")
    st.write("Halaman ini digunakan untuk Rumus Matematika Part 1. Jadi, sesudah menonton anime yukk belajar matematika bersama Nadia Alya^-^")
    
    with open('rumus.md','r') as file:
        isi_teks = file.read()
    st.markdown(isi_teks)
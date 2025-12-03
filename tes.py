import streamlit as st

st.title("Tugas Farel")
st.header("Tes Streamlit") 

rate = st.number_input("Rating", min_value=0, max_value=10,step=1)
st.write(f"Rating Anda = {rate}")

with st.form("Pengisi Rating"):
        st.write("Pengisi Rating")
        nama = st.text_input("nama")
        NIM = st.text_input("NIM")
        usia = st.number_input("usia",min_value=0, max_value=100, step=1)
        
    
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f"nama saya adalah {nama}, NIM saya {NIM} dan usia saya {usia}")

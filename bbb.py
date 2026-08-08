import streamlit as st
st.title("名前記憶アプリ")
st.session_state.neme = st.text_input("あなたの名前を入力してください")
if  st.button("名前を記憶"):
    st.write(f"kiokusiteirunamae:"{st.session_state.neme})




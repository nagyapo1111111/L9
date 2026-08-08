import streamlit as st
st.title("ユーザー情報入力")
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
name = st.text_input("あなたの名前を入力してください")    
if 'user_grade' not in st.session_state:
    st.session_state.user_grade = ""
grade = st.selectbox("gakunenn",["小５","小６","中１","中２"])
if 'user_hobbies' not in st.session_state:
    st.session_state.user_hobbies = ""
hobbies = st.multiselect("syumi",["読書","スポーツ","ゲーム"])
if st.button("情報を保存"):
    st.session_state.user_name = name
    st.success("情報を保存しました")
    st.write(f"現在保存されている情報:{st.session_state.user_name}") 

import streamlit as st
from storage import load_history, save_history
from ai import ai_convo

st.title("AI Chatbot Gloria")

if "history" not in st.session_state:
    st.session_state.history = load_history()

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.history.append({"role":"user","content":prompt})
    with st.spinner("Mulling"):
        reply=ai_convo(st.session_state.history)
    st.session_state.history.append({"role":"assistant","content":reply})
    save_history(st.session_state.history)

for m in st.session_state.history:
    with st.chat_message(m["role"]):
        st.write(m["content"])

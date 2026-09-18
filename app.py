import streamlit as st
from storage import load_history, save_history , clear_history
from ai import ai_convo

st.title("AI Chatbot Gloria")

if "history" not in st.session_state:
    st.session_state.history = load_history()

def clear_chat():
    st.session_state.history = []
    clear_history()

st.sidebar.button("Clear History", on_click=clear_chat)

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

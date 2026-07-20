import streamlit as st


def initialize_session():
    defaults = {
        "index": None,
        "chunks": None,
        "current_resume": None
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
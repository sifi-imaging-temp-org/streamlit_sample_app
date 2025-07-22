import streamlit as st

APP_NAME = "My first app"
APP_VERSION = "0.3.0"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="👋",
    menu_items={
        'about': f"{APP_NAME} v{APP_VERSION}"
    }
)

st.write(f"""
# {APP_NAME}
Hello *world!*
""")
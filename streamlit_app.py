import streamlit as st
from openai import OpenAI

# Show title and description.
# st.title("📄 Document question answering")
st.set_page_config(page_title=None, page_icon=None, layout="centered",
initial_sidebar_state="auto", menu_items=None)
first_page=st.Page("lab1.py", title="First page", icon=None,
url_path=None, default=False)
second_page=st.Page("lab2.py", title="Second page", icon=None,
url_path=None, default=True)
pg=st.navigation([first_page,second_page])
st.set_page_config(page_title="Data Manager",page_icon=":material/edit:")
pg.run()
from utils import get_answer, get_summary, init_conversation, get_desc
import streamlit as st
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()
st.set_option('deprecation.showPyplotGlobalUse', False)

# Streamlit Application
st.set_page_config(page_title="Chat With CSV",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')


st.header("Chat With CSV 🤖")
file_path = ""
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    if (not uploaded_file.name.endswith(".csv")):
        st.error('Please Upload A CSV File', icon="🚨")
    else:
        bytes_data = uploaded_file.getvalue()
        file_hash = hashlib.sha256(bytes_data).hexdigest()
        file_path = os.path.join("files", f"{file_hash}.csv")
        if (not os.path.exists(file_path)):
            with open(file_path, 'wb') as f:
                f.write(bytes_data)

    # Create Tabs

    summary, visualization, chat = st.tabs(
        ["Get Summary", "Get Visuals", "Chat With AI 🧠"])

    with (summary):
        with st.spinner("Please Wait"):
            st.write(get_summary(file_path))

    with (visualization):
        data = get_desc(file_path)

        st.bar_chart(data)
        st.line_chart(data)
        st.area_chart(data)
    with (chat):
        prompt = st.chat_input("Enter Your Prompt")
        if (prompt):
            st.chat_message("USER").write(prompt)
            agent = init_conversation(file_path)
            with st.spinner("Please Wait"):
                st.chat_message("ASSISTANT").write(
                    f"{get_answer(prompt, agent)}")

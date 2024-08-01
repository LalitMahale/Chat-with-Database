import streamlit as st
from utils import Chain
from utils import DB
st.set_page_config(page_title="💬 Chat_to_DB")

# st.title(":red[Chat] to :red[Database]")
st.markdown("<h1 style='text-align: center;'>Chat to Database</h1>", unsafe_allow_html=True)

st.sidebar.subheader("See table")
row = st.sidebar.number_input("Enter Number of rows", min_value=5,step=1)
st.sidebar.write(DB().see_table(rows = row))

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = Chain().final_sql(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
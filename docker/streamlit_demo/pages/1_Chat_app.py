import streamlit as st
import random
import time

st.set_page_config(
    page_title="Chatbot Streamlit App",
    layout="wide"
)

st.title("Chatbot demo")

funny_messages = [
    "I'm not lazy, I'm on energy-saving mode.",
    "I’m not arguing, I’m just explaining why I’m right.",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kat ads.",
    "Artificial intelligence is no match for natural stupidity.",
    "Why did the scarecrow become a successful software engineer? Because he was outstanding in his field!",
    "My life’s a constant cycle of ‘What the heck is this?’ and ‘Eh, it’ll be fine.’",
    "I told a joke about a roof... but it went over everyone's head.",
    "Why did the AI cross the road? To optimize the chicken's algorithm.",
    "My computer sings sometimes. It's a Dell."
]

with st.sidebar:
    if st.button("Reset Conversation", help="Reset the conversation"):
        st.session_state["messages"] = [{"role": "assistant", "content": "Hi, how can I help you?"}]


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi, how can I help you?"}]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    assistant_message = random.choice(funny_messages)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in assistant_message.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(assistant_message, unsafe_allow_html=True)

    st.session_state["messages"].append({"role": "assistant", "content": assistant_message})

import streamlit as st
import requests

st.set_page_config(page_title="Amr Chatbot", page_icon="🤖")
st.title("Amr's Simple Chatbot")
st.subheader("NTI (NLP Internship) ")



# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Show past chat messages
for msg in st.session_state.messages[1:]:  # skip system message
    st.chat_message("🧑" if msg["role"] == "user" else "🤖").write(msg["content"])

# User input
user_query = st.text_input("You:", key="user_input")

if user_query:
    # Add user message
    st.chat_message("🧑").write(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Send entire message history to LLM
    try:
        response = requests.post(
            "http://127.0.0.1:8000/llm/full/",
            json={"messages": st.session_state.messages}
        )
        if response.status_code == 200:
            bot_reply = response.json()["answer"]
        else:
            bot_reply = "⚠️ API Error"
    except Exception as e:
        bot_reply = f"❌ Error: {e}"

    # Display and save bot reply
    st.chat_message("🤖").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
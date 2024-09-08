import streamlit as st
from gradio_client import Client

client = Client("sugamer/MMORPG", hf_token="")

st.set_page_config(page_title="MMORPG SHOP - Harga Murah", page_icon="🗡️")
st.title("TOKOMMORPG🗡️")

st.write("Selamat data di toko MMORPG, selamat berbelanja")

if "history" not in st.session_state:
    st.session_state["history"] = []

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

def get_bot_response(user_input, history):
    response = client.predict(
		message=user_input,
		system_message="Anda adalah seorang pedagang dalam dunia MMORPG, tawarkan barang dagangan anda beserta harganya",
		max_tokens=512,
		temperature=0.7,
		top_p=0.95,
		api_name="/chat"
    )

    return response

user_input = st.text_input("You:", value=st.session_state["user_input"], placeholder="Ask anything...", key="input_field")

send_button = st.button("Send")

if send_button and user_input:
    bot_response = get_bot_response(user_input, st.session_state["history"])
    
    st.session_state["history"].append({"user": user_input, "bot": bot_response})
    
    st.session_state["user_input"] = ""

st.subheader("Chat History:")
if st.session_state["history"]:
    for chat in st.session_state["history"]:
        st.write(f"**You**: {chat['user']}")
        st.write(f"**Bot**: {chat['bot']}")
else:
    st.write("Start a conversation Above!")

if st.button("Clear Chat"):
    st.session_state["history"] = []
    st.session_state["user_input"] = ""
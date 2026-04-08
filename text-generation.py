import streamlit as st
from openai import OpenAI

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Text Generation",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom, #4f6f8f, #9a9a9a);
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.main-container {
    max-width: 420px;
    margin: auto;
    padding-top: 20px;
    color: white;
    text-align: center;
}

.top-bar {
    margin-left: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 22px;
    margin-bottom: 20px;
    color: white;
}

.subtitle {
    font-size: 18px;
    margin-top: 15px;
    margin-bottom: 25px;
    color: white;
    text-align: center;
}

.response-box {
    background-color: rgba(0,0,0,0.25);
    padding: 15px;
    border-radius: 18px;
    color: white;
    margin-top: 20px;
}

.stTextInput > div > div > input {
    border-radius: 20px;
    background-color: #3b3b3b;
    color: white;
}

.stButton > button {
    width: 100%;
    border-radius: 20px;
    background-color: #3b3b3b;
    color: white;
    border: none;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- MAIN CONTAINER ----------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Top bar
st.markdown("""
<div class="top-bar">
    <span><b>Text Generation</b></span>
</div>
""", unsafe_allow_html=True)

# Space before logo
st.markdown("<br>", unsafe_allow_html=True)

# ---------------- CENTERED LOGO ----------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("logo.png", width=220)

# Subtitle
st.markdown("""
<div class="subtitle">
    Your step to developement world
</div>
""", unsafe_allow_html=True)

# ---------------- API KEY ----------------
api_key = st.text_input(
    "API Key",
    type="password",
    placeholder="Enter your API key"
)

# ---------------- MESSAGE INPUT ----------------
user_message = st.text_input(
    "",
    placeholder="Ask Echo ?"
)

# ---------------- SEND BUTTON ----------------
if st.button("➤ Send"):
    if not api_key:
        st.warning("Please enter your API key")
    elif not user_message:
        st.warning("Please type a message")
    else:
        try:
            client = OpenAI(
                base_url="https://router.huggingface.co/v1",
                api_key=api_key
            )

            completion = client.chat.completions.create(
                model="zai-org/GLM-4.7-Flash:novita",
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            st.markdown(
                f'<div class="response-box">{completion.choices[0].message.content}</div>',
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
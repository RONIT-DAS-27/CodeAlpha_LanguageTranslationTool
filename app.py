import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.set_page_config(page_title="Advanced Translator", layout="centered")
st.markdown("""
<style>

/* Overall background */
.stApp {
    background: linear-gradient(135deg, #e0f2fe, #f8fafc);
}

/* Main card container */
.block-container {
    background: white;
    padding: 40px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    max-width: 750px;
    margin-top: 50px;
}

/* Title */
h1 {
    text-align: center;
    font-weight: 700;
    color: #0f172a;
}

/* Text area styling */
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #111827 !important;
    border-radius: 10px !important;
    border: 1px solid #cbd5e1 !important;
    padding: 12px !important;
    font-size: 15px !important;
}

/* Dropdown styling */
.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px !important;
}

/* Button styling */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    border-radius: 8px;
    padding: 8px 18px;
    font-weight: 600;
    border: none;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
    color: white;
}

/* Success box */
.stSuccess {
    background-color: #dcfce7 !important;
    color: #166534 !important;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
st.title("🌍 Advanced Language Translation Tool")

text = st.text_area("Enter text to translate:")

languages = {
    "Hindi": "hi",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

target_lang = st.selectbox("Select Target Language", list(languages.keys()))

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(source="auto", target=languages[target_lang]).translate(text)

        st.success("Translated Text:")
        st.write(translated)

        # Text to Speech
        tts = gTTS(translated, lang=languages[target_lang])
        tts.save("output.mp3")

        audio_file = open("output.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

    else:
        st.warning("Please enter text.")
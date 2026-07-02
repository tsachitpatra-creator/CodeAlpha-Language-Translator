import streamlit as st
from deep_translator import GoogleTranslator

# Page configuration
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 AI Language Translation Tool")
st.write("Translate text instantly into multiple languages.")

# Languages
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa"
}

# Source and target language
source_lang = st.selectbox(
    "Translate From",
    list(languages.keys()),
    index=0
)

target_lang = st.selectbox(
    "Translate To",
    list(languages.keys()),
    index=2
)

# Text input
text = st.text_area(
    "Enter text to translate",
    height=150
)

# Translate button
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    elif source_lang == target_lang and source_lang != "Auto Detect":
        st.warning("Source and target languages cannot be the same.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.subheader("✅ Translated Text")
            st.success(translated)

        except Exception as e:
            st.error("Translation failed. Please check your internet connection and try again.")

# Footer
st.markdown("---")
st.caption("Developed by Sachit Patra | CodeAlpha AI Internship")
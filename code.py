import streamlit as st
from deep_translator import GoogleTranslator

# Page settings
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍"
)

# Title
st.title("🌍 Language Translation Tool")
st.write("Translate text from one language to another.")

# Languages
languages = {
    "English": "en",
    "Bangla": "bn",
    "Hindi": "hi",
    "Arabic": "ar",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Turkish": "tr"
}

# Language selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "From:",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "To:",
        list(languages.keys()),
        index=1
    )

# Text box
text = st.text_area(
    "Enter your text:",
    height=150,
    placeholder="Type something here..."
)

# Translate button
if st.button("🔄 Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text.")

    elif source_language == target_language:
        st.warning("Please select different languages.")

    else:
        try:
            translator = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            )

            translated_text = translator.translate(text)

            st.success("Translation complete!")

            st.subheader("Translated Text")
            st.write(translated_text)

        except Exception as error:
            st.error("Translation failed.")
            st.write("Error details:")
            st.code(str(error))
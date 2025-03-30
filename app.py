import streamlit as st
import joblib

# Load the local Random Forest model
@st.cache_resource
def load_local_model():
    return joblib.load("model.pkl")

# Classify Emotion Locally
def classify_emotion_local(text, model):
    emotion = model.predict([text])[0]
    return emotion

# Streamlit UI
st.title("Local Text-to-Emotion Classifier (Random Forest)")

# Load the model
model = load_local_model()

# Text input
user_text = st.text_area("Enter text:", "I am very happy today!")

if st.button("Classify Emotion"):
    emotion = classify_emotion_local(user_text, model)
    st.write(f"Detected Emotion: **{emotion.capitalize()}**")

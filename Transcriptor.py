#Yukta Wagh

import streamlit as st
import speech_recognition as sr


# Streamlit app
def main():
    st.title("Real-Time Speech Transcription")
    st.write("Click the 'Start Recording' button and speak to get the transcription!")

    if st.button("Start"):
        st.write("Listening...")
        transcription = transcribe_audio()
        st.write("Transcription: ", transcription)


# Function to transcribe audio using the speech_recognition module
def transcribe_audio():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        transcription = r.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        st.error("Unable to transcribe audio. Please try again.")
    except sr.RequestError:
        st.error("Transcription service is currently unavailable. Please try again later.")

    return ""


if __name__ == "__main__":
    main()
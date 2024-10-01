import speech_recognition as sr
import pyttsx3
import pyaudio
import subprocess
import numpy as np
import librosa
from sklearn.svm import SVC
import pickle
import webbrowser

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def recognize_speech_from_mic():
    """Capture and recognize speech from the microphone."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        speech_text = recognizer.recognize_google(audio)
        return speech_text.lower()
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return None

def run_file(file_path):
    try:
        subprocess.run(file_path, check=True, shell=True)
        print(f"Successfully ran file: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run file: {file_path}. Error: {e}")

def main():
    try:
        speak("Welcome back sir!")
        speak("How may I assist you?")

        audio_path = recognize_speech_from_mic()
        if audio_path is None:
            return

        while True:
            speech_text = recognize_speech_from_mic()

            if speech_text:
                    print(f"You said: {speech_text}")
                    if any(phrase in speech_text.lower() for phrase in ["halo close", "halo exit", "halo turn off"]):
                        speak("Turning off, goodbye!")
                        break
                    elif any(phrase in speech_text.lower() for phrase in ["halo hi", "halo hello"]):
                        speak("Hi, how can I help you?")
                    elif any(phrase in speech_text.lower() for phrase in ["halo sudo apt virus check", "halo virus check"]):
                        speak("Running the virus check file...")
                        file_path = "C:/Program Files/Google/Chrome/Application/Chrome.exe"  # Update this path to your file
                        run_file(file_path)
                    elif any(phrase in speech_text.lower() for phrase in ["halo im bored"]):
                        speak("wanna play a game?")
                        if any(phrase in speech_text.lower() for phrase in ["halo sure"]):
                            speak("Ok let's play a random number picker game")
                    elif any(phrase in speech_text.lower() for phrase in ["search test on google"]):
                        webbrowser.open_new_tab("https://www.youtube.com/watch?v=9bZkp7q19f0")
                        break

    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to exit...")
if __name__ == "__main__":
    main()

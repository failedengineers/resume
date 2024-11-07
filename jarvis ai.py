import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")


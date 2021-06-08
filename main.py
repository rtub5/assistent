import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def sendEmail(to, content):
    pass


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishuser():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour <= 12):
        speak("Good Morning")
    elif (hour > 12 and hour <= 18):
        speak("Good Afternoon")
    elif (hour > 18 and hour < 24):
        speak("Good Night")

    speak("Hello, I am your assistant David. How may I help you?")


def takeCommand():
    # it takes microphone voice as input and shows us the output as string.
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(" User said - " + query)

    # except sr.UnknownValueError:
    #     print("Could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results; {0}".format(e))

    except Exception as e:
        print("Say that again please")
        return "None"

    return query


if __name__ == "__main__":
    wishuser()

    while(True):
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching results on wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ,")
            speak(results)

        elif "by david" in query:
            speak("Bye Bye see you later..")
            break

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            speak("opening youtube..")

        elif "open code" in query:
            path = "C:\\Users\\Harman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "send email to self" in query:

            try:
                speak("sending email to self..")
                to = "harman18284@gmail.com"
                content = "Hey bro"
                sendEmail(to, content)
                speak("Email sent")

            except Exception as e:
                print(e)
                speak("Email sending failed..")

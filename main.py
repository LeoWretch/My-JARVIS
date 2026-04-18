import os
import time
import pyttsx3
from actions import apps
from actions import files
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # improves accuracy
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    
    except sr.UnknownValueError:   #if didnt hear properly
        print("Could not understand")
        speak("can u say properly")
        return ""

    except sr.RequestError:
        print("Internet issue")
        return ""

# while True:
#     cmd = listen()
#     if "hello" in cmd:
#         speak("Hello, I am your assistant")

while True:
    cmd = listen()

#normals talking with my jarvis
    if "hello jarvis" in cmd:
        speak("Hello , I am your Jarvis , At your service, sir.")

    elif "how are you" in cmd:
        speak("All systems are operating within normal parameters, sir")

    # elif "open chrome" in cmd:
    #     speak("Opening Chrome")
    #     os.system("start chrome")

    elif "open chrome" in cmd:
        speak("Opening chrome")
        apps.open_chrome()    

    elif "open google" in cmd:
        speak("Opening Google")
        apps.open_google()

    elif "open notepad" in cmd:
        speak("Opening Notepad")
        apps.open_notepad()

    elif "open spotify" in cmd:
        speak("Opening Spotify") #not speaking
        engine.runAndWait() #this will make the system to wait and complete the speech
        apps.open_spotify()

    elif "read document" in cmd:
        speak("Reading your document")
        try:
            print("Trying to read file...")
            content = files.read_text_file("texttospeak.txt")
            print("FILE CONTENT:")
            print(content)
            # speak(content[:100])
            for line in content.split("."):
                if line.strip():
                    speak(line)
                    time.sleep(0.5)
            engine.runAndWait()        
        except Exception as e:
            print("ERROR:", e)
            speak("Error reading file")

    # elif "read document" in cmd:
    #     speak("Reading your document")
    #     engine.runAndWait()

    #     print("Going to read the content")
    #     content = files.read_text_file("texttospeak.txt")
    #     print("File content is this:-")
    #     print(content)
    #     # content = files.read_word_file("E:\\Jarvis\\texttospeak.txt")  # change path (later work)
    #     speak(content[:100])  # speak first part (avoid too long)    

    elif "open valorant" in cmd:
        speak("Launching Valorant")
        apps.open_valorant()
    
    elif "open resident evil 7" in cmd:
        speak("Launching Resident Evil 7 Biohazard")
        apps.open_re7()   
    
    elif "exit" in cmd:
        speak("Goodbye")
        break
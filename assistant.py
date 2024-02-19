import speech_recognition as sr
import os
import webbrowser
import openai
import pyttsx3
import datetime
import random
from config import api_key
chatStr = " "

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "api_key" 
    chatStr += f"Sarim: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    global chatstr 
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    if "choices" in response and response["choices"]:
        text = response["choices"][0]["message"]["content"]
        if not os.path.exists("openai"):
            os.mkdir("openai")

        with open(f"openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    else:
        print("No valid response received from OpenAI.")

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print("J.A.R.V.I.S")
    say("Hi I am JARVIS, your assistant, what would you like me to do?")
    while True:
        print("Listening...")
        text = takeCommand()
        if "how are you".lower() in text.lower() or "how are you doing".lower() in text.lower():
            say("I am doing well, I am here to assist you. Give me a task to do.")
        if "open Youtube".lower() in text.lower():
            webbrowser.open("https://youtube.com")
            say("Opening Youtube...")
        if "open google".lower() in text.lower():
            webbrowser.open("https://www.google.com/")
            say("Opening GOOGLE...")
        if "open Facebook".lower() in text.lower():
            webbrowser.open("https://www.facebook.com/")
            say("Opening facebook...")
        if "open instagram".lower() in text.lower():
            webbrowser.open("https://www.instagram.com/")
            say("Opening instagram...")
        if "open chat GPT".lower() in text.lower():
            webbrowser.open("https://chat.openai.com/")
            say("Opening chat GPT...")
        # ---------------------------------------------------------------------------------------------------------------------------------------------------apps
        if "open chrome".lower() in text.lower():
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            say("Opening chrome...")
        if "open mail".lower() in text.lower():
            os.startfile("C:\Program Files\Windows Mail\wab.exe")
            say("Opening mail...")
        if "open spotify".lower() in text.lower():
            os.startfile("C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.230.1135.0_x64__zpdnekdrzrea0\Spotify.exe")
            say("Opening spotify...")
        if "open notepad".lower() in text.lower():
            os.startfile("C:\Program Files/WindowsApps/Microsoft.WindowsNotepad_11.2312.18.0_x64__8wekyb3d8bbwe/Notepad/Notepad.exe")
            say("Opening notepad...")
        if "open calculator".lower() in text.lower():
            os.startfile("C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2311.0.0_x64__8wekyb3d8bbwe\CalculatorApp.exe")
            say("Opening calculator...")
        if "open whatsapp".lower() in text.lower():
            os.startfile("C:/Program Files/WindowsApps/5319275A.WhatsAppDesktop_2.2403.10.0_x64__cv1g1gvanyjgm/WhatsApp.exe")
            say("Opening WhatsApp...")
        if "the time".lower() in text.lower():
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strftime}")
            # add more apps
        if "using artificial intelligence".lower() in text.lower():
            ai(prompt=text)
        if "Jarvis" in text.lower() and "quit" in text.lower():
            exit()

import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
   if "open google" in c.lower():
       webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
       webbrowser.open("https://facebook.com") 
   elif "open whatsapp" in c.lower():
       webbrowser.open("https://whatsapp.com")  
   elif "open linkedin" in c.lower():
       webbrowser.open("https://linkedin.com") 
   elif "open youtube" in c.lower():
       webbrowser.open("https://youtube.com") 
   elif "open tiktok" in c.lower():
       webbrowser.open("https://tiktok.com")
   elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link = musicLibrary.music[song]
       webbrowser.open(link)

   elif "stop" in c.lower():
       speak("Good Bye!")
       exit()

if __name__=="__main__":
    speak("Jarvis")
    #Listen for the wake word "Jarvis"
    #Obtain audio from microphone
    while True:
        r=sr.Recognizer()
       
        #Recognize speech using Google
        
        with sr.Microphone() as source:
             r.adjust_for_ambient_noise(source)
             print("Listening!..")
             try:
                 audio=r.listen(source,timeout=2,phrase_time_limit=1)
                 print("Recognizing")
             except sr.WaitTimeoutError:
                 print("Listening timed out — no speech detected.")
                 continue
                 
        try:

               word = r.recognize_google(audio)
               if(word.lower()=="jarvis"):
                speak("Yess.")
                with sr.Microphone() as source:
                 print("Jarvis Active!..")
                 audio=r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)

        except sr.UnknownValueError:
            print("Couldn't understand audio")
        except sr.RequestError as e:
            print("Recognition error: {0}".format(e))

import webbrowser
import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime

# Method taking the voice from the machine
def speak(audio):
    engine = pyttsx3.init()

    # getter method (gets the current value of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and [1]=female voice in set Property
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the currently queued commands
    engine.runAndWait()

def take_query():
    # calling the hello function to make it more interactive
    Hello()

    # loop until we say bye to exit the program
    while(True):
        # take the queries and make it lower case to match query better
        query = takeCommand().lower()
        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")

            # opens the browser to geeksforgeeks
            webbrowser.open("www.geeksforgeeks.com")
            continue
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif "which day it is" in query:
            tellDay()
            continue
        elif "tell me the time" in query:
            tellTime()
            continue

        # exits the program
        elif "bye" in query:
            speak("Bye. Check out GFG for more exciting things.")
            exit()
        elif "from wikipedia" in query:
            # information from wikipedia
            speak("Checking the wikipedia")
            query = query.replace("wikipedia", "")

            # summary of 4 lines from wikipedia
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak("I am Sarah. Your desktop assistant")

# takes commands and recognizing the command from the speech_Recognition module
def takeCommand():
    r = sr.Recognizer()

    # use the micropone module for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # try and catch if the sound is recognized
        try:
            print("Recognizing")

            # for Listening the command in indian english we can also use 'hi-In' for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
             
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
         
        return Query

def tellDay():
     
    # telling the day of the week
    day = datetime.datetime.today().weekday() + 1
     
    # this line tells us about the number that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime(self):
    # will give the time
    time = str(datetime.datetime.now())         # will display like "2022-06-10 14:34:19.582630"

    print(time)
    hour = time[11:13]
    min = time[14:16]
    self.Speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")

def Hello():
    speak("hello sir I am your desktop asssitant. / Tell me how may I help you")

if __name__ == '__main__':
    # main method for executing the functions
    take_query()

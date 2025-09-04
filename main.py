import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import pyjokes
from datetime import datetime
import my_music
import files_library
import youtube
import subprocess as sp # for accessing window's file explorer

# recognizer = sr.Recognizer()

# engine = pyttsx3.init()
# print(engine.getProperty('volume'))

def speak(text):
    engine = pyttsx3.init() # engine object is created(that knows how to command OS's internal text to speech system)
    voices = engine.getProperty('voices') # gets list of voices [David and Zira]
    engine.setProperty('voice', voices[1].id) # chooses female voice (Zira)
    engine.setProperty('rate', 150) # sets the speak rate to 150
    engine.say(text)
    engine.runAndWait()
    # engine.stop()

# this will access given links
def processCommand(c):
    if ('open google' in c.lower()):
        wb.open('https://google.com')

    elif('open youtube' in c.lower()):
        wb.open('https://youtube.com')

    elif('yt history' in c.lower()):
        wb.open("https://www.youtube.com/feed/history")

    elif('open gmail' in c.lower()):
        wb.open('https://gmail.com')

    elif('open github' in c.lower()):
        wb.open('https://github.com')
    
    elif('open perplexity' in c.lower()):
        wb.open('https://perplexity.ai')

    elif('open chat' in c.lower()):
        wb.open('https://chatgpt.com')
    
    elif('open amazon' in c.lower()):
        wb.open('https://amazon.in')

    elif('open flipkart' in c.lower()):
        wb.open('https://flipkart.com')


    # this will access music library
    elif c.lower().startswith('play'): # the command must start with play

        parts = c.lower().split(' ', 1) # split for once
        song = parts[1].strip() # removes whitespace character if any

        if song in my_music.music_library:
            link = my_music.music_library[song]
            wb.open(link)
        
        else:
            speak(f'The {song} is not in your music library.')

    # this will access youtube library
    elif c.lower().startswith('show'):

        video = (c.lower().split(' ', 1)[1]).strip() # removes whitespace character if any

        if video in youtube.youtube_videos:
            link = youtube.youtube_videos[video]
            wb.open(link)
        
        else:
            speak(f'{video} is not in your youtube library')


    # accessing windows file explorer
    elif('open file explorer' in c.lower()):
        sp.Popen('explorer') # opens this pc

    # accessing any specific folder in explorer
    elif(c.lower().startswith('access')):
        folder_name = (c.lower().split(' ', 1)[1]).strip()

        if folder_name in files_library.my_files:
            path = files_library.my_files[folder_name]
            sp.Popen(f'explorer "{path}"') # double-quote make sure path with spaces work perfectly

        else:
            speak(f'{folder_name} is not in your file library')

    # this one will tell a joke based on programming or any programming language
    elif('joke' in c.lower()):
        joke = pyjokes.get_joke()
        print(f'The joke: {joke}')
        speak(joke)



if __name__ == '__main__':
    # Listen for the wake word.
    speak('Initializing LISA !!') # LISA -> Local Intregated System Algorithm

    while True:
        r = sr.Recognizer() # r is recognizer object
        print('Recognizing....')


        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout = 5, phrase_time_limit = 4)

            # recognize speech/audio using Google
            word = r.recognize_google(audio) # stores whatever you said in the audio and turns it to text
            print(word) # prints the audio in text

            # Listen for wake word(LISA)
            if('lisa' in word.lower()):
                speak('LISA is online... . How may I help you ?')
                
                with sr.Microphone() as source:
                    print("Command LISA....")
                    audio = r.listen(source, timeout = 5, phrase_time_limit = 3)
                    command = r.recognize_google(audio)

                if('stop' in command.lower() or 'terminate' in command.lower()): # checks if there is "stop" word
                    speak('LISA is shut down.')
                    break

                elif('date' in command.lower()):
                    now_date = datetime.now().date() # takes date part only from date and time object
                    format_date = now_date.strftime('%d %B, %y')
                    print(f'Today\'s day is {format_date}')
                    speak(f'The date is {format_date}')

                elif('the time' in command.lower()):
                    now_time = datetime.now().time() # takes time part from date and time object
                    format_time = now_time.strftime('%I:%M:%S %p')
                    print(f'The time is {format_time}')
                    speak(f'The time is {format_time}')

                else:
                    processCommand(command)
            else:
                speak('you are either not audible or saying wrong name.')

        except Exception as e:
            print(f'Error ocurred: {e}')

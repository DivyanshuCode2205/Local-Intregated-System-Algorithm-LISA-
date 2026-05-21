import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import pyjokes
from datetime import datetime
import my_music
import files_library
import system_library
import youtube
import subprocess as sp # for accessing window's file explorer

# engine = pyttsx3.init()
# print(engine.getProperty('volume'))

def speak(text):
    engine = pyttsx3.init() # engine object is created(that knows how to command OS's internal text to speech system)
    voices = engine.getProperty('voices') # gets list of voices [David and Zira]
    engine.setProperty('voice', voices[1].id) # chooses female voice (Zira)
    engine.setProperty('rate', 150) # sets the speak rate to 150
    engine.say(text) # queues the text to be spoken
    engine.runAndWait() # speaks the text in the queue and holds/waits until all the text is spoken.
    # engine.stop()

# this will access given links
def processCommand(c):
    if ('google' in c.lower()):
        wb.open('https://google.com')

    elif ('maps' in c.lower()):
        wb.open('https://maps.google.com/?authuser=0')

    elif ('python site' in c.lower()):
        wb.open('https://www.python.org/')

    elif('youtube' in c.lower()):
        wb.open('https://youtube.com')

    elif('yt history' in c.lower()):
        wb.open("https://www.youtube.com/feed/history")

    elif('gmail' in c.lower()):
        wb.open('https://gmail.com')

    elif('github' in c.lower()):
        wb.open('https://github.com')
    
    elif('perplexity' in c.lower()):
        wb.open('https://perplexity.ai')

    elif('chat' in c.lower()):
        wb.open('https://chatgpt.com')
    
    elif('amazon' in c.lower()):
        wb.open('https://amazon.in')

    elif('flipkart' in c.lower()):
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
    elif(c.lower().startswith('get')):
        folder_name = (c.lower().split(' ', 1)[1]).strip()

        if folder_name in files_library.my_files:
            path = files_library.my_files[folder_name]
            sp.Popen(f'explorer "{path}"') # double-quote make sure path with spaces work perfectly

        else:
            speak(f'{folder_name} is not in your file library')

    elif(c.lower().startswith('access')):
        system_file = (c.lower().split(' ', 1)[1]).strip()

        if system_file in system_library.sys_files:
            path = system_library.sys_files[system_file]
            sp.Popen(f'explorer "{path}"')

        else:
            speak(f'{system_file} is not in the system library')


    # this one will tell a joke based on programming or any programming language
    elif('joke' in c.lower()):
        joke = pyjokes.get_joke()
        print(f'The joke: {joke}')
        speak(joke)



if __name__ == '__main__':
    # Activation
    speak('Initializing LISA !!') # LISA -> Local Intregated System Algorithm

    while True:
        r = sr.Recognizer() # r is recognizer object
        print('Recognizing....')


        try:
            with sr.Microphone() as source:
                print("Listening....") # This is wake command
                audio = r.listen(source, timeout = 5, phrase_time_limit = 4)

            # recognize speech/audio using Google
            word = r.recognize_google(audio) # stores whatever you said in the audio and turns it to text
            print(word) # prints the audio in text

            # Listen for wake word(LISA)
            if('lisa' in word.lower()):
                from random import choice
                response = ["Yes, Divyanshu how can I help you today ?", "Yes Divyanshu !",
                             "What's your query ?", "What can I do for you ?"]
                random_response = choice(response)
                speak(random_response)
                
                with sr.Microphone() as source:
                    print("Command LISA ....")
                    audio = r.listen(source, timeout = 5, phrase_time_limit = 4)
                    command = r.recognize_google(audio)

                if('stop' in command.lower() or 'terminate' in command.lower()): # checks if there is "stop" word
                    speak('LISA is shut down.')
                    break

                elif('date' in command.lower()):
                    now_date = datetime.now().date() # takes date part only from date and time object
                    format_date = now_date.strftime('%d %B, %y') # Date Month, Year
                    week_day = now_date.strftime('%A')
                    print(f'Today\'s day is {format_date}')
                    speak(f'The date is {format_date}')

                    print(f'Today\'s weekday is {week_day}')
                    speak(f'Weekday is {week_day}')

                elif('time' in command.lower()):
                    now_time = datetime.now().time() # takes time part from date and time object
                    format_time = now_time.strftime('%I:%M:%S %p') # Hour:Minute:Second AM/PM
                    print(f'The time is {format_time}')
                    speak(f'The time is {format_time}')

                else:
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("I didn't hear anything.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
        except sr.RequestError:
            print("Network problem while recognizing.")


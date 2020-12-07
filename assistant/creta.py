"""
Creta - your virtual assistant
"""

from tkinter import *

from tkinter import messagebox as mb

import pyttsx3

import random

from datetime import datetime

import wikipedia

import webbrowser

import os

import requests


class Window:
    greet = ['Hey there!', 'Hello! It\'s good to meet you.', 'Hello! Its good to talk to you!',
             'Hello, How can I help You', 'Hi!']

    how = ['I am as good as I can be and I am trying my best to try the best I can',
           'I am quite fine. Thanks for asking.', 'I am good and ready to help!',
           'Talking to you always makes me happy']

    name = ['The name is Creta. Just Creta', 'I am Creta. I find that it is a great conversation starter',
            'I am Creta, your assistant']

    creator = ['I was made by Amey. Thanks for asking! ', 'I was Made by Amey', 'I am made by Amey, the programmer']

    can = ['I can do what you ask for', 'I can open apps or websites, tell the time and much more!']

    error = ["Sorry, I am not sure.", 'Sorry, I am unable to understand', 'Can you repeat?',
             'I have trouble understanding.']

    here = ['To Help You Out', 'To Help You To Do Tasks', 'To Be Your Assistant', 'To help you']

    frd = ['Thanks', 'Thank you!']

    me = ['I am talking to you.', 'I am talking to none other than you.']

    thanks = ['Your very very welcome!', 'My pleasure', 'Welcome!', 'Thanks!']

    nothing = ['You have not typed anything.', 'Make sure that you have typed something.']

    # You can add your own dialogs

    def __init__(self):
        self.win = Tk()
        self.win.geometry('380x300')
        self.win.title("Creta: the assistant")
        self.win.resizable(False, False)
        self.win.configure(bg='white')

        Label(self.win, text='Creta assistant', font=('arial black', 18), fg='white', width=30, bg='black', bd=5).pack()

        Label(self.win, text='You', font=('arial black', 20), fg='black', bg='white').place(x=60, y=50)
        Label(self.win, text='Creta', font=('arial black', 20), fg='black', bg='white').place(x=260, y=50)

        self.text_box1 = Text(self.win, font=('arial black', 13), width=16, height=5, fg='#F40202', bg='#029CF4',
                              wrap=WORD, relief=FLAT)
        self.text_box1.place(x=10, y=100)

        self.text_box2 = Text(self.win, font=('arial black', 13), width=15, height=5, fg='#029CF4', bg='#F40202',
                              wrap=WORD, relief=FLAT)
        self.text_box2.place(x=200, y=100)

        self.search_var = StringVar()

        Entry(self.win, font=('arial black', 14), width=18, textvariable=self.search_var, bg='#E7E7E7', fg='black',
              relief=FLAT, bd=5).place(x=10, y=250)

        Button(self.win, text='Send', font=('arial black', 10), relief=FLAT, bg='white', fg='black', bd=5,
               width=10,
               command=self.send()).place(x=270, y=250)

        # You can customise it as per as your needs

        def enter(*args):
            self.send()

        self.win.bind('<Return>', enter)

        self.win.mainloop()

    def about(self):
        about = Tk()
        about.configure(bg='black')
        about.geometry('400x250+300+450')

        Label(about, text='Creta - Your Virtual Assistant', bg='black', font=('Arial Black', 10, 'bold')).pack()

        Label(about, text='By: Amey V', bg='black', fg='white', font=('Arial Black', 10, 'bold')).pack()

        out = """Hi! I am Creta, a virtual assistant. 
    You just need to type, and I will give a typed
    as well as a spoken reply. I can open a number
    of apps, websites, I can search google and more!"""

        Label(about, text=out, bg='black', fg='white', font=('Arial Black', 10, 'bold')).pack()

        Button(about, text='Narrate', font=('Arial Black', 10, 'bold'),
               command=lambda: self.speak(out)).pack(side=RIGHT, padx=10)

        about.mainloop()

    # Creating the engine to speak
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def printing(self, out):
        self.text_box2.delete(1.0, END)
        self.text_box2.insert(INSERT, out)

    def speak(self, s):
        self.engine.say(s)
        self.engine.runAndWait()

    def send(self):
        user_input = self.search_var.get().lower()
        self.search_var.set('')
        self.text_box1.delete(1.0, END)
        self.text_box1.insert(INSERT, user_input)

        if 'about' in user_input and 'you' in user_input:
            output = 'Ok, Let me introduce myself.'
            self.printing(output)
            self.speak(output)
            self.about()

        elif 'you' in user_input:
            if 'who' in user_input and 'are' in user_input:
                r = random.randint(0, len(self.name) - 1)
                output = self.name[r]
                self.printing(output)
                self.speak(output)

            elif 'how are' in user_input:
                r = random.randint(0, len(self.how) - 1)
                output = self.how[r]
                self.printing(output)
                self.speak(output)

            elif 'good' in user_input:
                r = random.randint(0, len(self.frd) - 1)
                output = self.frd[r]
                self.printing(output)
                self.speak(output)
            elif 'who made' in user_input:
                r = random.randint(0, len(self.creator) - 1)
                output = self.creator[r]
                self.printing(output)
                self.speak(output)

            elif 'do' in user_input:
                r = random.randint(0, len(self.can) - 1)
                output = self.can[r]
                self.printing(output)
                self.speak(output)

            elif 'name' in user_input:
                r = random.randint(0, len(self.name) - 1)
                output = self.name[r]
                self.printing(output)
                self.speak(output)

            elif 'open' in user_input and 'youtube' in user_input:
                output = 'Opening Youtube'
                self.printing(output)
                self.speak(output)
                webbrowser.open('youtube.com')

            elif 'here' in user_input:
                r = random.randint(0, len(self.here) - 1)
                output = self.here[r]
                self.printing(output)
                self.speak(output)

            else:
                r = random.randint(0, len(self.error) - 1)
                output = self.error[r]
                self.printing(output)
                self.speak(output)

        elif 'who' in user_input and 'i' in user_input or 'my' in user_input and 'name' in user_input:
            r = random.randint(0, len(self.me) - 1)
            output = self.me[r]
            self.printing(output)
            self.speak(output)

        elif 'thanks' in user_input or 'thank you' in user_input:
            r = random.randint(0, len(self.thanks) - 1)
            output = self.thanks[r]
            self.printing(output)
            self.speak(output)

        elif 'good morning' in user_input:
            t = datetime.now().strftime('%H  hours and %M minutes')
            o = t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt) + ':' + str(o[3] + ' PM')
            else:
                time = str(o[0]) + ':' + str(o[3] + ' AM')

            try:
                url = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q' \
                      '=washington '
                json_data = requests.get(url).json()
                format_add = json_data['weather'][0]['main']
                format_temp = json_data['coord']['lat']
                output = f'Temperature In Your City is {format_temp} Degree Celsius, And  Climate is  {format_add}'

            except Exception:
                output = ' Weather Forecast Is Currently Unavailable'

            output = f'Good Morning, The Current Time is {time}, and {output}, Have A Good Day !'
            self.printing(output)
            self.speak(output)

        elif "good night" in user_input:
            output = "Have a nice sleep! Sweet dreams!"
            self.printing(output)
            self.speak(output)

        elif 'bored' in user_input:
            output = "Here's something to keep you output of boredom"
            self.printing(output)
            self.speak(output)
            webbrowser.open("neal.fun")

        elif 'translate' in user_input:
            output = "Translate what you want here: "
            self.printing(output)
            self.speak(output)
            webbrowser.open("translate.google.com")

        elif 'news' in user_input:
            output = "The current news can be found here: "
            self.printing(output)
            self.speak(output)
            webbrowser.open("bbc.com")

        elif 'weather' in user_input:
            try:
                if 'in' in user_input:
                    u = user_input.split()
                    for i in range(0, len(u)):
                        if u[i] == 'in':
                            city = u[i + 1]

                    api = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q' \
                          '=washington '
                    url = api + city
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    output = f'Temperature In {city} is {format_temp} Degree Celsius, And Climate is {format_add}'
                    self.printing(output)
                    self.speak(output)

                else:
                    url = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q' \
                          '=washington '
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    output = f'Temperature In Your city is {format_temp} Degree Celsius, And Climate is {format_add}'
                    self.printing(output)
                    self.speak(output)
            except Exception:
                output = 'I Was Unable To Connect To Internet.'
                self.printing(output)
                self.speak(output)

        elif 'where' in user_input and 'i' in user_input or 'location' in user_input:
            try:
                r = requests.get('https://ipinfo.io/')
                d = r.text.split()[4]
                output = 'You Location Is Near To ' + d
                self.printing(output)
                self.speak(output)
            except Exception:
                output = 'I Was Unable To Track Your Location'
                self.printing(output)
                self.speak(output)

        elif 'hello' in user_input or 'hi' in user_input:
            r = random.randint(0, len(self.greet) - 1)
            output = self.greet[r]
            self.printing(output)
            self.speak(output)

        elif 'exit' in user_input:
            output = 'Ok, Have a good Day!'
            self.printing(output)
            self.speak(output)
            self.win.destroy()

        elif 'open' in user_input:
            if 'google' in user_input:
                output = 'Opening Google'
                self.printing(output)
                self.speak(output)
                webbrowser.open('google.com')

            elif 'gmail' in user_input:
                output = 'Opening Google Mail'
                self.printing(output)
                self.speak(output)
                webbrowser.open("gmail.com")

            elif 'youtube' in user_input:
                output = 'Opening Youtube'
                self.printing(output)
                self.speak(output)
                webbrowser.open('youtube.com')

            elif 'bing' in user_input:
                output = "Opening Bing"
                self.printing(output)
                self.speak(output)
                webbrowser.open("www.bing.com")

            elif 'current' in user_input:
                output = 'Opening Current Working Directory'
                self.printing(output)
                self.speak(output)
                path = ''
                os.startfile(path)

            elif 'python' in user_input:
                output = 'Opening Python'
                self.printing(output)
                self.speak(output)
                path = 'E:\\'
                os.startfile(path)

            elif 'paint' in user_input:
                output = 'Opening Paint'
                self.printing(output)
                self.speak(output)
                path = r'C:\Windows\System32\mspaint.exe'
                os.startfile(path)

            elif 'wordpad' in user_input:
                output = 'Opening WordPad'
                self.printing(output)
                self.speak(output)
                path = r'C:\Program Files\Windows NT\Accessories\wordpad.exe'
                os.startfile(path)

            elif 'notepad' in user_input:
                output = 'Opening Note Pad'
                self.printing(output)
                os.chdir(r'E:\EXE_FILES\Text_editor')
                self.speak(output)
                path = r'E:\EXE_FILES\Text_editor\Text_editor.exe'
                os.startfile(path)

            elif 'code language' in user_input:
                output = 'Opening Code Language'
                self.printing(output)
                os.chdir(r'E:\EXE_FILES\CODE_LANGUAGE\V3.0')
                self.speak(output)
                path = r'E:\EXE_FILES\CODE_LANGUAGE\V3.0\CODE_LANGUAGE V3.0.exe'
                os.startfile(path)

            elif 'vlc' in user_input:
                output = 'Opening VLC'
                self.printing(output)
                self.speak(output)
                path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
                os.startfile(path)

            elif 'calculator' in user_input:
                output = 'Opening Calculator'
                self.printing(output)
                os.chdir(r'E:\EXE_FILES\calculator')
                self.speak(output)
                path = r'E:\EXE_FILES\CALCULATOR\CALCULATOR v2.0.exe'
                os.startfile(path)

            elif 'sticky notes' in user_input:
                output = 'Opening Sticky Notes'
                self.printing(output)
                os.chdir(r'E:\EXE_FILES')
                self.speak(output)
                path = r'E:\EXE_FILES\STICKY_NOTES.exe'
                os.startfile(path)

            elif 'browser' in user_input or 'chrome' in user_input:
                output = 'Opening Chrome Browser'
                self.printing(output)
                self.speak(output)
                path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                os.startfile(path)

            elif 'avast' in user_input or 'avast software' in user_input:
                output = 'Opening Avast'
                self.printing(output)
                self.speak(output)
                path = r'C:\Program Files\AVAST Software\Application\Avast.exe'

            elif 'vsc' in user_input:
                output = 'Opening Visual Studio Code'
                self.printing(output)
                self.speak(output)
                path = r"C:\Users\|user id|\AppData\Local\Programs\Microsoft Vs\Studio.exe" 
                # Make sure that you have used the correct user id 
                os.startfile(path)

            elif 'picture' in user_input or 'images' in user_input or 'photo' in user_input:
                output = 'Opening  Images'
                self.printing(output)
                self.speak(output)
                path = r'D:\Images\deep.exe'
                os.startfile(path)

            elif 'cmd' or 'command prompt' in user_input:
                output = 'Opening Command Prompt'
                self.printing(output)
                self.speak(output)
                path = r'C:\Windows\System32\cmd.exe'
                os.startfile(path)

            else:
                r = random.randint(0, len(self.error) - 1)  
                output = self.error[r]
                self.printing(output) 
                self.speak(output)  

        elif 'movie' in user_input:
            output = 'Playing Movies'
            self.printing(output)
            self.speak(output)
            mov_dir = r'D:\movies'
            songs = os.listdir(mov_dir)
            r = random.randint(0, len(mov_dir) - 2)
            os.startfile(os.path.join(mov_dir, songs[r]))

        elif 'screenshot' in user_input:
            output = 'Take ScreenShot'
            self.printing(output)
            self.speak(output)
            path = r'C:\Windows\system32\SnippingTool.exe'
            os.startfile(path)

        elif 'my' in user_input and 'image' in user_input or 'photo' in user_input or 'picture' in user_input:
            output = 'Opening Photos'
            self.printing(output)
            self.speak(output)
            path = r'D:\photo\deep'
            os.startfile(path)

        elif 'bye' in user_input:
            output = 'Ok bye! Have a nice day!'
            self.printing(output)
            self.speak(output)
            self.win.destroy()

        elif user_input == '':
            output = random.randint(0, len(self.nothing) - 1)
            self.printing(output)
            self.speak(output)

        elif 'time' in user_input:  # |
            t = datetime.now().strftime('%H  hours and %M minutes')  # |
            o = t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt) + ':' + str(o[3] + ' PM')
            else:
                time = str(o[0]) + ':' + str(o[3] + ' AM')
            output = 'Current time is : ' + time  # |
            self.printing(output)  # |
            self.speak(output)  # |

        elif 'wikipedia' in user_input:  # |
            i_l = list(user_input.split())  # |
            i_l.remove('wikipedia')  # |
            to2 = ''.join(i_l)  # |

            try:  # |
                output = 'According To Wikipedia ' + wikipedia.summary(to2, 2)  # |
                self.printing(output)  # |
                self.speak(output)  # |
            except Exception:  # |
                output = 'cannot find'  # |
                self.printing(output)  # |
                self.speak(output)  # |

        elif 'fine' in user_input:
            output = 'Great'
            self.printing(output)  # |
            self.speak(output)

        elif 'shutdown' in user_input:
            output = 'Shutting Down The System'
            self.printing(output)
            self.speak(output)
            os.system('shutdown -s')

        else:

            to_search = user_input
            output = 'Can I search that on google?'
            self.printing(output)
            self.speak(output)

            res = mb.askquestion('Google Search', 'Shall I search that on google?')

            if res == 'yes':
                output = 'Opening Google Search'
                self.printing(output)
                self.speak(output)
                webbrowser.open('https://www.google.co.in/search?q=' + to_search)
            else:
                output = 'Ok!'
                self.printing(output)
                self.speak(output)


root = Window()


from tkinter import *
from gtts import gTTS
from playsound import playsound
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("900x495+200+200")
root.resizable(False, False)
root.configure(bg="#305065")

engine=pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    spead = speed_combobox.get()
    language = language_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (spead == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (spead == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

    if (text):
        if (language == 'Hindi'):
            language = 'hi'
            output = gTTS(text=text, lang=language, slow=False)
            output.save("Audio.mp3")
            os.system("Audio.mp3")

        elif (language == 'English'):
            language = 'en'
            output = gTTS(text=text, lang=language, slow=False)
            output.save("Audio.mp3")

        elif (language == 'Marathi'):
            language = 'mr'
            output = gTTS(text=text, lang=language, slow=False)
            output.save("Audio.mp3")
            os.system("Audio.mp3")


def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    spead = speed_combobox.get()
    voices = engine.getProperty('voices')
    language = language_combobox.get()

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'Audio.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'Audio.mp3')
            engine.runAndWait()


    if (text):
        if (spead == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (spead == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

    if (text):
        if (language == 'Hindi'):
            language = 'hi'
            output = gTTS(text=text, lang=language, slow=False)
            output.save("Audio.mp3")


        elif (language == 'English'):
            language = 'en'
            output = gTTS(text=text, lang=language, slow=False)
            output.save("Audio.mp3")
            setvoice()

        elif (language == 'Marathi'):
            language = 'mr'
            output = gTTS(text=text, lang=language, slow=False)
            output.save("Audio.mp3")

#icon
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False, image_icon)

#Top Frame
Top_Frame = Frame(root, bg="light blue", width=900, height=100)
Top_Frame.place(x=0, y=0)

Logo = PhotoImage(file="speaker logo.png")
Label(Top_Frame, image=Logo, bg="light blue").place(x=250, y=5)

Label(Top_Frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="light blue", fg="black").place(x=345, y=30)

##########

Label( text="ENTER TEXT", font="arial 15 bold", bg="#305065", fg="white").place(x=20, y=140)
text_area = Text(root, font="Robote 15", bg="white", relief=GROOVE, wrap=WORD)

text_area.place(x=10, y=180, width=500, height=250)

Label(root, text='VOICE', font='arial 15 bold', bg='#305065', fg='white').place(x=580, y=160)
Label(root, text='SPEED', font='arial 15 bold', bg='#305065', fg='white').place(x=760, y=160)
Label(root, text='LANGUAGE', font='arial 15 bold', bg='#305065', fg='white').place(x=645, y=260)

gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 14', state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font='arial 14', state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

language_combobox = Combobox(root, values=['Hindi', 'English', 'Marathi'], font='arial 14', state='r', width=10)
language_combobox.place(x=645, y=300)
language_combobox.set('English')

image_icon = PhotoImage(file='speak.png')
btn=Button(root, text='Speak', compound=LEFT, image=image_icon, width=130, bg='#39c790', font='arial  14 bold', command=speaknow)
btn.place(x=550, y=370)

image_icon2 = PhotoImage(file='download.png')
save=Button(root, text='Save', compound=LEFT, image=image_icon2, width=130, bg='#39c790', font='arial 14 bold', command=download)
save.place(x=730, y=370)

root.mainloop()
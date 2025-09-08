from gtts import gTTS
from tkinter import *
import os
window = Tk()
def Playtext():
    s = gTTS(text=text.get(), lang='en', slow=False)

    s.save("test.mp3")

    os.system("start test.mp3")
text=Entry(window)
text.pack()
Button(window,text="Play",command=Playtext).pack()

window.mainloop()

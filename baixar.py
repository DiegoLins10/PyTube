## Para baixar a lib pytube:  pip install pytube 
## baixar um video do youtube com pytube
## python youtube.py   https://youtu.be/61R6Qq7mmIA
## gerar arquivo exe  pyinstaller --onefile -w baixar.py
## baixar pyinstaller pip install pyinstaller

from pytube import YouTube
from tkinter import *

def baixar():
    ##link = str(input("Digite o link: "))
    link = vlink.get()
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()
    print("baixado com sucesso") ##pega o conteudo
    indo()

def indo():
    a= "baixado com sucesso"
    Label(app, text=a,background="#dde", foreground="#009", anchor=W).place(x=10, y=100, width=200, height=20)

app = Tk() ##intanciando a classe
app.title("Youtube video download")
app.geometry("500x300") ## config tamanho janela
app.configure(background="#dde") ## mudar cor
Label(app, text="Link",background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20) ##declarar label
## posicionando o label

vlink = Entry(app)
vlink.place(x=10, y=30, width=200, height=20)

Button(app, text="Baixar", command=baixar).place(x=10, y=80, width=100, height=20)

app.mainloop()



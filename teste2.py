## Para baixar a lib pytube:  pip install pytube 
## baixar um video do youtube com pytube
## python youtube.py   https://youtu.be/61R6Qq7mmIA

from pytube import YouTube
from tkinter import *

def baixar():
    print("aa: %s"%vlink.get()) ##pega o conteudo
    print("aa: %s"%vlink.get("1.0", END)) ##pega o conteudo de um arquivo text()

app =Tk() ##intanciando a classe
app.title("Youtube video download")
app.geometry("500x300") ## config tamanho janela
app.configure(background="#dde") ## mudar cor
Label(app, text="Link",background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20) ##declarar label
## posicionando o label

vlink = Entry(app)
vlink.place(x=10, y=30, width=200, height=20)

Button(app, text="Baixar", command=baixar).place(x=10, y=270, width=100, height=20)

app.mainloop()


##link = str(input("Digite o link: "))
##video = YouTube(link)
##stream = video.streams.get_highest_resolution()
##stream.download()
app =Tk() ##intanciando a classe
app.title("Youtube video download")
app.geometry("500x300") ## config tamanho janela
##app.configure(background="#008") ## mudar cor
txt1 = Label(app, text="Youtube",background="#ff0", foreground="#000") ##declarar label
txt1.place(x=10, y=10, width=150, height=30) ## posicionando o label

app.mainloop()
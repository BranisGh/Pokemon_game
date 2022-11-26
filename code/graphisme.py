from tkinter import *
from main import *

class application:

    def __init__(self):
        self.window = Tk()
        self.window.title("Pokemon")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.iconbitmap("poke.ico")
        self.window.config(background='#4065A4')

        # initialization des composants
        self.frame = Frame(self.window, bg='#4065A4')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=True)
        self.canvas.grid(row=1, column=0, sticky=W)

    def create_widgets(self):
        self.create_title()
        # self.create_subtitle()
        # self.create_youtube_button()
        self.create_image()
        self.create_boutton()

    def create_image(self):
        # creation d'image
        self.width = 400
        self.height = 400
        self.image = PhotoImage(file="pok.png").subsample(6)  # .zoom(1)
        self.canvas = Canvas(self.frame, width=self.width, height=self.height, bg='#4065A4', bd=0, highlightthickness=0)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.image)

    def create_title(self):
        self.label_title = Label(self.frame, text="Bienvenue dans le jeu Pokemon", font=("Courrier", 30), bg='#4065A4',
                                 fg='white')
        self.label_title.grid(row=0, column=0, sticky=W)

    def create_boutton(self):
        self.boutton = Button(self.frame, text="Jouer", font=("Courrier", 15), bg='#4065A4',
                              fg='white', command=""Main"".start)
        self.boutton.grid(row=1, column=1, sticky=E)


# afficher
app = application()
app.window.mainloop()
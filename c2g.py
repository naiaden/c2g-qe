import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.font as tkFont

from PIL import ImageTk, Image

class App:
    def __init__(self, root):
        
        #setting title
        root.title("undefined")
        #setting window size
        width=773
        height=626
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.btn_select_front=tk.Button(root)
        self.btn_select_front["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.btn_select_front["font"] = ft
        self.btn_select_front["fg"] = "#000000"
        self.btn_select_front["justify"] = "center"
        self.btn_select_front["text"] = "Bestand selecteren"
        self.btn_select_front.place(x=50,y=200,width=70,height=25)
        self.btn_select_front["command"] = self.hndlr_select_front

        self.lbl_select_front=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl_select_front["font"] = ft
        self.lbl_select_front["fg"] = "#333333"
        self.lbl_select_front["justify"] = "center"
        self.lbl_select_front["text"] = "Voorkant"
        self.lbl_select_front.place(x=40,y=70,width=70,height=25)

        self.lbl_select_back=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl_select_back["font"] = ft
        self.lbl_select_back["fg"] = "#333333"
        self.lbl_select_back["justify"] = "center"
        self.lbl_select_back["text"] = "Achterkant"
        self.lbl_select_back.place(x=50,y=170,width=70,height=25)

        self.btn_select_back=tk.Button(root)
        self.btn_select_back["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.btn_select_back["font"] = ft
        self.btn_select_back["fg"] = "#000000"
        self.btn_select_back["justify"] = "center"
        self.btn_select_back["text"] = "Bestand selecteren"
        self.btn_select_back.place(x=40,y=100,width=129,height=30)
        self.btn_select_back["command"] = self.hndlr_select_back

        self.lbl_back_file=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl_back_file["font"] = ft
        self.lbl_back_file["fg"] = "#333333"
        self.lbl_back_file["justify"] = "center"
        self.lbl_back_file["text"] = "Kies een voorkant"
        self.lbl_back_file.place(x=40,y=140,width=128,height=30)

        self.lbl_front_file=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl_front_file["font"] = ft
        self.lbl_front_file["fg"] = "#333333"
        self.lbl_front_file["justify"] = "center"
        self.lbl_front_file["text"] = "Kies een achterkant"
        self.lbl_front_file.place(x=40,y=240,width=125,height=30)

        self.img_front_file=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.img_front_file["font"] = ft
        self.img_front_file["fg"] = "#333333"
        self.img_front_file["justify"] = "center"
        self.img_front_file["text"] = "label"
        self.img_front_file.place(x=20,y=320,width=208,height=242)

        self.img_back_file=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.img_back_file["font"] = ft
        self.img_back_file["fg"] = "#333333"
        self.img_back_file["justify"] = "center"
        self.img_back_file["text"] = "label"
        self.img_back_file.place(x=260,y=320,width=181,height=234)

        self.btn_process_imgs=tk.Button(root)
        self.btn_process_imgs["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.btn_process_imgs["font"] = ft
        self.btn_process_imgs["fg"] = "#000000"
        self.btn_process_imgs["justify"] = "center"
        self.btn_process_imgs["text"] = "Verwerken"
        self.btn_process_imgs.place(x=270,y=110,width=89,height=35)
        self.btn_process_imgs["command"] = self.hndlr_process_images

        self.lbl_process_imgs=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.lbl_process_imgs["font"] = ft
        self.lbl_process_imgs["fg"] = "#333333"
        self.lbl_process_imgs["justify"] = "center"
        self.lbl_process_imgs["text"] = "label"
        self.lbl_process_imgs.place(x=240,y=170,width=145,height=140)

        GLineEdit_162=tk.Entry(root)
        GLineEdit_162["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_162["font"] = ft
        GLineEdit_162["fg"] = "#333333"
        GLineEdit_162["justify"] = "center"
        GLineEdit_162["text"] = "mezelf"
        GLineEdit_162.place(x=480,y=90,width=154,height=30)

        GLabel_170=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_170["font"] = ft
        GLabel_170["fg"] = "#333333"
        GLabel_170["justify"] = "center"
        GLabel_170["text"] = "Ik heb vertrouwen in"
        GLabel_170.place(x=480,y=50,width=171,height=34)

        GLabel_307=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_307["font"] = ft
        GLabel_307["fg"] = "#333333"
        GLabel_307["justify"] = "center"
        GLabel_307["text"] = "Ik ga door met de spaarkring"
        GLabel_307.place(x=500,y=150,width=168,height=30)

        GLineEdit_154=tk.Entry(root)
        GLineEdit_154["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_154["font"] = ft
        GLineEdit_154["fg"] = "#333333"
        GLineEdit_154["justify"] = "center"
        GLineEdit_154["text"] = "Ja"
        GLineEdit_154.place(x=500,y=200,width=70,height=25)

        GLabel_890=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_890["font"] = ft
        GLabel_890["fg"] = "#333333"
        GLabel_890["justify"] = "center"
        GLabel_890["text"] = "Groep"
        GLabel_890.place(x=490,y=260,width=70,height=25)

        GListBox_162=tk.Entry(root)
        GListBox_162["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_162["font"] = ft
        GListBox_162["fg"] = "#333333"
        GListBox_162["justify"] = "center"
        GListBox_162["text"] = "AL321"
        GListBox_162.place(x=490,y=310,width=80,height=25)

        GButton_642=tk.Button(root)
        GButton_642["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_642["font"] = ft
        GButton_642["fg"] = "#000000"
        GButton_642["justify"] = "center"
        GButton_642["text"] = "Antwoorden overnemen"
        GButton_642.place(x=490,y=400,width=145,height=30)
        #GButton_642["command"] = self.GButton_642_command

        GButton_562=tk.Button(root)
        GButton_562["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_562["font"] = ft
        GButton_562["fg"] = "#000000"
        GButton_562["justify"] = "center"
        GButton_562["text"] = "Opslaan"
        GButton_562.place(x=490,y=460,width=70,height=25)
        #GButton_562["command"] = self.GButton_562_command


    def hndlr_select_front(self):
        filename = askopenfilename()
        self.lbl_front_file["text"] = f"Voorkant gekozen: {filename}"
        image1 = Image.open(filename).resize((234, 181), Image.Resampling.LANCZOS)
        self.image2 = ImageTk.PhotoImage(image1)
        self.img_front_file.configure(image=self.image2)
        self.img_front_file.image=self.image2


    def hndlr_select_back(self):
        filename = askopenfilename()
        self.lbl_back_file["text"] = f"Achterkant gekozen: {filename}"
        image1 = Image.open(filename).resize((234, 181), Image.Resampling.LANCZOS)
        self.image2 = ImageTk.PhotoImage(image1)
        self.img_back_file.configure(image=self.image2)
        self.img_back_file.image=self.image2

    def hndlr_process_images(self):
        text = ""

        # processing file transformation
        text += "Transformeren van afbeelding\n"
        self.lbl_process_imgs["text"] = text

        text += "Detecteren antwoorden\n"
        self.lbl_process_imgs["text"] = text

        text += "Verwerken van antwoorden\n"
        self.lbl_process_imgs["text"] = text
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

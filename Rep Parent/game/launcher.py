import tkinter as tk
#from PIL import Image, Imagetk
from config import LAUNCHER_SIZE, LAUNCHER_TITLE, LAUNCHER_ICON


class GameLauncher():
    def __init__(self, master):
        self.root = master
        self.root.geometry(LAUNCHER_SIZE)
        #self.frame = tk.Frame(root, width=LAUNCHER_WIDTH, height=LAUNCHER_HEIGHT)
        #self.frame.pack_propagate(0)  # Empêche la redimension automatique du cadre
        #self.frame.pack()
        self.root.title(LAUNCHER_TITLE)
        #img = Imagetk.PhotoImage(Image.open("./ressources/images/icon.png").resize((24, 24)))
        #self.root.iconphoto(False, img)
        
        self.root.iconbitmap(LAUNCHER_ICON)

        # Configurer la grille principale
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.rowconfigure(0, weight=80)
        self.root.rowconfigure(1, weight=20)

        # Frame principale
        self.config_frame = tk.Frame(self.root, background="gray40")
        self.config_frame.grid(row=0, column=1, sticky="nsew",rowspan=2)

        self.config_frame.columnconfigure(0, weight=1)
        self.config_frame.rowconfigure(0, weight=1)
        self.config_frame.rowconfigure(1, weight=500)

        # Menu (boutons)
        self.menu_frame = tk.Frame(self.config_frame, background="gray30")
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        self.menu_frame.columnconfigure(0, weight=1)

        # Zone de contenu
        self.content_frame = tk.Frame(self.config_frame, background="gray50")
        self.content_frame.grid(row=1, column=0, sticky="nsew")

        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.columnconfigure(1, weight=4)

        self.content_frame.rowconfigure(0, weight=1)
        
            # Boutons du menu
        for i, (text, command) in enumerate([("Profil", self.show_pro_content),
                                            ("Video", self.show_video_content),
                                            ("Audio", self.show_audio_content), 
                                            ("Admin", self.show_admin_content)]):
            btn = tk.Button(self.menu_frame, text=text, command=lambda c=command: self.show_content(c), bg="gray54",relief="flat")
            btn.grid(row=0, column=i, sticky="nsew")

            self.menu_frame.columnconfigure(i, weight=1)

        # Bouton de démarrage
        start_btn = tk.Button(self.root, text="Start", command=self.start_game)
        start_btn.grid(row=1, column=0, sticky="nsew")



        # self.start_button = tk.Button(self.frame, text="Start", command=self.start_game)
        # self.start_button.pack(expand=True)
        self.callback = None

    def set_start_callback(self, callback):
        # Definir la fonction à appeler lorsque start_game est appelée
        self.callback = callback

    def start_game(self):
        # Ferme la fenêtre du launcher
        for widget in self.root.winfo_children():
            widget.destroy()
        
        if self.callback:
            self.callback()


    def show_content(self,content_func):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        content_func()

    # Fonctions pour chaque menu
    def show_pro_content(self):
        #tk.Label(self.content_frame, text="Profil settings", bg="gray50").grid(row=0, column=0)
        pro_content_L = tk.Frame(self.content_frame,bg="gray54")
        pro_content_L.grid(column=0,row=0,sticky="nsew")
       
       

        new_pro = tk.Label(pro_content_L,background="gray40",text="New Profil")
        new_pro.pack()
        #profils = db.get_all_profils()
        #for profil in profils:
        #   profil = tk.Label(pro_content_L,background="gray40",text=profil)
        #   profil.pack(expand=True,side="top")
       

        pro = tk.Frame(self.content_frame,background="gray50")
        pro_txt = tk.Label(pro, text="Profil",background="gray50")
        # pro_txt.grid(column=0,row=0)
        pro.grid()

        ##Profil expanding Menu
        pro_default = tk.StringVar(pro)
        pro_default.set("New Profil")
        pro_options = ["Profil 1", "Profil 2","New Profil"]
        pro_expanding = tk.OptionMenu(pro, pro_default, *pro_options)
        # pro_expanding.grid(column=1,row=0)




    def show_video_content(self):
        # tk.Label(self.content_frame, text="Video settings", bg="gray50").grid(row=0, column=0)

        rez =tk.Frame(self.content_frame,bg="lightblue")
        rez_txt = tk.Label(rez,text="Resolution")
        rez_default = tk. StringVar(rez)
        rez_default.set("600")

        rez_options = ["400","600","800"]
        rez_expanding = tk.OptionMenu(rez, rez_default, *rez_options)

        rez_txt.grid(column=0,row=0)
        rez_expanding.grid(column=1,row=0)
        rez.grid()

        qual = tk.Frame(self.content_frame, bg="lightblue")
        qual_txt = tk.Label(qual,text="Qualité")
        qual_txt.grid(column=0,row=0)
        qual.grid()
        qual_var = tk.StringVar()
        qual_var.set("H") # Default value
        qual_selectionH = tk.Radiobutton(qual, text="High", variable=qual_var, value="H")
        qual_selectionL = tk.Radiobutton(qual, text="Low", variable=qual_var, value="L")

        qual_txt.grid(column=0,row=0)
        qual_selectionH.grid(column=1,row=0)
        qual_selectionL.grid(column=2,row=0)


    def show_audio_content(self):
        tk.Label(self.content_frame, text="Audio settings", bg="gray50").grid(row=0, column=0)

    def show_admin_content(self):
        tk.Label(self.content_frame, text="Admin settings", bg="gray50").grid(row=0, column=0)


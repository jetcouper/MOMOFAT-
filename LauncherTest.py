import tkinter as TK

root = TK.Tk()
root.title("TD Launcher")
root.geometry("600x400")

# Configurer la grille principale
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=80)
root.rowconfigure(1, weight=20)

# Frame principale
config_frame = TK.Frame(root, background="gray40")
config_frame.grid(row=0, column=1, sticky="nsew",rowspan=2)

config_frame.columnconfigure(0, weight=1)
config_frame.rowconfigure(0, weight=1)
config_frame.rowconfigure(1, weight=500)

# Menu (boutons)
menu_frame = TK.Frame(config_frame, background="gray30")
menu_frame.grid(row=0, column=0, sticky="nsew")

menu_frame.columnconfigure(0, weight=1)

# Zone de contenu
content_frame = TK.Frame(config_frame, background="gray50")
content_frame.grid(row=1, column=0, sticky="nsew")

content_frame.columnconfigure(0, weight=1)
content_frame.rowconfigure(0, weight=1)

# Fonction pour afficher du contenu
def show_content(content_func):
    for widget in content_frame.winfo_children():
        widget.destroy()
    content_func()

# Fonctions pour chaque menu
def show_pro_content():
    #TK.Label(content_frame, text="Profil settings", bg="gray50").grid(row=0, column=0)

    pro = TK.Frame(content_frame)
    pro_txt = TK.Label(pro, text="Profile")
    pro_txt.grid(column=0,row=0)
    pro.grid()

    ##Profil expanding Menu
    pro_default = TK.StringVar(pro)
    pro_default.set("New Profil")
    pro_options = ["Profil 1", "Profil 2","New Profil"]
    pro_expanding = TK.OptionMenu(pro, pro_default, *pro_options)
    pro_expanding.grid(column=1,row=0)




def show_video_content():
    # TK.Label(content_frame, text="Video settings", bg="gray50").grid(row=0, column=0)

    rez =TK.Frame(content_frame,bg="lightblue")
    rez_txt = TK.Label(rez,text="Resolution")
    rez_default = TK. StringVar(rez)
    rez_default.set("600")

    rez_options = ["400","600","800"]
    rez_expanding = TK.OptionMenu(rez, rez_default, *rez_options)

    rez_txt.grid(column=0,row=0)
    rez_expanding.grid(column=1,row=0)
    rez.grid()

    qual = TK.Frame(content_frame, bg="lightblue")
    qual_txt = TK.Label(qual,text="Qualité")
    qual_txt.grid(column=0,row=0)
    qual.grid()
    qual_var = TK.StringVar()
    qual_var.set("H") # Default value
    qual_selectionH = TK.Radiobutton(qual, text="High", variable=qual_var, value="H")
    qual_selectionL = TK.Radiobutton(qual, text="Low", variable=qual_var, value="L")

    qual_txt.grid(column=0,row=0)
    qual_selectionH.grid(column=1,row=0)
    qual_selectionL.grid(column=2,row=0)


def show_audio_content():
    TK.Label(content_frame, text="Audio settings", bg="gray50").grid(row=0, column=0)

def show_admin_content():
    TK.Label(content_frame, text="Admin settings", bg="gray50").grid(row=0, column=0)

# Boutons du menu
for i, (text, command) in enumerate([("Profil", show_pro_content), 
                                     ("Video", show_video_content),
                                     ("Audio", show_audio_content), 
                                     ("Admin", show_admin_content)]):
    btn = TK.Button(menu_frame, text=text, command=lambda c=command: show_content(c), bg="gray54",relief="flat")
    btn.grid(row=0, column=i, sticky="nsew")

    menu_frame.columnconfigure(i, weight=1)

# Bouton de démarrage
start_btn = TK.Button(root, text="Start", command=lambda: show_content(show_pro_content))
start_btn.grid(row=1, column=0, sticky="nsew")

TK.mainloop()

import tkinter as TK

root = TK.Tk()
root.title("TD Launcher")
root.geometry("600x400")

# Configurer la grille principale
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=1)

# Frame principale
config_frame = TK.Frame(root, background="gray40")
config_frame.grid(row=0, column=1, sticky="nsew")

config_frame.columnconfigure(0, weight=1)
config_frame.rowconfigure(0, weight=1)
config_frame.rowconfigure(1, weight=5)

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
    TK.Label(content_frame, text="Profil settings", bg="gray50").grid(row=0, column=0)

def show_video_content():
    TK.Label(content_frame, text="Video settings", bg="gray50").grid(row=0, column=0)

def show_audio_content():
    TK.Label(content_frame, text="Audio settings", bg="gray50").grid(row=0, column=0)

def show_admin_content():
    TK.Label(content_frame, text="Admin settings", bg="gray50").grid(row=0, column=0)

# Boutons du menu
for i, (text, command) in enumerate([("Profil", show_pro_content), 
                                     ("Video", show_video_content),
                                     ("Audio", show_audio_content), 
                                     ("Admin", show_admin_content)]):
    btn = TK.Button(menu_frame, text=text, command=lambda c=command: show_content(c), bg="gray54")
    btn.grid(row=0, column=i, sticky="nsew")

    menu_frame.columnconfigure(i, weight=1)

# Bouton de démarrage
start_btn = TK.Button(root, text="Start", command=lambda: show_content(show_pro_content))
start_btn.grid(row=0, column=0, sticky="nsew")

TK.mainloop()

import tkinter as TK
#import test2  # On assume que test2.py est dans le même répertoire que ce script.


root = TK.Tk()
root.title("TD Launcher")

root.geometry("500x500")

def start_game():
    root.destroy()
    # Appelle une fonction de test2 si nécessaire.
    # test2.currentGame(rez_var)  # Si tu as besoin de passer des variables, ajuste cette ligne.

# Frames
config_frame = TK.Frame(root,background="gray40")
start_frame = TK.Frame(root)
animation_frame = TK.Frame(root)

animation_frame.grid(row=0, column=0, sticky="nsew")
start_frame.grid(row=1, column=0, sticky="nsew")
config_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")

config_frame.columnconfigure(0,weight=1)
config_frame.columnconfigure(1,weight=1)
config_frame.columnconfigure(2,weight=1)
config_frame.columnconfigure(3,weight=1)
config_frame.rowconfigure(0, weight=1)
config_frame.rowconfigure(1, weight=100)
config_frame.grid_propagate(False)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)

config_content = TK.Frame()

#### Config Actions
def show_pro_content():
    print("Profil")
    delete_config()
    set_config()
    set_video_info()
    
    

def show_video_content():
    print("Video")
    

def show_audio_content():
    print("Audio")
    

def show_admin_content():
    print("Admin")

####

def delete_config():
    for child in config_frame.winfo_children():
            child.destroy()


############### Config widget
### Config frame management

def set_config():
    

    config_content = TK.Frame(config_frame,background="gray50")

    widget_pro   = TK.Frame(config_frame,background="gray54")
    widget_video = TK.Frame(config_frame,background="gray54")
    widget_audio = TK.Frame(config_frame,background="gray54")
    widget_admin = TK.Frame(config_frame,background="gray54")



    widget_pro.grid(row=0, column=0, sticky="nsew")
    widget_video.grid(row=0, column=1, sticky="nsew")
    widget_audio.grid(row=0, column=2, sticky="nsew")
    widget_admin.grid(row=0, column=3, sticky="nsew")

    widget_pro.grid_propagate(False)
    widget_video.grid_propagate(False)
    widget_audio.grid_propagate(False)
    widget_admin.grid_propagate(False)

    config_content.grid(column=0,row=0, columnspan= 4, rowspan=5, sticky="nsew")


    title_pro = TK.Label(widget_pro,text="Profil",background="gray54")
    title_video = TK.Label(widget_video,text="Video",background="gray54")
    title_audio = TK.Label(widget_audio,text="Audio",background="gray54")
    title_admin = TK.Label(widget_admin,text="Admin",background="gray54")

    title_pro.pack( side="bottom",expand=True)
    title_video.pack(side="bottom",expand=True)
    title_audio.pack(side="bottom",expand=True)
    title_admin.pack(side="bottom",expand=True)
    
    widget_pro.bind("<Button-1>",lambda e:show_pro_content())  
    widget_video.bind("<Button-1>",lambda e:show_video_content())  
    widget_audio.bind("<Button-1>",lambda e:show_audio_content())  
    widget_admin.bind("<Button-1>",lambda e:show_admin_content())  
    
    title_pro.bind("<Button-1>",lambda e:show_pro_content())  
    title_video.bind("<Button-1>",lambda e:show_video_content())  
    title_audio.bind("<Button-1>",lambda e:show_audio_content())  
    title_admin.bind("<Button-1>",lambda e:show_admin_content())  
    return config_content
###

####Events
def set_video_info():
    vid_qual = TK.Frame(config_content)
    vid_label1 = TK.Label(vid_qual, text="Qualité vidéo : ")
    vid_label1.grid(column=0,row=0)
    vid_qual.pack()
    print("Printing video screen")
    



####



###############

# Start
#start_btn = TK.Button(start_frame, text="Start", command=start_game)
start_btn = TK.Button(start_frame, text="Start", command=set_config)
start_btn.pack()


TK.mainloop()

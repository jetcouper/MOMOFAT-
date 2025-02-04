import tkinter as TK
#from test2 import currentGame


root = TK.Tk()
root.title("TD Launcher")

root.geometry("250x250")

def start_game():
    root.destroy()
    #currentGame(rez_var)
    import test2
    #exec("test2.py")
    


#Profile
pro = TK.Frame(root)
pro_txt = TK.Label(pro, text="Profile")
pro_txt.grid(column=0,row=0)
pro.pack( expand=True, pady=10)

##Profil expanding Menu
pro_default = TK.StringVar(pro)
pro_default.set("New Profil")
pro_options = ["Profil 1", "Profil 2"]
pro_expanding = TK.OptionMenu(pro, pro_default, *pro_options)
pro_expanding.grid(column=1,row=0)


#Resolution
rez =TK.Frame(root,bg="lightblue")
rez_txt = TK.Label(rez,text="Resolution")
rez_default = TK. StringVar(rez)
rez_default.set("600")

rez_options = ["400","600","800"]
rez_expanding = TK.OptionMenu(rez, rez_default, *rez_options)

rez_txt.grid(column=0,row=0)
rez_expanding.grid(column=1,row=0)
rez.pack( expand=True, pady=10)

#Qualité
qual = TK.Frame(root, bg="lightblue")
qual_txt = TK.Label(qual,text="Qualité")
qual_txt.grid(column=0,row=0)
qual.pack( expand=True, pady=10)
qual_var = TK.StringVar()
qual_selectionH = TK.Radiobutton(qual, text="High", variable=qual_var, value="H")
qual_selectionL = TK.Radiobutton(qual, text="Low", variable=qual_var, value="L")

qual_txt.grid(column=0,row=0)
qual_selectionH.grid(column=1,row=0)
qual_selectionL.grid(column=2,row=0)

#Start
start_btn = TK.Button(root,text="Start", command=start_game)
start_btn.pack()





TK.mainloop()
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
pro_txt.pack()
pro.pack( expand=True, pady=10)


#Resolution
rez_var = 400

rez =TK.Frame(root,bg="lightblue")
rez_txt = TK.Label(rez,text="Resolution")
rez_4 = TK.Radiobutton(rez, text="400",variable=rez_var, value=400)
rez_6 = TK.Radiobutton(rez, text="600",variable=rez_var, value=600)
rez_8 = TK.Radiobutton(rez, text="800",variable=rez_var, value=800)
rez_4.pack()
rez_6.pack()
rez_8.pack()


rez_txt.pack()
rez.pack( expand=True, pady=10)

#Qualité
qual = TK.Frame(root, bg="lightblue")
qual_txt = TK.Label(root,text="Qualité")
qual_txt.pack()
qual.pack( expand=True, pady=10)

#Start
start_btn = TK.Button(root,text="Start", command=start_game)
start_btn.pack()





TK.mainloop()
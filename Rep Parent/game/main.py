import tkinter as tk
import launcher
import controller
# from game import launcher
# from game import controller

if __name__ == "__main__":
    root = tk.Tk()
    # Afficher le launcher
    launcher_instance = launcher.GameLauncher(root)
    
    def start_game():
        # creation du controlleur du jeu
        game_controller = controller.Controller(root)
        

    launcher_instance.set_start_callback(start_game)
    root.mainloop()


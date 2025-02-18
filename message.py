import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json

TILE_SIZE = 32  # Size of each tile in the tileset
ISO_WIDTH = 32  # Width of isometric tile
ISO_HEIGHT = 16  # Height of isometric tile
MAP_WIDTH = 50   # Map width in tiles
MAP_HEIGHT = 50  # Map height in tiles

class IsoMapMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Isometric Map Maker")

        # Canvas for the map
        self.canvas = tk.Canvas(root, width=MAP_WIDTH * ISO_WIDTH, height=MAP_HEIGHT * ISO_HEIGHT, bg='white')
        self.canvas.pack(side=tk.LEFT)
        self.canvas.bind("<Button-1>", self.place_tile)

        # Panel for tileset selection
        self.tileset_canvas = tk.Canvas(root, width=256, height=256)
        self.tileset_canvas.pack()
        self.tileset_canvas.bind("<Button-1>", self.select_tile)

        # Buttons
        self.load_tileset_button = tk.Button(root, text="Load Tileset", command=self.load_tileset)
        self.load_tileset_button.pack()
        self.save_button = tk.Button(root, text="Save Map", command=self.save_map)
        self.save_button.pack()
        self.load_button = tk.Button(root, text="Load Map", command=self.load_map)
        self.load_button.pack()

        self.tileset_image = None
        self.selected_tile = None
        self.map_data = []  # Stores tile placements
        self.tile_images = {}  # Store references to tile images
    
    def load_tileset(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            return
        self.tileset_image = Image.open(file_path)
        self.tileset_tk = ImageTk.PhotoImage(self.tileset_image)
        self.tileset_canvas.create_image(0, 0, anchor=tk.NW, image=self.tileset_tk)

    def select_tile(self, event):
        if not self.tileset_image:
            return
        x, y = event.x // TILE_SIZE, event.y // TILE_SIZE
        self.selected_tile = (x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE)

    def place_tile(self, event):
        if not self.tileset_image or not self.selected_tile:
            return
        
        # Adjust for correct cursor alignment
        x_offset = (MAP_WIDTH * ISO_WIDTH) // 2
        col = ((event.x - x_offset) // (ISO_WIDTH // 2) + event.y // (ISO_HEIGHT // 2)) // 2
        row = ((event.y // (ISO_HEIGHT // 2)) - (event.x - x_offset) // (ISO_WIDTH // 2)) // 2
        
        iso_x = (col - row) * (ISO_WIDTH // 2) + x_offset
        iso_y = (col + row) * (ISO_HEIGHT // 2)
        
        tile = self.tileset_image.crop(self.selected_tile)
        tile_tk = ImageTk.PhotoImage(tile)
        
        tile_id = self.canvas.create_image(iso_x, iso_y, anchor=tk.NW, image=tile_tk)
        self.tile_images[tile_id] = tile_tk  # Store reference to prevent garbage collection
        
        self.map_data.append({"col": col, "row": row, "tile": list(self.selected_tile)})  # Convert tuple to list for JSON

    def save_map(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, "w") as f:
                json.dump(self.map_data, f, indent=4)
            messagebox.showinfo("Save Map", "Map saved successfully!")
    
    def load_map(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, "r") as f:
                self.map_data = json.load(f)
            self.redraw_map()
    
    def redraw_map(self):
        if not self.tileset_image:
            messagebox.showerror("Error", "Load a tileset first!")
            return
        
        self.canvas.delete("all")
        self.tile_images.clear()  # Clear stored references
        for tile_entry in self.map_data:
            col, row, tile_coords = tile_entry["col"], tile_entry["row"], tile_entry["tile"]
            iso_x = (col - row) * (ISO_WIDTH // 2) + (MAP_WIDTH * ISO_WIDTH // 2)
            iso_y = (col + row) * (ISO_HEIGHT // 2)
            
            tile = self.tileset_image.crop(tuple(tile_coords))  # Convert list back to tuple
            tile_tk = ImageTk.PhotoImage(tile)
            tile_id = self.canvas.create_image(iso_x, iso_y, anchor=tk.NW, image=tile_tk)
            self.tile_images[tile_id] = tile_tk  # Store reference to prevent garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = IsoMapMaker(root)
    root.mainloop()

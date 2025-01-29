import tkinter as TK
import random



split = 50  # Number of tiles in rows/cols
cs = 700  # Window size
cursor_size = 3  # Defines the size of the hovered area

class currentGame:
    def __init__(self, rez, qual, lang, profile):
        cs = rez

cl = []  # Stores all grid tiles

root = TK.Tk()
root.geometry(f"{cs}x{cs}")

root.update_idletasks()

# Get updated tile width and height
cwidth = root.winfo_width() // split
cheight = root.winfo_height() // split

print(cwidth, cheight)

canvas = TK.Canvas(root, width=root.winfo_width(), height=root.winfo_height())
canvas.pack()

class Case:
    def __init__(self, x, y, offsetx, offsety, row, col) -> None:
        self.x = x
        self.y = y
        self.x2 = x + offsetx
        self.y2 = y + offsety
        self.row = row
        self.col = col
        self.isBlocked = random.random() < 0.01  # 1% chance of being initially blocked
        self.isPermanent = False  # Track whether it's a placed tile
        self.color = "white"
        
        # Draw the rectangle
        self.rect_id = canvas.create_rectangle(self.x, self.y, self.x2, self.y2, fill=self.color, outline="black")
        
        # Bind mouse events
        canvas.tag_bind(self.rect_id, "<Enter>", self.on_hover)
        canvas.tag_bind(self.rect_id, "<Leave>", self.on_leave)
        canvas.tag_bind(self.rect_id, "<Button-1>", self.on_click)  # Left-click to place tile
        canvas.tag_bind(self.rect_id, "<Button-3>", self.on_drop_tileset)  # Right-click to drop tileset (block area)

    def on_hover(self, event):
        """Highlight the hovered tile and its surrounding tiles."""
        highlight_area(self.row, self.col)

    def on_leave(self, event):
        """Reset tiles back to their proper color when leaving."""
        reset_hovered_tiles()

    def on_click(self, event):
        """Attempt to place the tiles permanently."""
        place_tiles_if_possible(self.row, self.col)

    def on_drop_tileset(self, event):
        """Blocks the hovered area, making it non-placeable."""
        block_area(self.row, self.col)

# Function to highlight hovered area
def highlight_area(row, col):
    """Highlights a (cursor_size x cursor_size) area around the hovered tile."""
    hovering_blue = any(case.isPermanent for case in cl if abs(case.row - row) < cursor_size // 2 + 1 and abs(case.col - col) < cursor_size // 2 + 1)

    for case in cl:
        if abs(case.row - row) < cursor_size // 2 + 1 and abs(case.col - col) < cursor_size // 2 + 1:
            if case.isBlocked:
                canvas.itemconfig(case.rect_id, fill="red")  # Blocked tile is red
            elif case.isPermanent or hovering_blue:
                canvas.itemconfig(case.rect_id, fill="red")  # Hovering over blue tiles = red tiles
            else:
                canvas.itemconfig(case.rect_id, fill="green")  # Free tile is green

# Function to reset tiles after hover leaves
def reset_hovered_tiles():
    """Resets tiles back to white or blue after hover leaves."""
    for case in cl:
        if case.isPermanent:
            canvas.itemconfig(case.rect_id, fill="blue")  # Keep placed tiles blue
        elif not case.isBlocked:
            canvas.itemconfig(case.rect_id, fill="white")  # Reset unblocked tiles to white

# Function to check and place blue tiles
def place_tiles_if_possible(row, col):
    """If all hovered tiles are free, make them permanently blue."""
    affected_tiles = [case for case in cl if abs(case.row - row) < cursor_size // 2 + 1 and abs(case.col - col) < cursor_size // 2 + 1]
    
    # Check if any tile is blocked or already placed
    if any(case.isBlocked or case.isPermanent for case in affected_tiles):
        return  # Prevent placing if any tile is blocked or already placed

    # If all are free, make them permanent
    for case in affected_tiles:
        case.isPermanent = True
        canvas.itemconfig(case.rect_id, fill="blue")  # Lock in the blue color

# Function to drop a tileset (block an area)
def block_area(row, col):
    """Blocks a cursor_size x cursor_size area."""
    affected_tiles = [case for case in cl if abs(case.row - row) < cursor_size // 2 + 1 and abs(case.col - col) < cursor_size // 2 + 1]
    
    # Mark all tiles in this area as blocked
    for case in affected_tiles:
        case.isBlocked = True
        canvas.itemconfig(case.rect_id, fill="gray")  # Mark blocked tiles in gray

# Creating grid tiles
for y in range(split):
    for x in range(split):
        cl.append(Case(x * cwidth, y * cheight, cwidth, cheight, y, x))

root.mainloop()

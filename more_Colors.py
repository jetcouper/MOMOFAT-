def adjust_color(color, factor):
    """
    Ajuste la luminosité d'une couleur en fonction du facteur.
    :param color: Couleur en format hexadécimal (#RRGGBB)
    :param factor: Facteur d'ajustement (positif pour éclaircir, négatif pour assombrir)
    :return: Nouvelle couleur ajustée en format hexadécimal
    """
    # Enlever le caractère "#" au début de la couleur hexadécimale
    color = color.lstrip('#')

    # Découper la couleur en ses composantes RGB
    r, g, b = [int(color[i:i+2], 16) for i in (0, 2, 4)]

    # Appliquer l'ajustement
    r = max(0, min(255, int(r * (1 + factor))))
    g = max(0, min(255, int(g * (1 + factor))))
    b = max(0, min(255, int(b * (1 + factor))))
    
    return f'#{r:02x}{g:02x}{b:02x}'

Colors = {}

Colors['widget_default'] = 737373
Colors['widget_selected'] = 999999
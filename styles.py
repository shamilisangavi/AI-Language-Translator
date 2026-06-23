from tkinter import ttk

# Colors
BG_COLOR = "#0f172a"
FRAME_COLOR = "#1e293b"
TEXTBOX_COLOR = "#334155"
TEXT_COLOR = "#ffffff"

# Fonts
TITLE_FONT = ("Segoe UI", 24, "bold")
TEXT_FONT = ("Segoe UI", 12)

def apply_styles(root):
    style = ttk.Style(root)

    try:
        style.theme_use("clam")
    except:
        pass

    style.configure(
        "TCombobox",
        padding=5
    )
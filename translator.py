from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from styles import *
import pyttsx3
import threading
from gtts import gTTS
import os
from playsound import playsound

# -------------------------
# Language Codes
# -------------------------

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN"
}

# -------------------------
# Functions
# -------------------------

def translate_text():
    try:
        text = input_text.get("1.0", END).strip()

        if not text:
            messagebox.showwarning(
                "Warning",
                "Please enter some text!"
            )
            return

        source_code = languages[source_lang.get()]
        target_code = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source_code,
            target=target_code
        ).translate(text)

        output_text.config(state="normal")
        output_text.delete("1.0", END)
        output_text.insert("1.0", translated)
        output_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


def clear_text():
    input_text.delete("1.0", END)

    output_text.config(state="normal")
    output_text.delete("1.0", END)
    output_text.config(state="disabled")

def copy_translation():
    translated_text = output_text.get("1.0", END).strip()

    if translated_text:
        root.clipboard_clear()
        root.clipboard_append(translated_text)

        messagebox.showinfo(
            "Copied",
            "Translation copied successfully!"
        )
def speak_translation():
    print("Speak button clicked")
    text = output_text.get("1.0", "end-1c").strip()

    if not text:
        return

    try:
        lang_map = {
            "English": "en",
            "Tamil": "ta",
            "Hindi": "hi",
            "French": "fr",
            "German": "de",
            "Spanish": "es",
            "Arabic": "ar",
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese": "zh-CN"
        }

        lang = lang_map.get(target_lang.get(), "en")

        tts = gTTS(text=text, lang=lang)
        tts.save("speech.mp3")
        print("MP3 saved")

        playsound("speech.mp3")

    except Exception as e:
        messagebox.showerror("Speech Error", str(e))

def swap_languages():
    src = source_lang.get()
    tgt = target_lang.get()

    if src != "Auto Detect":
        source_lang.set(tgt)
        target_lang.set(src)

# -------------------------
# Main Window
# -------------------------
engine = pyttsx3.init()
root = Tk()
root.title("AI Language Translator")
root.geometry("1200x750")
root.configure(bg=BG_COLOR)

apply_styles(root)

# -------------------------
# Header
# -------------------------

header = Label(
    root,
    text="🌍 AI Language Translator",
    font=TITLE_FONT,
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

header.pack(pady=20)

# -------------------------
# Language Selection
# -------------------------

lang_frame = Frame(root, bg=BG_COLOR)
lang_frame.pack(pady=10)

source_lang = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    width=20,
    state="readonly"
)

source_lang.current(1)
source_lang.grid(row=0, column=0, padx=15)

swap_btn = Button(
    lang_frame,
    text="⇄",
    bg="#f59e0b",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=4,
    command=swap_languages
)

swap_btn.grid(row=0, column=1, padx=10)

target_lang = ttk.Combobox(
    lang_frame,
    values=list(languages.keys())[1:],
    width=20,
    state="readonly"
)

target_lang.current(1)
target_lang.grid(row=0, column=2, padx=15)

# -------------------------
# Buttons
# -------------------------

button_frame = Frame(root, bg=BG_COLOR)
button_frame.pack(pady=15)

translate_btn = Button(
    button_frame,
    text="Translate",
    bg="#2563eb",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=8,
    command=translate_text
)

translate_btn.pack(side=LEFT, padx=10)

clear_btn = Button(
    button_frame,
    text="Clear",
    bg="#ef4444",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=8,
    command=clear_text
)

clear_btn.pack(side=LEFT, padx=10)

speak_btn = Button(
    button_frame,
    text="🔊 Speak",
    bg="#8b5cf6",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=8,
    command=speak_translation
)

speak_btn.pack(side=LEFT, padx=10)

copy_btn = Button(
    button_frame,
    text="📋 Copy",
    bg="#10b981",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=8,
    command=copy_translation
)

copy_btn.pack(side=LEFT, padx=10)

# -------------------------
# Main Translator Area
# -------------------------

main_frame = Frame(root, bg=BG_COLOR)
main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# -------------------------
# Input Panel
# -------------------------

left_frame = Frame(
    main_frame,
    bg=FRAME_COLOR
)

left_frame.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10
)

Label(
    left_frame,
    text="Input Text",
    bg=FRAME_COLOR,
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(
    anchor="w",
    padx=15,
    pady=10
)

input_text = Text(
    left_frame,
    bg=TEXTBOX_COLOR,
    fg="white",
    insertbackground="white",
    font=TEXT_FONT,
    relief="flat",
    wrap="word"
)

input_text.pack(
    fill=BOTH,
    expand=True,
    padx=15,
    pady=(0, 15)
)

# -------------------------
# Output Panel
# -------------------------

right_frame = Frame(
    main_frame,
    bg=FRAME_COLOR
)

right_frame.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=10
)

Label(
    right_frame,
    text="Translated Text",
    bg=FRAME_COLOR,
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(
    anchor="w",
    padx=15,
    pady=10
)

output_text = Text(
    right_frame,
    bg=TEXTBOX_COLOR,
    fg="white",
    insertbackground="white",
    font=TEXT_FONT,
    relief="flat",
    wrap="word",
    state="disabled"
)

output_text.pack(
    fill=BOTH,
    expand=True,
    padx=15,
    pady=(0, 15)
)

root.mainloop()
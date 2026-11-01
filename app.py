import os
import sys

import pygame


def resource_path(relative_path):
    """Mendapatkan absolute path ke resource, berfungsi saat dev, .exe, dan Android/APK."""
    try:
        # PyInstaller membuat folder temporary dan menyimpan path-nya di _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


# Ambatukam Virus

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Ambatukam Virus")

# Force can't shortcut
# (Pada Android/Windows modern, sebagian pintasan sistem tidak dapat diblokir sepenuhnya.)

# PERBAIKAN PATH: Dibungkus dengan resource_path() agar tidak error
audio_path = resource_path(os.path.join("sound", "sound.mp3"))
image_path = resource_path(os.path.join("images", "image.png"))

# load and display images
try:
    img = pygame.image.load(image_path)
    img = pygame.transform.smoothscale(img, (screen_width, screen_height))
except Exception as e:
    print(f"Gagal memuat gambar: {e}")
    img = None

# load and play sound
try:
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play(-1)
except Exception as e:
    print(f"Gagal memutar audio. Pastikan file berada di {audio_path}. Error: {e}")

clock = pygame.time.Clock()
running = True

# Main program
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Pertahankan perilaku asli yang memblokir pintasan tertentu.
            if event.key in (pygame.K_F11, pygame.K_ESCAPE):
                continue

    screen.fill((0, 0, 0))
    if img is not None:
        screen.blit(img, (0, 0))

    title_font = pygame.font.SysFont("Arial", 50, bold=True)
    title = title_font.render("Ambatukam Virus", True, (255, 0, 0))
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, 150))

    message_font = pygame.font.SysFont("Arial", 30)
    message_lines = [
        "Your computer has been infected with the Ambatukam Virus.",
        "Please don't turn off your computer. Your files will be encrypted",
        "Ambatukam!!!",
    ]
    for index, line in enumerate(message_lines):
        text = message_font.render(line, True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, 300 + index * 40))

    pygame.display.flip()
    clock.tick(30)

pygame.mixer.music.stop()
pygame.quit()
sys.exit()

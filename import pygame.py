import pygame
import time

# Initialize Pygame
pygame.mixer.init()

# Load the MP3 file
mp3_file = '/Users/anaritamoreirarangel/Documents/guanabara/serenity-waves.mp3'  # Full path

try:
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

    # Keep the program running while the music is playing
    while pygame.mixer.music.get_busy(): 
        time.sleep(1)

except pygame.error as e:
    print(f"An error occurred: {e}")

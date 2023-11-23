import pygame
import streamlit as st
import tempfile
import time


def play_audio(file_path):
    pygame.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Keep the program running while the audio plays
    while pygame.mixer.music.get_busy():
        time.sleep(1)


file = st.file_uploader("Upload File")

if file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name  # Store the path before closing
        # Process the temporary file
        st.write("Temporary file path:", temp_file_path)

    # Close the temporary file before passing its path to play_audio
    play_audio(temp_file_path)


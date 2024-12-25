import tkinter as tk
from tkinter import filedialog
import os
import shutil

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory()
    print(f"Selected folder: {folder_selected}")
    return folder_selected

def organize_images(folder_path):
    image_extensions = [
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.heic', '.avif'
    ]
    for root, _, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_path = os.path.join(root, file)
                image_folder = os.path.join(folder_path, os.path.splitext(file)[0])
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                new_image_path = os.path.join(image_folder, file)
                if not os.path.exists(new_image_path):
                    shutil.move(image_path, new_image_path)
                    print(f"Moved {file} to {image_folder}")

if __name__ == "__main__":
    folder_selected = select_folder()
    if folder_selected:
        organize_images(folder_selected)
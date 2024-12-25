import tkinter as tk
from tkinter import filedialog
import os

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory()
    print(f"Selected folder: {folder_selected}")
    return folder_selected

def organize_files(folder_path):
    image_extensions = [
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.heic', '.avif'
    ]
    video_extensions = [
        '.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.mpeg', '.mpg'
    ]
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if any(file.lower().endswith(ext) for ext in image_extensions + video_extensions):
                new_file_name = f"{os.path.basename(root)}_{file}"
                new_file_path = os.path.join(root, new_file_name)
                if not os.path.exists(new_file_path):
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {file} to {new_file_name}")

if __name__ == "__main__":
    folder_selected = select_folder()
    if folder_selected:
        organize_files(folder_selected)

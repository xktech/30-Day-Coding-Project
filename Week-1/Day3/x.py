# File organiser
# I have already one this project so technically i'm skipping it.

import watchdog
import json
import os
import shutil
import pathlib
import argparse
import logging

FOLDER = os.path.expanduser("~/Downloads")
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Documents": [".doc", ".docx", ".txt", ".xlsx", ".csv"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".cpp", ".c", ".tsx"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Applications": [".exe"],
    "Bedrock Packs": [".mcpack"],
    "Java Mods": [".jar"],
    "Java Mod Packs": [".mrpack"],
    "Disk Image": [".iso"],
    "Other": [".msi", ".msix", ".geode", ".avif"],
    "Windows": [".winmd"],
    "Cursors": [".cur"],
}


for filename in os.listdir(FOLDER):
    filepath = os.path.join(FOLDER, filename)

    # skip folders
    if os.path.isdir(filepath):
        continue

    ext = os.path.splitext(filename) [1].lower()
    moved = False

    for folder_name, extensions in FILE_TYPES.items():
        if ext in extensions:
            dest_folder = os.path.join(FOLDER, folder_name)
            os.makedirs(dest_folder, exist_ok=True) # creates folder if not already
            shutil.move(filepath, os.path.join(dest_folder, filename))
            print(f"Moved: {filename} -> {folder_name}/")
            moved = True
            break

    if moved:
        with open('logs.txt', "w") as f:
            f.write(f"{filename} -> {folder_name}\n")
            print(f"Moved {filename} -> {folder_name}")
    if not moved:
        print(f"Skipped: {filename}, (unknown type)")

print("\nDone!")
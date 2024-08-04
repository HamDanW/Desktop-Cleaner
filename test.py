import shutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

source_dir = r'C:\Users\ryanc\Downloads'
dest_dir_image = r'C:\Users\ryanc\Downloads\Downloaded Images'
dest_dir_pdf = r'C:\Users\ryanc\Downloads\Downloaded PDF'
dest_dir_videos = r'C:\Users\ryanc\Downloads\Downloaded Videos'
dest_dir_doc = r'C:\Users\ryanc\Downloads\Downloaded Docs'

document_extensions = [".doc", ".docx", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

pdf_extensions = [".pdf"]

def rename(dest, name):
    file_check = os.path.exists(dest + r'\\' + name)
    fname = os.path.splitext(name)
    counter = 1
    while(file_check):
        name = f"{fname[0]}({str(counter)}){fname[1]}"
        file_check = os.path.exists(dest + r'\\' + name)
        counter+=1
    return name

def move(dest, entry, name):
    file_check = os.path.exists(dest + r'\\' + name)
    if file_check:
        new_name = rename(dest, name)
        old = os.path.join(dest, name)
        new = os.path.join(dest, new_name)
        os.rename(old, new)
    shutil.move(entry,dest)

while(True):
    with os.scandir(source_dir) as entries:
        for entry in entries:
            fname = entry.name
            extension = '.'+fname.split('.')[-1].lower()
            dest = source_dir
            if extension in pdf_extensions:
                dest = dest_dir_pdf
                move(dest, entry, fname)
            elif extension in image_extensions:
                dest = dest_dir_image
                move(dest, entry, fname)
            elif extension in video_extensions:
                dest = dest_dir_videos
                move(dest, entry, fname)
            elif extension in document_extensions:
                dest = dest_dir_doc
                move(dest, entry, fname)
            continue
